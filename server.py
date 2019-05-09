from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('//')
def render_static():
	return render_template('hello.html')
 
if __name__ == '__main__':
	app.run(host='127.0.0.1', port='8080', debug=False)
