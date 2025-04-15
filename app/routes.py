from flask import render_template, request, jsonify, redirect, url_for
from app import app
from app.ocr import perform_ocr
import os
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            return redirect(request.url)
        
        file = request.files['image']
        if file.filename == '':
            return redirect(request.url)
        
        if file:
            image_bytes = file.read()
            extracted_text = perform_ocr(image_bytes)
            return render_template('result.html', 
                                 extracted_text=extracted_text,
                                 filename=file.filename)
    
    return render_template('index.html')

@app.route('/api/ocr', methods=['POST'])
def api_ocr():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No image selected'}), 400
    
    try:
        image_bytes = file.read()
        extracted_text = perform_ocr(image_bytes)
        return jsonify({'text': extracted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500