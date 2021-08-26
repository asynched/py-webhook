import requests


def send_registration_request():
    requests.post(
        "http://localhost:5517/auth/register",
        json={
            "name": "Eder Lima",
            "email": "eder@mail.com",
            "password": "senha123",
        },
    )


if __name__ == "__main__":
    send_registration_request()
