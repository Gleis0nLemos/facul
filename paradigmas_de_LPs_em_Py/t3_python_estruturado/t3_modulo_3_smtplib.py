#import dos pacotes necessários
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# criação de um objeto de mensagem
msg = MIMEMultipart()
texto = "Estou enviando um email com Python"

#parâmetros
senha = "senha"
msg['From'] = "gleison04lemos@gmail.com"
msg["To"] = "atendimentoshome01@gmail.com"
msg["Subject"] = "Segura o hackerman kk"

# smtp_server = 'smtp.gmail.com'
# smtp_port = 587

#criação do corpo da mensagem
msg.attach(MIMEMultipart(texto, 'plain'))

#criação do servidor
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

#Login na conta para envio
server.login(msg['From'], senha)

#envio da mensagem
server.sendmail(msg['From'], msg['To'], msg.as_string())

#encerramento do servidor
server.quit()

print('Mensagem enviada com sucesso')






# ABAIXO ---> OUTRA FORMA DE SE ENVIAR UM E-MAIL COM UM SCRIPT PYTHON

# import smtplib
# import email.message

# def enviar_email():
#     smtp_server = 'smtp.gmail.com'
#     smtp_port = 587
    
#     corpo_email = """
#     <p>Hackerman kk</p>
#     """

#     msg = email.message.Message()
#     msg['From'] = "gleison04lemos@gmail.com"
#     msg["To"] = "gleison04lemos@gmail.com"
#     msg["Subject"] = "Segura o hackerman kk"
#     password = "senha"
#     msg.add_header('Content-Type', 'text/html')
#     msg.set_payload(corpo_email)

    

#     s = smtplib.SMTP(smtp_server, smtp_port)
#     s.starttls()
#     # Login Credentials for sending the mail
#     s.login(msg['From'], password)
#     s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
#     print('Email enviado')

# enviar_email()