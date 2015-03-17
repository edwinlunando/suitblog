from django.shortcuts import render

from .forms import ContactForm

def contact(request):
    form = ContactForm(request.POST or None)
    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)
