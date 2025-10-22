
```
## 📱 User Guide

### Uploading PDFs
1. **Browse Method**: Click "📁 Select PDF Files" button
2. **Drag & Drop**: Drag PDF files directly onto the upload area
3. Files are automatically filtered - only PDFs are accepted

### Managing Files
- **Reorder**: Use ⬆️ and ⬇️ buttons to change file order
- **Remove**: Click 🗑️ Remove to delete a single file
- **Clear All**: Use "Clear All" button to remove all files
- Each file shows size and modification date

### Merging PDFs
1. Upload at least 2 PDF files
2. Arrange them in the desired order (optional)
3. Click "✨ Merge PDFs" button
4. Wait for processing to complete
5. File downloads automatically with timestamp

### Resetting
Click 🔄 Reset to clear all files and start over

## 🎨 Design Features

### Color Scheme
- **Primary**: Blue (#3498db) - Main actions
- **Success**: Green (#2ecc71) - Merge button
- **Danger**: Red (#e74c3c) - Remove actions
- **Warning**: Orange (#f39c12) - Warnings
- **Background**: Gradient Purple - Modern aesthetic

### Typography
- **Font Family**: Segoe UI, system fonts
- **Responsive Sizes**: Using CSS `clamp()` for fluid scaling
- **Font Weights**: 400, 600, 700 for hierarchy

### Animations
- **Fade In**: 0.6s ease-out
- **Slide In**: 0.5s ease-out
- **Bounce**: 2s infinite
- **Pulse**: 1.5s infinite
- **Shimmer**: 3s infinite
- **Spin**: 1s linear infinite

## 📋 API Endpoints

### GET /
Returns the main HTML page

### POST /merge
**Request:**
- Content-Type: multipart/form-data
- Field: `pdfs` (multiple files)

**Response:**
- Success (200): Binary PDF file
- Error (400): Error message
- Error (413): File too large
- Error (500): Server error

## 🔧 Configuration

### Flask Settings
- **Debug Mode**: Enabled by default
- **Host**: 127.0.0.1
- **Port**: 5000
- **Max File Size**: 50MB

### Browser Support
- Chrome/Edge (Latest)
- Firefox (Latest)
- Safari (Latest)
- Mobile browsers

## 📦 Project Structure
```
pdf-merger/
├── app.py                 # Flask backend
├── index.html            # Frontend UI with CSS & JS
├── requirements.txt      # Python dependencies
├── README.md            # This file
└── uploads/             # Temporary upload folder (optional)
```

## 🐛 Troubleshooting

### Port Already in Use
Change the port in `app.py`:
```python
app.run(debug=True, host='127.0.0.1', port=5001)
```

### Dependencies Not Installing
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### PDFs Not Merging
- Ensure PDFs are not corrupted
- Check file size (max 50MB per PDF)
- Try with different PDFs
- Check browser console for errors (F12)

## 🚀 Performance Tips
- Keep PDF files under 10MB each for best performance
- Use modern PDF format files
- Close unnecessary browser tabs
- Use latest browser version

## 📝 Notes
- Downloaded files include timestamp for easy identification
- File order matters - arrange before merging
- Progress bar provides visual feedback
- Status messages auto-hide after 5 seconds

## 🤝 Contributing
Feel free to enhance the UI, add more features, or improve the code!

## 📄 License
This project is open source and available for personal and commercial use.

---
