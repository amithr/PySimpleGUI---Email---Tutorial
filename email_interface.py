import smtplib, ssl

def send_email(message, recipient_email):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email="studyiochannel@gmail.com"
    password = "studyio23"

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, message)
    except Exception as e:
        print(e)
    finally:
        server.quit()

