from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_activation_code(email, activation_code):
    activation_link = f'http://127.0.0.1:8000/account/activate/{activation_code}'
    message = f'Активируйте аккаунт перейдя по ссылке {activation_link}'
    send_mail('Activate account', message, 'admin@admin.com', [email])
    return 'Send'

@shared_task
def update_balance(email, balance, amount, activation_code):
    activation_link = f'http://127.0.0.1:8000/account/payment/{activation_code}/{amount}/'
    message = f'Подтвердите пополнение баланса на сумму {amount}$, Ваш текущий баланс = {balance}$, \nДля подтверждения оплаты перейдите по ссылке {activation_link}'
    send_mail('Confirm payment', message, 'admin@admin.com', [email])
    return 'Send'