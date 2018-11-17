import smtplib
from settings import CONST_EMAIL, CONST_PW, RECIP_EMAIL

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(CONST_EMAIL, CONST_PW)
smtpObj.sendmail(CONST_EMAIL, RECIP_EMAIL,
                 'Subject: Automated Email with Python3.\nHello World!')
smtpObj.quit()
print('Goodbye!')
