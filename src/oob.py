from time import gmtime, strftime

from flask import Flask, render_template, session, request, url_for
import os
from os import listdir
import zipfile
import tempfile

from werkzeug.utils import redirect

from src import main
from src.database import database
from src.sginupmethod import signupmethod

app=Flask(__name__)

app.secret_key='waleed23'

database.init("waleed",'waleed23')


@app.route('/game:<string:name>')
def hello(name):
    return render_template("game.html",name=name)

@app.route('/signup',methods=['POST','get'])
def signup():
    return (signupmethod.method())

@app.route('/')
def waleed(error=False,nameerror=False,loginwrong=False):
    return main.main.waleed()

@app.route('/logout',methods=['post','get'])
def logout():
    session['login']=''
    return redirect('/')

@app.route('/uploadgame',methods=['post'])
def upload():
    if(request.form['name'] is ''):
      return waleed(nameerror=True)
    get = database.getOne('games', {"name": request.form['name']})
    if(get=="None" or get==None ):
        f = request.files['file']
        if(f.filename.endswith('.zip')):
           f.save(os.path.join('./uploaded', request.form['name']+'.zip'))
           inset= database.insertOne('games',
                           {"name": request.form['name'],
                            "time":strftime("%d %D %Y %H:%M ", gmtime())
                            ,"state":"wating"})

           return render_template('uploadgame.html',
                           name=request.form['name'])
        else:
           return waleed(error=True)

    return render_template('uploadgame.html',
                               name=request.form['name'],exists=True)

@app.route('/test',methods=['post','get'])
def test():
    return ''

@app.route('/login',methods=['post','get'])
def login():
    email = request.form['email']
    password = request.form['password']
    check=database.getOne('accounts',{'username':email,"password":password})
    if(check is not None and check is not 'None'):
        session['login']=email
    else:
        return redirect(url_for('waleed',loginwrong=True))
    return redirect('/')

@app.route('/uploadedgames')
def uploadedgames():
    uploaded_games=database.getMany('games')
    return render_template('uploadedgames.html',games=uploaded_games
                           ,login=session['login'])

if(__name__=="__main__"):
    app.run(port=3000,debug=True)


