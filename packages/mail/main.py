from flask import Flask
from packages.mail.decorators import auth_required

app = Flask(__name__)


@app.get('/email/<email>')
@auth_required
def send_email(email: str):
    print(f'[EMAIL]: SENDING AN E-MAIL TO: {email}')

    return {
        'message': 'E-mail has been sent',
    }, 200
