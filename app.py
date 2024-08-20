from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

# Usuarios exemplo
USERS = {
    'user@example.com': 'senha123'
}

# Jogos exemplo
jogos_mais_jogados = [
    {'nome': 'Jogo A', 'jogadores': 5000},
    {'nome': 'Jogo B', 'jogadores': 3500},
]

jogos_recentes = [
    {'nome': 'Jogo X', 'data_adicao': '2024-08-10'},
    {'nome': 'Jogo Y', 'data_adicao': '2024-08-15'},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if USERS.get(email) == password:
            session['usuario'] = email  # Armazena o email na sessão
            return redirect(url_for('home'))
        else:
            flash('E-mail ou senha incorretos. Tente novamente.')
            return redirect(url_for('login'))
    
    return render_template('home.html', jogos_mais_jogados=jogos_mais_jogados, jogos_recentes=jogos_recentes)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/perfil', defaults={"nome": "usuario demo"})
@app.route('/perfil/<nome>')
def perfil(nome):
    return render_template('perfil.html', nome=nome)

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Você foi deslogado com sucesso.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
