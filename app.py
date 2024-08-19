from flask import Flask, render_template, request, redirect, url_for, flash

app=Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

USERS = {
    'user@example.com': 'senha123'
}


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
            return redirect(url_for('home'))
        else:
            flash('E-mail ou senha incorretos. Tente novamente.')
            return redirect(url_for('login'))
    return render_template('home.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/perfil', defaults={"nome":"usuario demo"})
@app.route('/perfil/<nome>')
def perfil():
    return render_template('perfil.html')


if __name__ == '__main__':
    app.run(debug=True)