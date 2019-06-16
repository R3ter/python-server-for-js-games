from flask import render_template, session,request
from src.database import database
from src import main


class signupmethod():
    @staticmethod
    def method():
        try:
            username = request.form['username']
            password = request.form['password']
            repassword = request.form['password_confirm']
            email = request.form['email']
            if (username == ''):
                return render_template('signup.html',
                                       login=False, error='username')
            elif len(password) < 8:
                return render_template('signup.html',
                                       login=False, error='password')
            elif email == '':
                return render_template('signup.html',
                                       login=False, error='email')
            elif password != repassword:
                print(password + repassword)
                return render_template('signup.html',
                                       login=False, error='repassword')
            else:
                database.insertOne('accounts', {
                    "username": username,
                    "password": password,
                    "email": email
                })
                session['login'] = username
                return main.main.waleed()
        except Exception as e:
            print(e)
            try:
                return render_template('signup.html', login=session['login'])
            except:
                return render_template('signup.html', login=False)
