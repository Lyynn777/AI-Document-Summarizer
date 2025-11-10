from flask import Flask, render_template, request
from summarizer import extract_text_from_pdf, summarize_text
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    uploaded_file = request.files['document']
    if uploaded_file and uploaded_file.filename.endswith('.pdf'):
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        uploaded_file.save(file_path)

        text = extract_text_from_pdf(file_path)
        summary = summarize_text(text)
        return render_template('summary.html', summary=summary)
    return "Please upload a valid PDF file."

if __name__ == '__main__':
    app.run(debug=True)
