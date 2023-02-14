from django.contrib.auth.models import User
from users.models import Profile

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile.objects.create(
            user=user,
            username = user.username,
            email=user.email,
            name=(f'{user.first_name} {user.last_name}')
        )
    else:
        print(user.username)
        profile = Profile.objects.get(user=user)
        profile.username = user.username
        profile.email= user.email
        profile.name=f'{user.first_name} {user.last_name}'
        profile.save()
        

@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, ** kwargs):
    deleteduser = instance.user
    deleteduser.delete()