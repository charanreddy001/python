

import pywhatkit
india = +91
phno = input("enter phone number(in format of +919908386094) ")
mess = input("enter the message ")
hours = int(input("enter hour in 24h format "))
minu = int(input("enter minutes "))
pywhatkit.sendwhatmsg(phno, mess, hours, minu)




# pywhatkit.sendwhatmsg('+918519938511', 'hello Amrutha how are you',11, 35)