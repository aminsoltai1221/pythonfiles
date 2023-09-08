# import secure_smtplib as smtp
# from email.mime.text import MIMEText

# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
# username = 'aminsoltani.1221@gmail.com'
# password = 'Hossain110@'


# with smtp.SMTPS(smtp_server, smtp_port) as server:
#     server.starttls()
#     server.login(username, password)
    
# msg = MIMEText("Hi, are u good amin? it's a new email")
# msg['Subject'] = 'عنوان ایمیل'
# msg['From'] = 'aminsoltani.1221@gmail.com'
# msg['To'] = 'aminsoltani.137979@gmail.com'

# server.sendmail(username, 'aminsoltani.137979@gmail.com', msg.as_string())



# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# # اطلاعات حساب جیمیل خود را وارد کنید
# email_address = 'aminsoltani.1221@gmail.com'
# password = 'Hossain110@'

# # اتصال به سرور SMTP جیمیل
# smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
# smtp_server.starttls()

# # ورود به حساب کاربری
# smtp_server.login(email_address, password)

# # ساخت نامه الکترونیکی
# msg = MIMEMultipart("Hi, are u good amin? it's a new email")
# msg['From'] = email_address
# msg['To'] = 'aminsoltani.137979@gmail.com' # آدرس ایمیل گیرنده را وارد کنید
# msg['Subject'] = 'موضوع ایمیل'

# # body = 'متن ایمیل'
# # msg.attach(MIMEText(body, 'plain'))

# # ارسال ایمیل
# smtp_server.send_message(msg)

# # خاتمه ارتباط با سرور SMTP جیمیل
# smtp_server.quit()






# import smtplib
# from email.mime.text import MIMEText

# # مشخصات حساب جیمیل خود را وارد کنید
# gmail_user = 'your_email@gmail.com'
# gmail_password = 'Hossain110@'

# # مشخصات فرستنده و گیرنده را تعریف کنید
# sender = 'aminsoltani.1221@gmail.com'
# recipients = ['aminsoltani.137979@gmail.com']

# # محتوای ایمیل را تعریف کنید
# subject = 'مثال ارسال ایمیل با استفاده از جیمیل SMTP'
# message = 'سلام!\nاین یک نمونه ایمیل است.'

# msg = MIMEText(message, 'plain', 'utf-8')
# msg['Subject'] = subject
# msg['From'] = sender
# msg['To'] = ', '.join(recipients)

# # بر قراری ارتباط با سرور SMTP جیمیل
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.ehlo()
# server.starttls()

# # ورود به حساب کاربری جیمیل
# server.login(gmail_user, gmail_password)

# # ارسال ایمیل
# server.send_message(msg)
# server.quit()





import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# اطلاعات حساب جیمیل خود را وارد کنید
sender_email = 'aminsoltani.1221@gmail.com'
sender_password = "iyyvvpkdqegcrwls"
# اطلاعات گیرنده و محتوای ایمیل را وارد کنید
receiver_email = 'aminsoltani.137979@gmail.com'
subject = 'مثال ارسال ایمیل با استفاده از جیمیل SMTP'
message_body = "Hello, this is the body of the email."

# تنظیم ایمیل
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
# msg.attach(MIMEText(message_body, plain))

try:
    # برقراری ارتباط با سرویس SMTP جیمیل
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        
        # ارسال ایمیل
        smtp.send_message(msg)
        print("یمیل با موفقیت ارسال شد!")
except smtplib.SMTPAuthenticationError:
    print("SMTPAuthenticationError")
except smtplib.SMTPException as e:
    print("خطا در ارسال ایمیل:", repr(e))