from django.db import models
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Create your models here.
class Score(models.Model):
    result = models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)
    
    def save(self,*args,**kwargs):
        if self.result < 70:
            account_sid = 'Account_sid_from_twilio'
            auth_token = 'auth_token_id_from_twilio'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                                        body=f'You result is not so good, result - {self.result}',
                                        from_='verified_ph_no_of_twilio',
                                        to='verified_ph_No'
                                    )

            print(message.sid)
        return super().save(*args, **kwargs)