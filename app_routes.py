# Define the routes for the web application
from flask import render_template, request
from .ocr import perform_ocr

def setup_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/upload', methods=['POST'])
    def upload():
        file = request.files['file']
        result = perform_ocr(file)
        return render_template('result.html', result=result)