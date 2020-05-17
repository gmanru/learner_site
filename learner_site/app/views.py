from datetime import datetime
import django_rq
from django.views.generic import FormView
from .forms import ContactForm
from .tasks import send_message_job, send_push_admin_job, send_push_user_job


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'app/index.html'
    success_url = '/'

    def form_valid(self, form):
        form_data = form.cleaned_data
        message = form_data['message']
        email = form_data['email']
        scheduler = django_rq.get_scheduler('default')
        scheduler.enqueue_at(datetime.utcnow(), func=send_message_job, message=message, email=email)
        scheduler.enqueue_at(datetime.utcnow(), func=send_push_admin_job, email=email)
        scheduler.enqueue_at(datetime.utcnow(), func=send_push_user_job, email=[email])
        return super().form_valid(form)
