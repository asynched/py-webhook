import requests


def send_email_request(email: str):
    """Background task to send an e-mail to a newly registered user

    Args:
        email (str): User's e-mail
    """

    URL = 'http://localhost:5518'

    response = requests.get(
        f'{URL}/email/{email}',
        headers={
            'Authorization': 'secret_key',
        },
    )

    if response.status_code == 200:
        print('[TASKS]: Registration e-mail has been sent')
    else:
        print(
            '[TASKS]: Registration e-mail hasn\'t been send'
            + f'Response status code: {response.status_code}'
        )
