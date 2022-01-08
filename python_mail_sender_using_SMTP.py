#Importing SMTP Library
import smtplib

smtp = smtplib.SMTP('smtp.gmail.com',587)

smtp.starttls()

smtp.login("Enter your email Id","Enter your password")

message = input("Enter your Message here")

smtp.sendmail("sender's email Id","receiver's email Id",message)

smtp.quit()

