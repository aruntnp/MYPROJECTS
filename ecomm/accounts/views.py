from django.shortcuts import render, redirect
from django.views.generic.edit import FormView

from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views import View
from .forms import GuestForm
from .models import GuestEmail
from django.utils.http import is_safe_url


# Create your views here.


class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/register.html'


class GuestLoginView(FormView):
    form_class = GuestForm
    template_name =  reverse_lazy('guest_login')
    success_url = reverse_lazy('cart:checkout')

    # def form_valid(self, form, **kwargs):
    #     guest_email = form.cleaned_data.get('email')  # This is coming from client side.
    #     new_guest_email = GuestEmail.objects.create(email=guest_email)  # This will create a new email in db and store objects in variable.
    #     request = kwargs['request']
    #     request.session['guest_email_id'] = new_guest_email.id
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form
    #     return super().form_valid(form)
    #
    # # def form_invalid(self, form, **kwargs):
    # #     context = self.get_context_data(**kwargs)
    # #     context['form'] = form
    # #     return self.render_to_response(context)
    #
    #
    # def get(self, request, *args, **kwargs):
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form
    #     return self.render_to_response(context)
    #
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         kwargs = {'request':request}
    #         return self.form_valid(form, **kwargs)
    #     else:
    #         return self.form_invalid(form, **kwargs)

