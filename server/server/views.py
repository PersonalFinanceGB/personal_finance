from django.views.generic import TemplateView


class RegistrationView(TemplateView):
    template_name = 'registration.html'


class HomePage(TemplateView):
    template_name = 'index.html'