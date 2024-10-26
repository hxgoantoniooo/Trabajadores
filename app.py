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
    # Obtener el número de trabajadores de cada día
    data = {
        "lunes": request.form['lunes'],
        "martes": request.form['martes'],
        "miércoles": request.form['miercoles'],
        "jueves": request.form['jueves'],
        "viernes": request.form['viernes'],
        "sábado": request.form['sabado']
    }
    fecha = datetime.now().strftime('%Y-%m-%d')
    
    # Crear el mensaje
    mensaje = f"Reporte semanal de trabajadores (semana del {fecha}):\n\n"
    for dia, cantidad in data.items():
        mensaje += f"{dia.capitalize()}: {cantidad} trabajadores\n"
    mensaje += "\nSaludos"
    
    # Configurar y enviar el correo
    msg = Message("Informe Semanal de Trabajadores", recipients=["hugonzalezcontreras@gmail.com"])
    msg.body = mensaje

    mail.send(msg)
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
