from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')    
def rootHome():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/user')
def user():
    return render_template('user.html')

if __name__ == "__main__":
    app.run(debug=True)