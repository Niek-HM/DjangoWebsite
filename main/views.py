from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .forms import contactForm

def homeView(request):
    context = {}
    return render(request, 'main/home.html', context)

def contactView(request):
    if request.method == 'POST':
        form = contactForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user_email = form.cleaned_data['user_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail(subject, 'New message from {} {} ({}):\n{}'.format(first_name, last_name, user_email, message), 'weggoiemail@gmail.com', ['niek@meijlink5.nl'])
            send_mail('Conformation email ({})'.format(subject), 'Conformation email: `{}`'.format(subject, message), 'weggoiemail@gmail.com', [user_email])

            messages.success(request, 'A confirmation email has been send.')
        else: messages.success(request, 'Please check if all or your information is valid.')
        
    else: 
        form = contactForm()

    context = {'form': form}
    return render(request, 'main/contact.html', context)
