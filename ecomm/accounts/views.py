from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate

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
    template_name = 'carts/checkout.html'
    success_url = 'carts/checkout.html'

    # def form_valid(self, form):
    #     guest_email = form.cleaned_data.get('email')  # This is coming from client side.
    #     new_guest_email = GuestEmail.objects.create(
    #         email=guest_email)  # This will create a new email in db and store objects in variable.
    #     # request.session['guest_email_id'] = new_guest_email.id
    #     return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        context = {'form': form}
        if form.is_valid():
            guest_email = form.cleaned_data.get('email')  # This is coming from client side.
            new_guest_email = GuestEmail.objects.create(
                email=guest_email)  # This will create a new email in db and store objects in variable.
            request.session['guest_email_id'] = new_guest_email.id
            return redirect('cart:checkout')

        return redirect('cart:checkout')


class MyLoginView(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        # print('--------------- MY FORM_VALID CALLED-----------')
        try:
            del self.request.session['guest_email_id']
            # print('*********************** DELETED GUEST EMAIL ******************')
        except:
            # print('*********************** NOT DELETED GUEST EMAIL ******************')
            pass

        return super(MyLoginView, self).form_valid(form)
