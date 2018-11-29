from django.shortcuts import  redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import AddressForm
from billing.models import BillingProfile


class CheckoutAddressView(FormView):
    form_class = AddressForm
    # success_url = reverse_lazy('cart:checkout')
    template_name = 'accounts/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        context = {'form': form}
        next_url = request.build_absolute_uri
        if form.is_valid():
            print(request.POST)
            instance = form.save(commit=False)
            billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
            print("Bill ----> " + str(billing_profile.email))

            if billing_profile is not None:
                # print("Req --> "+request.POST.get('address_type'))
                address_type = request.POST.get('address_type')
                instance.billing_profile = billing_profile
                instance.address_type = address_type
                instance.save()

                request.session[address_type + "_address_id"] = instance.id
                billing_address_id = request.session.get("billing_address_id", None)
                shipping_address_id = request.session.get("shipping_address_id", None)
                # return redirect(next_url)
            else :
                print('Error page..')
                return redirect('cart:checkout')
        return redirect('cart:checkout')
