import smtplib

def mail_send(email,password,subject_c, body_c, mail_to):
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email,password)

        subject = subject_c
        body = body_c

        message = f'Subject: {subject} \n\n{body}'
            
        smtp.sendmail(email, mail_to, message)
