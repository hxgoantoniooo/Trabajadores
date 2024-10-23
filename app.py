from flask import Flask, render_template, request
from flask_mail import Mail, Message
from datetime import datetime

app = Flask(__name__)

# Configuraciones de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'helper.apps.webservice@gmail.com'
app.config['MAIL_PASSWORD'] = 'bnup olmq kmfq acxc'
app.config['MAIL_DEFAULT_SENDER'] = 'Helper Apps'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    numero_personas = request.form['numero_personas']
    destinatario = "hugonzalezcontreras@gmail.com"  # Destinatario fijo
    fecha = datetime.now().strftime('%Y-%m-%d')

    mensaje = f"Hoy {fecha} fueron {numero_personas} personas,\nSaludos"

    msg = Message("Informe Diario", recipients=[destinatario])
    msg.body = mensaje

    mail.send(msg)
    return render_template('success.html', numero_personas=numero_personas, fecha=fecha)

if __name__ == '__main__':
    app.run(debug=True)
