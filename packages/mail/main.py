from flask import Flask
from packages.mail.routes.email import router as email_router

app = Flask(__name__)

app.register_blueprint(email_router, url_prefix="/email")
