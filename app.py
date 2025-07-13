from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

# Configuração de e-mail (opcional)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'seuemail@gmail.com'
app.config['MAIL_PASSWORD'] = 'suasenhaouappkey'

mail = Mail(app)

@app.route("/")
def index():
    return render_template("site.html")

@app.route("/inscrever", methods=["POST"])
def inscrever():
    email = request.form.get("email")
    if email:
        flash("Obrigado por se inscrever! Entraremos em contato por e-mail.", "success")
        # Aqui você pode salvar no banco ou enviar e-mail
        # msg = Message("Nova inscrição", sender=email, recipients=["suporte@escorel.com.br"])
        # msg.body = f"Novo e-mail inscrito: {email}"
        # mail.send(msg)
    else:
        flash("Erro: E-mail inválido.", "error")
    return redirect("/")

@app.route("/contato", methods=["POST"])
def contato():
    nome = request.form.get("nome")
    email = request.form.get("email")
    mensagem = request.form.get("mensagem")
    if nome and email and mensagem:
        flash("Mensagem enviada com sucesso!", "success")
        # msg = Message("Nova mensagem de contato", sender=email, recipients=["suporte@escorel.com.br"])
        # msg.body = f"Nome: {nome}\nE-mail: {email}\nMensagem: {mensagem}"
        # mail.send(msg)
    else:
        flash("Erro ao enviar mensagem. Preencha todos os campos.", "error")
    return redirect("/")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)