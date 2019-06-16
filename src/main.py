import os

from flask import render_template, session,request
from os import listdir

list=listdir(os.path.dirname(os.path.realpath(__file__)+'/../static/js/'))
games=[]
for name in list:
    games.append(name.replace('.js',''))

class main():
    @staticmethod
    def waleed(error=False, nameerror=False, loginwrong=False):
        try:
            return render_template('main.html', logintry=bool(request.args.get('loginwrong')),
                                       error=error, name=nameerror, games=games,
                                       login=session['login'])
        except:
              return render_template('main.html',
                                       error=error, name=nameerror, games=games,
                    logintry=False,
                                       login=False)