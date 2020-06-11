from flask import Flask, jsonify, render_template

app = Flask('flaskconftest', template_folder='./static')

@app.route('/')
def start():
    return render_template('welcome.html')

@app.route('/html/<var>')
def start_html(var):
    return render_template('welcome.html', var=var,)

@app.route('/<var>')
def var_pass(var):
    return f'A variável passada foi {var}.'

@app.route('/user/<var>')
def user_loged(var):
    return f'usuário logado: {var}.', 201

@app.route('/employees/<name>')
def list_employees(name):
    r = {
            'nome': name,
            'idade': 42
        }
    return jsonify(r)

app.run(port=3001)