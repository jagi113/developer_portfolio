from django.contrib.auth.models import User
from users.models import Profile

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=(f'{user.first_name} {user.last_name}')
        )
        
        subject = 'Welcome to DevSearch'
        message = 'We are glad you signed up!'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )


@receiver(post_save, sender=Profile)
def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name.split()[0]
        user.last_name = profile.name.split()[-1]
        user.username = profile.username
        user.email = profile.email
        user.save()


@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, ** kwargs):
    try:
        deleteduser = instance.user
        deleteduser.delete()
    except: 
        print("This user has been deleted.")
