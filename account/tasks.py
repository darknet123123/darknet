from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_activation_code(email, activation_code):
    activation_link = f'http://localhost:8000/account/activate/{activation_code}'
    message = f'Активируйте аккаунт перейдя по ссылке {activation_link}'
    send_mail('Activate account', message, 'admin@gmail.com', [email])
    return 'Отправлено'

@shared_task
def password_confirm(email, activation_code):
    activation_url = f'http://127.0.0.1:8000/user_account/password_confirm/{activation_code}'
    message = f"""
    Do you want to change password?
    Confirm password changes: {activation_url}
    """
    send_mail("Please confirm your new changes", message, "admin@gmail.com", [email,])
    return 'Отправлено'