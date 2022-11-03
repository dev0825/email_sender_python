import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_f(recipient, subject, body):
    email_addr = "theoneguy6942@gmail.com"
    #msg = EmailMessage()
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = email_addr
    msg["To"] = recipient
    body=MIMEText(body)
    msg.attach(body)
    #msg. = body

    # with open("face.png", "rb") as fp:
    #     img_data = fp.read()
    # msg.add_attachment(img_data, maintype="image", subtype=imghdr.what(None, img_data))

    session = smtplib.SMTP("smtp.gmail.com", 587)
    session.starttls()
    session.login(email_addr, "pkye kuet qkwp nuos")
    text = msg.as_string()
    session.sendmail(email_addr, recipient, text)
    session.quit()
    return "Mail Sent"


from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/send_email", methods=["POST"])
def send_email():
    json_data = request.get_json()
    # print(json_data["body"])  # type: ignore
    # return_response = "succcess"
    return_response = send_email_f(
        json_data["recipient"], json_data["subject"], json_data["body"]  # type:ignore
    )
    if return_response:
        response = {
            "message": "Success",
        }
    else:
        response = {
            "message": "Failed",
        }
    return jsonify(response), 201


app.run(host="192.168.222.191", port=5001)
