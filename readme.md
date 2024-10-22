# SociallySecure

SociallySecure is a full-stack web application designed to detect sensitive data in images, preventing accidental uploads to social media. The application utilizes Optical Character Recognition (OCR) technology to scan images for sensitive information, ensuring robust data privacy and protection.

## Features

- **Sensitive Data Detection:** Automatically detects sensitive information in images using OCR.
- **User Authentication:** Secure user authentication with encrypted credential storage.
- **Data Privacy:** Ensures user data is handled with strict privacy standards.
- **Machine Learning Integration (In Progress):** Currently enhancing the application with machine learning classification to flag inappropriate content.

## Tech Stack

- **Frontend:**
  - HTML
  - CSS
  - JavaScript

- **Backend:**
  - Django
  - Django REST Framework
  - Python

- **Databases:**
  - PostgreSQL (or SQLite for development)

- **Libraries:**
  - OpenCV
  - Tesseract OCR
  - NumPy
  - Pandas

- **Tools:**
  - Git
  - Docker
  - VS Code

## Installation

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

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the server:**
   ```bash
   python manage.py runserver
   ```

6. **Open your browser and go to** `http://127.0.0.1:8000/`.

## Usage

1. Sign up or log in to the application.
2. Upload an image containing potentially sensitive information.
3. The app will process the image and notify you if any sensitive data is detected.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the developers of [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for their outstanding OCR library.
- Thanks to [Django](https://www.djangoproject.com/) for providing a robust web framework.
