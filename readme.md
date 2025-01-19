# SociallySecure

SociallySecure is a full-stack web application designed to detect sensitive data in images, preventing accidental uploads to social media. The application utilizes Optical Character Recognition (OCR) technology, specifically **EasyOCR** and **Tesseract OCR**, to scan images for sensitive information, ensuring robust data privacy and protection.

The application allows users to scan documents and compare the text found in the scanned image with previously saved data, offering added security and privacy.

## Features

- **Sensitive Data Detection:** Automatically detects sensitive information in images using **EasyOCR** and **Tesseract OCR**.
- **User Authentication:** Secure user authentication with encrypted credential storage.
- **Data Privacy:** Ensures user data is handled with strict privacy standards.
- **Document Scanning:** Allows users to upload and scan documents to detect text and compare it with previously saved data.
- **Machine Learning Integration (In Progress):** Currently enhancing the application with machine learning classification to flag inappropriate content.

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript

- **Backend:** Django, Django REST Framework, Python

- **Databases:** SQLite for development

- **Libraries:** OpenCV, EasyOCR, Tesseract OCR, NumPy, Pandas

- **Tools:** Git, GitHub, VS Code

## Installation

### Manual Setup

To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AkashDas253/SociallySecure.git
   cd SociallySecure
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install EasyOCR:**
   ```bash
   pip install easyocr
   ```

5. **Create a `.env` file in the root directory:**
   ```bash
   touch .env
   ```

6. **Add the following environment variables to the `.env` file:**
   ```
   SECRET_KEY=generated-key
   DEBUG=True | False
   ENCRYPTION_KEY=generated-key
   OCR_ENGINE=EASYOCR | TESSERACT
   FERMAT_KEY=generated-key
   ```

7. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

8. **Start the server:**
   ```bash
   python manage.py runserver
   ```

9. **Open your browser and go to** `http://127.0.0.1:8000/`.

## Usage

1. **Sign up or log in** to the application.
2. **Upload an image** containing potentially sensitive information or a document for OCR processing.
3. The app will **process the image** using EasyOCR or Tesseract OCR and extract any text found.
4. The detected text will be **compared with previously saved data** from your registered account to check for any sensitive information.
5. If sensitive data is detected, the application will **notify you**.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## Acknowledgments

- Special thanks to the developers of [EasyOCR](https://github.com/JaidedAI/EasyOCR) and [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for their outstanding OCR libraries.
- Thanks to [Django](https://www.djangoproject.com/) for providing a robust web framework.
