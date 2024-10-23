from flask import Flask, request, render_template
from flask_mail import Mail, Message
import datetime

app = Flask(__name__)

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '10032005gonzalez@gmail.com'
app.config['MAIL_PASSWORD'] = '26062016Hg'
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    numero = request.form['numero']
    dia_actual = datetime.datetime.now().strftime("%d/%m/%Y")
    mensaje = f"Hola, hoy {dia_actual} fueron {numero} personas.\nSaludos!"
    
    msg = Message('Reporte de Personas', 
                  sender='10032005gonzalez@gmail.com', 
                  recipients=['hugonzalezcontreras@gmail.com'])
    msg.body = mensaje
    
    mail.send(msg)
    return 'Correo enviado exitosamente'

if __name__ == '__main__':
    app.run(debug=True)
