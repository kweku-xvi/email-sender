from django import forms

class EmailSender(forms.Form):
    sender_mail = forms.EmailField(label="Sender's Email")
    recipient_mail = forms.EmailField(label="Recipient's Email")
    subject = forms.CharField(max_length=1000)
    message = forms.CharField(widget=forms.Textarea)