from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def main():
	return render_template('home.html')

@app.route('/members')
def member():
	return render_template('members.html')

if __name__ == '__main__':
    from views import *
    app.run(port=5000, debug=True)
