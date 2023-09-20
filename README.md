
# Dynamic QR Code

This simple project is meant to have a static url (embeded in a QR code) redirect to a changing url.
This allows to change the url without changing the printed QR Code.


## Demo

A demo is currently hosted on Render [here](https://dynamicqrcode.onrender.com/).
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`QR_PASS` is the unique password for the app

## Run Locally

Clone the project

```bash
  git clone https://github.com/liamLatour/DynamicQRCode.git
```

Go to the DynamicQRCode

```bash
  cd DynamicQRCode
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  gunicorn app:app
```

Login at http://127.0.0.1:8000 and set the redirection url.  
Then go to http://127.0.0.1:8000/redirect to get redirected to the selected url.
