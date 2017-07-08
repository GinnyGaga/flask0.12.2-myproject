from flask import Flask 
app=Flask(__name__)

@app.route('/')
def hello_world():
	return '<h1>Ginny,you are so good!</h1>'

@app.route('/user/<username>')
def show_user_profile(username):
	return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'post %d' % post_id
