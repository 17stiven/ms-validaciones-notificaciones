from flask import Flask
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask import request



app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/email")
def enviarCorreo():
    hashString=request.args.get("hash")
    if(hashString==os.environ.get('SECURITY_HASH')):
        destino=request.args.get("correo_destino")
        asunto=request.args.get("asunto")
        mensaje=request.args.get("mensaje")
        
        
        message = Mail(
        from_email='1704stiven@gmail.com',
        to_emails=destino,
        subject=asunto,
        html_content=mensaje)
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print("enviado")
            
            return "ok"
        except Exception as e:
            print(e.message)
            return "ko"
    else:
            print("sin hash")
            return "hash error"
    


if __name__== '__main__':
    app.run()
