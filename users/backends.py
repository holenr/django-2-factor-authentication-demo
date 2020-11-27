from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from users.models import Customer

class CustomerBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        customer_id = kwargs['username']
        password = kwargs['password']
        try:
            customer = Customer.objects.get(customer_id=customer_id)
            if customer.user.check_password(password) is True:
                # here normal django authentication should have succeeded.
                # TODO: add TWILIO SMS Authentication here?
                # ...
                # begin edits Roland:
                phone_number = customer.phone_number
                print(phone_number) # works!
                # ...
                # end edits Roland.
                return customer.user
        except Customer.DoesNotExist:
            pass
