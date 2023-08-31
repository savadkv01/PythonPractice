import smtplib

to = input("Enter the email of the receiver")

message = input("Enter the message: ")


def sendEmail(to, message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('senderemail','password')
    server.sendmail(senderemail, to, message)
    server.close()
    
sendEmail()