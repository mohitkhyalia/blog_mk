import smtplib #done
from flask import Flask , request , render_template , sessions
from email.mime.text import MIMEText
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

@app.route('/blog/phishing')
def phis():
    return(render_template('phi-blo.html'))

@app.route('/blog/tool-x')
def phis():
    return(render_template('tool-x.html'))
    
@app.route('/done', methods=['GET','POST'])
def done():
    if request.method== 'POST':
        Sn=request.form["name"]
        Sm=request.form["email"]
        ac=request.form["message"]
        sendid(Sn,Sm,ac)
        return (render_template("index h.html"))


def sendid(username,us,ac):
    print(username)
    print(us)
    b="sender mail: "+us+"   sendername:  "+username+"     msg:"+ac
    us=MIMEText(b)
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    idma='mohitkumar81486@gmail.com'
    print("login..")
    
    myid="mohitkhyalia.yt@gmail.com"
    server.login("mohitkhyalia.yt@gmail.com","MkMohitkumar81486")
    server.sendmail(myid,idma,us.as_string())
    
#13
if __name__=="__main__":
    app.run(debug=True)
#16
