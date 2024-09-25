from django.db.models.signals import (pre_save, post_save, pre_delete, post_delete,
    pre_init, post_init,
    pre_migrate, post_migrate,
    class_prepared)

from .models import Student
from django.dispatch import receiver

import smtplib

#Signals need to be registered in apps.py
@receiver(post_save, sender = Student)
def post_save_signal_receiver(sender, instance, created, *args, **kwargs):
    print("Post save signal received")
    if created:
        # # starting smtp session
        # s = smtplib.SMTP('smtp.gmail.com', 587)
        # #start tls for security
        # s.starttls()
        # #sender login
        # s.login("sender email id", "sender email pass")
        # #message to be sent
        # message = "New student added"
        # #sending mail
        # s.sendmail("sender email id", "receiver email id", message)
        # #session termination
        # s.quit()

        print("New student saved")

@receiver(pre_save, sender= Student)
def pre_save_signal_receiver(sender, instance,*args, **kwargs):
    print("Pre save signal received")
    print(kwargs)