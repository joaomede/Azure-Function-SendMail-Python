import logging
import azure.functions as func
from smtplib import SMTPException
import smtplib
import os


def main(req: func.HttpRequest) -> func.HttpResponse:
    emailSender = os.environ.get("EMAILSENDER")
    emailReceivers = os.environ.get("EMAILRECEIVERS")
    passwordEmail = os.environ.get("PASSWORD_EMAIL")
    smtpProvider = os.environ.get("SMTP_PROVIDER")
    smtpPort = os.environ.get("SMPT_PORT")

    sender = emailSender
    receivers = [emailReceivers]

    message = req.params.get('message')

    try:
        server = smtplib.SMTP_SSL(smtpProvider, smtpPort)
        server.login(emailSender, passwordEmail)
        server.sendmail(sender, receivers, message)
        logging.info("Successfully sent email")
        server.quit()
        return func.HttpResponse(
            "Email enviado com sucesso",
            status_code=200
        )
    except SMTPException:
        return func.HttpResponse(
            "Error: unable to send email",
            status_code=200
        )
        logging.info("Error: unable to send email")