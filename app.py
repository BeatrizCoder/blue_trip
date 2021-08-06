from flask import Flask, render_template, redirect, request, session, flash
from flask_mail import Mail, Message #Importa o Mail e o Message do flask_mail para facilitar o envio de emails
from flask_sqlalchemy import SQLAlchemy # ORM responsável por realizar as operações do banco de dados via Python

app = Flask(__name__)
app.secret_key = 'Bluetrip' # Chave de criptografia para guardar sessão de login

# mail_settings = {
#     "MAIL_SERVER": 'smtp.gmail.com',
#     "MAIL_PORT": 465,
#     "MAIL_USE_TLS": False,
#     "MAIL_USE_SSL": True,
#     "MAIL_USERNAME": 'bluetrip.contato@gmail.com',
#     "MAIL_PASSWORD": 'Bluetrip123'
# }

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://xogpdzxt:XVt_V6xupNzrflQArM6JggGA-XTBS8oR@kesavan.db.elephantsql.com/xogpdzxt'
db = SQLAlchemy(app)


class NotificacaoEmail:
   def __init__ (self, destino, preco, descricao):
      self.destino = destino
      self.preco = preco
      self.descricao = descricao

    
class Viagem(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    destino = db.Column(db.String(150), nullable=False)
    preco = db.Column(db.String(10000), nullable=False)
    descricao = db.Column(db.String(500), nullable=False)
    link = db.Column(db.String(300), nullable=False)
   
    def __init__(self, destino, imagem, descricao, link, tipo_viagem):
        self.destino = destino
        self.imagem = imagem
        self.descricao = descricao
        self.link = link
        self.tipo_viagem = tipo_viagem


# ----------- ROTAS -------------

@app.route('/')
def index():
   session['usuario_logado'] = None
   viagens = Viagem.query.all()  # Busca todas as viagens no banco e coloca na variável Viagem, que se transforma em uma lista.
   return render_template('index.html', viagens=viagens) # Renderiza a página index.html mandando a lista de projetos

@app.route('/pacotes')
def pacotes():
    return render_template('pacotes.html')

@app.route('/missao')
def missao():
    return render_template('missao.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/login')
def login():
    return render_template('login.html')


# ROTAS DE CRUD

# CREATE
@app.route('/new', methods=['GET', 'POST'])
def new():
   if request.method == 'POST':     
      viagem = Viagem(
         request.form['destino'],
         request.form['imagem'],
         request.form['preco'],
         request.form['link'],
         request.form['tipo-viagem']
      )
      db.session.add(viagem) # Adiciona o objeto projeto no banco de dados.
      db.session.commit() # Confirma a operação
      flash('Viagem adicionada ao catálogo com sucesso!') # Mensagem de sucesso.
      return redirect('/admin') # Redireciona para a rota admin

# Rota edit que recebe um paremetro
@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
   viagem = Viagem.query.get(id) # Busca um projeto no banco através do id
   viagens = Viagem.query.all()
   if request.method == "POST": # Se a requisição for um POST, faça:
      # Alteração de todos os campos de projetoEdit selecionado no get id
      viagem.destino = request.form['destino']
      viagem.preco = request.form['preco']
      viagem.imagem = request.form['imagem']
      viagem.link = request.form['link']
      viagem.tipo_viagem = request.form['tipo-viagem']
      db.session.commit() # Confirma a operação
      return redirect('/admin') #Redireciona para a rota adm
   # Renderiza a página adm.html passando o projetoEdit (projeto a ser editado)
   return render_template('admin.html', viagem=viagem, viagens=viagens)

if __name__ == '__main__':
   db.create_all() # Cria o banco assim que a aplicação é ligada.
   app.run(debug=True)