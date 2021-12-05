import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_mail_processed_file(
        to_email: str,
        original_filename: str,
        new_format: str,
        processed_filename: str):
    message = Mail(
        from_email='equipo11cloud@gmail.com',
        to_emails=to_email,
        subject='Audio file processed and available',
        html_content=f'The file <strong>{original_filename}</strong> was converted to format <strong>{new_format}</strong> and is available with the name <strong>{processed_filename}</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
    except Exception as e:
        print(str(e))
