from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')

def home():
	username = "Tashvin"
	#title = "Flipkart"
	element_h1 = "Welcome to Flipkart"
	return render_template('home.html', username = username, h1 = element_h1, home='home') #title=title)

@app.route('/about')

def about():
	return render_template('about.html')

@app.route('/Contact')

def contact():
	return render_template('contact.html')

@app.route('/welcome')

def welcome():
	return render_template('welcome.html')

@app.route('/login',methods = ['POST'])

def login():

	user = {'username':'tashvin','password':'12345'}

	username = request.form['username']
	password = request.form['password']

	if user['username'] == username:
		if user['password'] == password:
			return redirect(url_for('welcome'))
		return "wrong password, go back and try again!"
	return "this uer doesn't exist.go back and enter a valid user"

if __name__ == '__main__':
	app.run(debug=True)