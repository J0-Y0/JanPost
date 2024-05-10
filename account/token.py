from django.contrib.auth.tokens import PasswordResetTokenGenerator  
from django.contrib.auth.hashers import make_password
class ActivationTokenGenerator(PasswordResetTokenGenerator):  
    def _make_hash_value(self, user, timestamp):  
        return (  
            str(user.pk) + str(timestamp) +  
            str(user.is_active)  
        )  
class ResetTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        hashed_password = make_password(user.password)
        return (
            str(user.pk) + str(timestamp) +
            str(user.is_active) + hashed_password
        )
account_activation_token = ActivationTokenGenerator()  
reset_token_generator = ResetTokenGenerator()