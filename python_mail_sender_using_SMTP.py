###PYTHON PROGRAM TO SEND AN EMAIL USING SMTP LIB

import smtplib

smtp = smtplib.SMTP('smtp.gmail.com',587)

smtp.starttls()

smtp.login("Enter your sender's email Id","sender's password")

message = input("Enter your Message here")

smtp.sendmail("sender's email Id","receiver's email Id",message)

smtp.quit()

