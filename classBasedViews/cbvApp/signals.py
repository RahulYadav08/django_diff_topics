from django.db.models.signals import (pre_save, post_save, pre_delete, post_delete,
                                      pre_init, post_init, pre_migrate, post_migrate)

from django.dispatch import receiver

from django.contrib.auth.models import User

@receiver(pre_save, sender=User)
def pre_save_signal_receiver(**kwargs):
    print("User pre save signal received")
    print(kwargs)

@receiver(post_save, sender = User)
def post_save_signal_receiver(**kwargs):
    print("User post save signal received")
    print(kwargs)

@receiver(pre_delete, sender = User)
def post_save_signal_receiver(**kwargs):
    print("User pre delete signal received")
    print(kwargs)

@receiver(post_delete, sender = User)
def post_save_signal_receiver(**kwargs):
    print("User post delete signal received")
    print(kwargs)