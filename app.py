from flask import Flask, request, send_file
from PyPDF2 import PdfWriter
import io

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/merge', methods=['POST'])
def merge_pdfs():
    if 'pdfs' not in request.files:
        return 'No files uploaded', 400
    
    files = request.files.getlist('pdfs')
    if len(files) < 2:
        return 'At least 2 PDFs required', 400
    
    merger = PdfWriter()
    
    try:
        # Process each PDF file
        for file in files:
            # Verify it's a PDF (basic check)
            if not file.filename.lower().endswith('.pdf'):
                continue
                
            # Add to merger
            merger.append(file)
        
        # Create in-memory PDF
        output = io.BytesIO()
        merger.write(output)
        output.seek(0)
        
        return send_file(
            output,
            as_attachment=True,
            download_name='merged.pdf',
            mimetype='application/pdf'
        )
        
    except Exception as e:
        return f'Error merging PDFs: {str(e)}', 500
    finally:
        merger.close()

if __name__ == '__main__':
    app.run(debug=True)