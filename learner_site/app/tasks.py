from django.core.mail import send_mail
from django_rq import job


@job
def send_message_job(message, email):
    send_mail('Text message', message, email, ['admin@localhost'], False)


@job
def send_push_admin_job(email):
    send_mail('Got new message', 'Получено новое сообщение', email,
              ['admin@localhost'], False)


@job
def send_push_user_job(email):
    send_mail('Notification', 'Уважаемый подписчик! Мы приняли Ваше письмо, на данный момент оно находится в обработке', 'admin@localhost', (email, ), False)
