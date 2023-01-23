from celery import shared_task
from django.core.mail import send_mail
from decouple import config
from django.utils.crypto import get_random_string
from .models import CodeLink


@shared_task
def send_activation_code(email, activation_code):
    activation_link = f'http://{config("SERVER_CONFIG")}/account/activate/{activation_code}/'
    message = f'Активируйте аккаунт перейдя по ссылке {activation_link}\nВнимание! для регистрации с вашего баланса будет вычето 10$'
    send_mail('Activate account', message, 'admin@admin.com', [email])
    return 'Send'

@shared_task
def update_balance(email, balance, amount, activation_code):
    activation_link = f'http://{config("SERVER_CONFIG")}/account/payment/{activation_code}/{amount}/'
    message = f'Подтвердите пополнение баланса на сумму {amount}$, Ваш текущий баланс = {balance}$, \nДля подтверждения оплаты перейдите по ссылке {activation_link}'
    send_mail('Confirm payment', message, 'admin@admin.com', [email])
    return 'Send'

@shared_task
def password_recovery(email, activation_code, new_password):
    activation_link = f'http://{config("SERVER_CONFIG")}/account/forgot_password_confirm/{activation_code}/{new_password}'
    message = f'Ваш пароль был сброшен. Ваш новый пароль: {new_password}, \nДля подтверждения сброса перейдите по ссылке: {activation_link}'
    send_mail('Confirm password recovery', message, 'admin@admin.com', [email])
    return 'Send'

@shared_task
def get_string_time():
    code = get_random_string(10,'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890')
    CodeLink.objects.create(code=code)
    delete_string.apply_async(args=[code], countdown=60*30)
    return code

@shared_task
def delete_string(code):
    CodeLink.objects.filter(code=code).delete()