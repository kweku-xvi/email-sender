from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import EmailSender

def email(request):
    if request.method == 'POST':
        form = EmailSender(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            email_from = form.cleaned_data['sender_mail']
            recipient = form.cleaned_data['recipient_mail']
            recipient_list = [recipient]
            message = form.cleaned_data['message']

            send_mail(subject, message, email_from, recipient_list)

            return redirect('complete')
    else:
        form = EmailSender()
    return render(request, 'main/home.html', {'form':form})


def complete(request):
    return render(request, 'main/complete.html')
