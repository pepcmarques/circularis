from django.db import models

from circularis.accounts.models import User


class MessageOneOne(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.DO_NOTHING)
    receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=30, blank=False)
    content = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.subject

    def to_str(self):
        return f"{self.subject}"

    class Meta:
        ordering = ['created_at']
