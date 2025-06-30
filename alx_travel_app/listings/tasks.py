from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_confirmation_email_task(user_email, booking_id, username):
    subject = "Booking Confirmed!"
    message = f"Hey {username}, your booking #{booking_id} is confirmed! 🎉"
    from_email = "no-reply@"
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list)
