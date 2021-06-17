#1
from flask import Flask , request , render_template , sessions
#3
#4
#5
us="username: "
#6
app=Flask(__name__)
app.static_folder = 'static'
@app.route('/')
def signin():
    return(render_template('index h.html'))
@app.route('/blog')
def signi():
    return(render_template('blog.html'))

@app.route('/blog/kali-install')
def kali():
    return(render_template('ins-kali.html'))
#12
#13
if __name__=="__main__":
    app.run(debug=True)
#16
