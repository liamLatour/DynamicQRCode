# Dynamic QR Code

DynamicQRCode is a Flask web application that allows users to generate and configure dynamic QR codes for redirection purposes.

## Features

- User authentication with password protection.
- Customizable redirection URL.
- Error handling for 404 and 500 status codes.
- Stylish and responsive web interface.

## Getting Started

### Prerequisites

Make sure you have Python installed. Additionally, install the required dependencies:

```bash
pip install -r requirements.txt
```

### Configuration

Set up the configuration by creating a `.env` file and providing the required environment variables, including the QR code password.

```plaintext
QR_PASS=your_password_here
```

### Running the Application

Run the application using the following command:

```bash
gunicorn app:app
```

Visit [http://localhost:8000](http://localhost:8000/) in your web browser to access the application.
Then go to [http://localhost:8000/redirect](http://localhost:8000/redirect) to get redirected to the selected url.

## Contributing

Feel free to contribute to the project by opening issues or creating pull requests. Your feedback and contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit/)  file for details.
