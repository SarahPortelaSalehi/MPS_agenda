
from flask.views import MethodView
from flask import request, render_template,redirect
from src.db import mysql


class IndexController(MethodView):
    def get(self):
        # with mysql.cursor() as cur:
            # cur.execute("SELECT * FROM agenda_usuarios")
            # data = cur.fetchall()
        return render_template('login.html')
    
    def post(self):
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
        return "cadastro realizado"
        # with mysql.cursor()as cur:
            # cur.execute("INSERT INTO agenda_usuarios( nome, email, senha) VALUES(%s,%s,%s,%s)", (nome, email, senha))
            # cur.connection.commit()
            # return redirect('/')
        
        
# class DeleteUserController(MethodView):
    # def get(self, id):
        # with mysql.cursor()as cur:
            # cur.execute("DELETE FROM agenda_usuarios WHERE email=%s", (id,))
            # cur.connection.commit()
            # return redirect('/')
        
# class UpdateUserController(MethodView):
    # def get(self, id):
            # return redirect('/')
        
        