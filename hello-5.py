from flask import Flask,session,redirect,url_for,escape,request

app=Flask(__name__)

@app.route('/')
def index():
	if 'username' in session:
		return 'Logged in as %s' % escape(session['username'])
	return 'You are not logged in '

@app.route('/login',methods=['GET','POST'])
def login():
	
	if request.method == 'POST':
		session['username']=request.form['username']
		return redirect(url_for('index'))	
	return '''
		<form method="post">
			<p><input type=text name=username
			<p><input type=submit value=login>		'''

@app.route('/logout')
def logout():
	session.pop('username',None)
	return redirect(url_for('index'))

app.secret_key = b'\xa4?\xf8v\x96$\rj \x19\xa1;&\xb4\xb8g\x85\x9d\xe0\x95\xa3kbN'





