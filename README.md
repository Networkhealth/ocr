# Persian OCR Web App

This is a web application for performing OCR (Optical Character Recognition) on Persian text.

## Features
- Upload an image containing Persian text.
- Extract and display the text using OCR.

## Structure
```
persian-ocr-webapp/
├── app/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── routes.py
│   └── ocr.py
├── requirements.txt
├── Dockerfile
├── render.yaml
└── README.md
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/persian-ocr-webapp.git
   ```

2. Navigate to the project directory:
   ```bash
   cd persian-ocr-webapp
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   flask run
   ```

## Deployment

This application is configured for deployment on [Render](https://render.com). Just connect your repository and Render will handle the rest.

## License

This project is licensed under the MIT License.
