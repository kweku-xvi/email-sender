from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import EmailSender, EmailSenderCourier
from trycourier import Courier

# using courier 
def email(request):
    if request.method == 'POST':
        form = EmailSenderCourier(request.POST)

        if form.is_valid():
            recipient_email = form.cleaned_data['recipient_mail']
            message = form.cleaned_data['message']

            client = Courier(auth_token="pk_prod_P6KGDK2MFM44YHQYXE0TMXQE1BW0")

            resp = client.send_message(
                message={
                    "to": {
                    "email": recipient_email,
                    },
                    "template": "VVY5W4MWN840MHKGKJBCRRDXC18S",
                    "data": {
                    "message": message,
                    },
                }
            )

            return redirect('complete')
    else:
        form = EmailSenderCourier()

    return render(request, 'main/home_courier.html', {'form':form})


def complete(request):
    return render(request, 'main/complete.html')


# using SMTP
def email_smtp(request):
    if request.method == 'POST':
        form = EmailSender(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            email_from = form.cleaned_data['sender_mail']
            # email_from = settings.EMAIL_HOST_USER
            recipient = form.cleaned_data['recipient_mail']
            recipient_list = [recipient]
            message = form.cleaned_data['message']

            send_mail(subject, message, email_from, recipient_list)

            return redirect('complete')
    else:
        form = EmailSender()
    return render(request, 'main/home_smtp.html', {'form':form})