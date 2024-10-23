from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

app = Flask(__name__)

# Función para enviar correo
def send_email(to_address, subject, body):
    from_address = "10032005gonzalez@gmail.cl"
    password = "26062016Hg"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_address
    msg["To"] = to_address

    # Conexión al servidor SMTP
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(from_address, password)
        server.sendmail(from_address, to_address, msg.as_string())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email_route():
    # Obtener los datos del formulario
    name = request.form['name']
    number = request.form['number']

    # Obtener la fecha actual
    day = datetime.now().strftime("%d/%m/%Y")

    # Cuerpo del mensaje
    body = f"Hola {name},\n\nHoy {day} fueron {number} personas.\n\nSaludos."

    # Enviar correo
    send_email("hugonzalezcontreras@gmail.com", "Reporte de personas", body)

    return f"Correo enviado a hugonzalezcontreras@gmail.com con el número {number} de personas"

if __name__ == '__main__':
    app.run(debug=True)
