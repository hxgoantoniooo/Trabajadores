from flask import Flask, render_template, request
from flask_mail import Mail, Message
from datetime import datetime

app = Flask(__name__)

# Configuraciones de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '10032005gonzalez@gmail.com'
app.config['MAIL_PASSWORD'] = 'hspa odbg pwxe rnqx'
app.config['MAIL_DEFAULT_SENDER'] = '10032005gonzalez@gmail.com'

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
    return "Correo enviado exitosamente!"

if __name__ == '__main__':
    app.run(debug=True)
