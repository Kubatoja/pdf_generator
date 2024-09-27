import smtplib
from email.message import EmailMessage
import mimetypes
from .details import *
from flask import jsonify
import os
import ssl

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

SMPT_SERVER = os.getenv("SMPT_SERVER")
SMPT_SERVER_PORT = os.getenv("SMPT_SERVER_PORT")


def send_mail(file, data):
    FILE_PATH = "./pdf_storage/"+file+".pdf"  # Path to the attachment
    
    RECIPIENT_EMAIL = data['recipient_email']
    USER_EMAIL = data['user_email']
    # !--Create the email content--!
    msg = EmailMessage()
    msg['Subject'] = f'Zlecenie nr. {data["order_No"]}'
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg.set_content(footer(data=data))
    # !--Create the email content--!

    
    # Determine the file's MIME type (e.g., application/pdf for PDFs)
    mime_type, _ = mimetypes.guess_type(FILE_PATH)
    if mime_type is None:
        mime_type = 'application/octet-stream'  # Default to binary if unknown
    main_type, sub_type = mime_type.split('/')

    # Attach the file
    with open(FILE_PATH, 'rb') as f:
        file_data = f.read()
        tmp = f.name
        file_name = tmp[13::]
        msg.add_attachment(file_data, maintype=main_type, subtype=sub_type, filename=file_name)

    context = ssl.create_default_context()
    # Connect to the SMTP server and send the email
    try:
        with smtplib.SMTP(SMPT_SERVER, SMPT_SERVER_PORT) as smtp:
            smtp.ehlo()  # Identify yourself to the server
            smtp.starttls(context=context)  # Secure the connection
            smtp.ehlo()  # Re-identify after TLS
            smtp.login(SENDER_EMAIL, EMAIL_PASSWORD)  # Login to your account
            
            # Send the email
            smtp.send_message(msg, to_addrs=[RECIPIENT_EMAIL, USER_EMAIL])
            return jsonify({"message":"Email sent succesfully"}), 200
    except Exception as e:
        return 500

