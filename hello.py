from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
	return 'hello,world!'
@app.route('/hello')
def ginny():
	return '<h1>Hello,ginny!</h1>'
