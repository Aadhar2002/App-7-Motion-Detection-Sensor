import smtplib
from email.message import EmailMessage
import imghdr

PASSWORD = "Write your password"
SENDER = "Write Sender's Email"
RECIEVER = "Write Recievers Email"
def send_email(image_path):
    print("Send_email started")
    email_message = EmailMessage()
    email_message["Subject"] = "Motion Detected!"
    email_message.set_content("Hey some movement was detected by the app!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype = "image", subtype = imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECIEVER, email_message.as_string())
    gmail.quit()
    print("send email ended")


if __name__ == "__main__":
    send_email(image_path="images/20.png")
