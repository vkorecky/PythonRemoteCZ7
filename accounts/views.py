from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(CreateView):
    template_name = "accounts/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
