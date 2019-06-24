from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import get_template
from saunterer.forms import ContactForm
from .models import BookingForm, Preferences
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.mail import send_mail, BadHeaderError              # For sending emails    

def index(request):
    return render(request, 'saunterer/index.html', context = None)

def about(request):
    return render(request, 'saunterer/about.html', context = None)

def offer(request):
    return render(request, 'saunterer/offer.html', context = None)

def galary(request):
    return render(request, 'saunterer/gallery.html', context = None)


class TourForm(CreateView):
    model = BookingForm
    fields = ['first_name', 'last_name', 'email_address', 'contact_number']


class PreferenceForm(CreateView):
    model = Preferences
    fields = ['entry_1', 'entry_2', 'entry_3', 'entry_4', 'entry_5']



def contact(request):
    form_class = ContactForm
    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('saunterer/contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['arj.kashyap123@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('saunterer/contact.html')

    return render(request, 'saunterer/contact.html', {
        'form': form_class,
    })
