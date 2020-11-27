from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from users.models import Customer

# From Verify API Documentation:
from twilio.rest import Client # new

# Roland's Twilio Account Details to use Twilio services: (send sms, emails, voicecall etc.)
TWILIO_ACCOUNT_SID = 'AC313e28cfd8f0ef11c59b56184b91dccc' #required
TWILIO_AUTH_TOKEN = '532f80cfeb39a76c1bac46117376aa5b'    #required

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
                print(phone_number) # debugging, works!
                # ...
                # end edits Roland.
                return customer.user
        except Customer.DoesNotExist:
            pass
