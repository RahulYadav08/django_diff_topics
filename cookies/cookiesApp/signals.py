from django.db.models.signals import (pre_save, post_save, pre_delete, post_delete)
from django.dispatch import receiver

from django.contrib.auth.models import User

@receiver(pre_save, sender=User, dispatch_uid = "my unique identifier1")
def pre_save_signal_receiver(**kwargs):
    print("Pre save signal received")
    print(kwargs)