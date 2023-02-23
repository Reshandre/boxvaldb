from django.db import models
from partners.models import BusinessPartner
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    RelatedToBusinesspartner = models.OneToOneField(BusinessPartner,  on_delete=models.CASCADE,null=True)
    avatar = models.ImageField(default='avatar.png', upload_to='avatars',blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" profile {self.user.username} "
