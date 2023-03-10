from flask import Flask, render_template, redirect, request, make_response
import uuid
import os

app = Flask(__name__)
app.config.from_object('config')

redirect_url = "http://www.example.com"
password = os.getenv("QR_PASS")
registered_users = []

@app.route('/', methods = ['POST', 'GET'])
def home():
    global redirect_url
    login_id = request.cookies.get('loginID')
    index = 'pages/index.html'
    login = 'pages/login.html'
    
    if request.method == 'GET':
        if login_id not in registered_users:
            return render_template(login)
        return render_template(index, redirect_url=redirect_url)
        
    if request.method == 'POST':
        if "password" in request.form:
            if request.form["password"] != password:
                return render_template(login, wrong_password="Mot de passe incorrect")
        
            identifier = uuid.uuid4()
            
            resp = make_response(render_template(index, redirect_url=redirect_url))
            resp.set_cookie('loginID', str(identifier), max_age=3600*24*2)
            registered_users.append(str(identifier))
            return resp
        
        if "redirect_url" in request.form and login_id in registered_users:
            redirect_url = request.form["redirect_url"]
            return render_template(index, redirect_url=redirect_url)
        return render_template(login)

@app.route('/redirect')
def about():
    return redirect(redirect_url, code=302)

# Error handlers.

@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

# Default port:
if __name__ == '__main__':
    app.run()
