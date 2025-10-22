from flask import Flask, request, send_file
from PyPDF2 import PdfMerger
import io
import os
from datetime import datetime

app = Flask(__name__, static_folder='.')

# Configure max file size (50MB)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

@app.route('/')
def index():
    """Serve the main HTML page"""
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return 'HTML file not found', 404

@app.route('/merge', methods=['POST'])
def merge_pdfs():
    """Merge multiple PDF files"""
    try:
        # Validate request
        if 'pdfs' not in request.files:
            return 'No files uploaded', 400
        
        files = request.files.getlist('pdfs')
        
        # Validate file count
        if len(files) < 2:
            return 'At least 2 PDFs required', 400
        
        # Filter and validate PDF files
        pdf_files = []
        for file in files:
            if file and file.filename:
                # Check filename
                if not file.filename.lower().endswith('.pdf'):
                    continue
                # Check MIME type
                if file.content_type not in ['application/pdf', 'application/x-pdf']:
                    continue
                pdf_files.append(file)
        
        # Validate that we have at least 2 PDFs after filtering
        if len(pdf_files) < 2:
            return 'At least 2 valid PDF files required', 400
        
        # Create PdfMerger and append each uploaded PDF (read into memory first)
        merger = PdfMerger()
        appended_any = False

        try:
            for pdf_file in pdf_files:
                try:
                    pdf_file.seek(0)
                    data = pdf_file.read()
                    if not data:
                        continue

                    bio = io.BytesIO(data)
                    # append accepts a file-like object
                    merger.append(bio)
                    appended_any = True
                except Exception:
                    # skip files that can't be read/parsed
                    continue

            if not appended_any:
                return 'Failed to merge: no readable PDF pages found', 400

            # Write merged PDF to memory
            output = io.BytesIO()
            merger.write(output)
            output.seek(0)

            # Generate filename with timestamp
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            download_name = f'merged_{timestamp}.pdf'

            return send_file(
                output,
                as_attachment=True,
                download_name=download_name,
                mimetype='application/pdf'
            )

        except Exception as merge_error:
            app.logger.exception('Error during PDF merge')
            return f'Error during merge: {str(merge_error)}', 500
        finally:
            try:
                merger.close()
            except Exception:
                pass
    
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return f'Unexpected error: {str(e)}', 500

@app.errorhandler(413)
def request_entity_too_large(error):
    """Handle file too large error"""
    return 'File size too large. Maximum 50MB allowed.', 413

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)