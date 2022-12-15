from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.config.from_object('config')

redirect_url = "http://www.example.com"

@app.route('/',methods = ['POST', 'GET'])
def home():
    global redirect_url
    if request.method == 'POST':
        redirect_url = request.form["redirect_url"]
    
    return render_template('pages/home.html', redirect_url=redirect_url)

@app.route('/redirect')
def about():
    return redirect(redirect_url, code=302)

# Error handlers.

@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

# Default port:
if __name__ == '__main__':
    app.run()
