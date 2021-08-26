from fastapi import FastAPI, BackgroundTasks
from packages.api.types import User
from packages.api.tasks.send_email import send_email_request

app = FastAPI()


@app.post('/register')
async def register(user: User, background_tasks: BackgroundTasks):
    """Endpoint to register a user in the API

    Args:
        user (User): User data in the request body
        background_tasks (BackgroundTasks): Background tasks queue to schedule a new task
    """

    # 'Registers' a user
    print(f'[REGISTRATION]: {user}')

    # Schedules the background task
    background_tasks.add_task(lambda: send_email_request(user.email))

    return {
        'message': 'Successfully registered',
    }
