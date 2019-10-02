from .models import Task
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


@receiver(post_save, sender=Task)
def announce_new_task(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notification", {"type": "task.notification",
                       "event": "New Task",
                       'pk':instance.assigned_to.pk})
