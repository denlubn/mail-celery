from django.views import generic

from .forms import ContactForm
from .models import Contact
from.tasks import send_spam_email


class ContactView(generic.CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        send_spam_email.delay(form.instance.email)
        return super().form_valid(form)
