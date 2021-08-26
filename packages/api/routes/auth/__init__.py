from fastapi import APIRouter, BackgroundTasks
from packages.api.types import UserType
from packages.api.tasks.send_email import send_email_request
from packages.api.models.user import User

router = APIRouter()


@router.post("/register")
async def register(user: UserType, background_tasks: BackgroundTasks):
    """Endpoint to register a user in the API

    Args:
        user (User): User data in the request body
        background_tasks (BackgroundTasks): Background tasks queue to schedule a new task
    """

    # 'Registers' a user

    print(f"[REGISTRATION]: {user}")
    user_instance = User(name=user.name, email=user.email, password=user.password)
    user_instance.save()

    # Schedules the background task
    background_tasks.add_task(lambda: send_email_request(user.email))

    return {
        "message": "Successfully registered",
    }
