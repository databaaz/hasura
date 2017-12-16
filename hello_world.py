from flask import Flask, request, redirect, make_response, render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello World - Shahbaz"

@app.route('/authors')
def authors():
	author_list = requests.get('https://jsonplaceholder.typicode.com/users').json()
	author_data = dict()
	for i in author_list:
		author_data[i['id']]=i['name']
	posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
	post_count=dict()
	for i in posts:
		u_id = i['userId']
		post_count[u_id] = post_count.get(u_id,0) + 1
	resp = ''
	for u_id in author_data:
		resp += (' '.join([str(author_data[u_id]),str(post_count[u_id])])+'<br>')
	return resp

@app.route('/setcookie')
def setCookie():
	#redirect_to_index = redirect('/')
	resp = app.make_response('Cookies Set !')
	resp.set_cookie('name', value='Shahbaz')
	resp.set_cookie('age', value='21')
	return resp
@app.route('/getcookie')
def getCookie():
	name = request.cookies.get('name')
	age = request.cookies.get('age')
	return 'name: '+ name + '<br>' + 'age: '+age

@app.route('/robots.txt')
def deny_robot():
	return r"""<pre>
          .-''''''-.
        .' _      _ '.
       /   O      O   \
      :                :
      |                |
      :       __       :
       \  .-"`  `"-.  /
        '.          .'
          '-......-'
     YOU SHOULDN'T BE HERE</pre>"""

@app.route('/image')    
def send_image():
	return app.send_static_file('sad_bot.jpg')
@app.route('/html')
def send_html():
	return render_template('home.html')

@app.route('/input')	
def send():
	return render_template('form.html')

@app.route('/send-name',  methods = ['POST'])	
def get_name():
	name = request.form['user_name']
	print(name)
	return 'Welcome '+name

