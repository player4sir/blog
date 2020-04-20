from django.views import generic
from . forms import CustomUserCreateForm
from django.urls import reverse_lazy
from .models import CustomUser


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreateForm
    success_url = reverse_lazy('account_login')
    model = CustomUser
    template_name = 'signup.html'
