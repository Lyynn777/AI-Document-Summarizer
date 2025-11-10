from transformers import pipeline
import pdfplumber
import re

# 🧠 Load lightweight summarization model (~300 MB)
summarizer = pipeline("summarization", model="t5-small")

def extract_text_from_pdf(file_path):
    """Extract and clean raw text from a PDF."""
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += " " + page_text
    # remove extra whitespace
    return re.sub(r"\s+", " ", text).strip()

def summarize_text(text):
    """Return a clean bullet-point summary."""
    if len(text) < 50:
        return "Text too short to summarize."

    # ---------- split text into manageable chunks ----------
    max_chunk = 800
    sentences = text.split(". ")
    chunks, current_chunk = [], ""
    for s in sentences:
        if len(current_chunk) + len(s) <= max_chunk:
            current_chunk += s + ". "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = s + ". "
    chunks.append(current_chunk.strip())

    # ---------- run summarization ----------
    all_summaries = []
    for chunk in chunks:
        prompt = "summarize: " + chunk
        result = summarizer(prompt, max_length=200, min_length=60, do_sample=False)
        all_summaries.append(result[0]["summary_text"])

    summary = " ".join(all_summaries)

    # ---------- cleanup ----------
    # remove echoes or web footers
    bad_phrases = [
        r"write\s+\d+", r"avoid", r"academic", r"contact\s+us",
        r"click\s+here", r"free\s+consultation", r"latest\s+news",
        r"if you have any questions.*", r"for more information.*",
        r"for all the latest.*"
    ]
    for bp in bad_phrases:
        summary = re.sub(bp, "", summary, flags=re.IGNORECASE)

    # remove section numbers like 1.6.4.1
    summary = re.sub(r"\b\d+(\.\d+)+\b", "", summary)
    # fix broken hyphenated words
    summary = re.sub(r"(\w+)-\s+(\w+)", r"\1\2", summary)
    # collapse duplicated words
    summary = re.sub(r"\b(\w+)\s+\1\b", r"\1", summary, flags=re.IGNORECASE)
    # normalize punctuation
    summary = re.sub(r"\.\s*\.", ".", summary)
    summary = re.sub(r"\s+", " ", summary).strip()

    # ---------- bullet formatting ----------
    lines = [
        l.strip().capitalize()
        for l in re.split(r"\.\s+", summary)
        if l.strip() and len(l.strip()) > 5
    ]
    summary = "\n• " + "\n• ".join(lines)

    # final polish
    summary = re.sub(r"analytics analytics", "analytics", summary, flags=re.IGNORECASE)
    summary = re.sub(r"\s+\.", ".", summary)
    summary = summary.strip()

    return summary
