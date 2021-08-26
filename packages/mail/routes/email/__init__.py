from flask import Blueprint
from packages.mail.lib.decorators import auth_required

router = Blueprint("email", __name__)


@router.get("/<email>")
@auth_required
def send_email(email: str):
    print(f"[EMAIL]: SENDING AN E-MAIL TO: {email}")

    return {
        "message": "E-mail has been sent",
    }, 200
