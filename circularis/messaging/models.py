from django.db import models
from django.utils.translation import gettext_lazy as _

from circularis.accounts.models import User
from circularis.books.models import Book


class MessageTypeManager(models.Manager):

    def populate(self, recreate=False):
        book_status = [('RQ', 'Request'),
                       ('RJ', 'Reject'),
                       ('AC', 'Accept')]

        if recreate:
            self.all().delete()
        else:
            if self.all():
                print(f"There is data in {self.model.__name__}. Nothing to do.")
                return False

        for b_status in book_status:
            code, status = b_status
            self.create(code=code, status=status)
            print(f"Populating {self.model.__name__} model with: {code}, {status}")

        return True


class MessageType(models.Model):
    class MessageTypeOptions(models.TextChoices):
        RQ = 'RQ', _('Request')
        RJ = 'RJ', _('Reject')
        AC = 'AC', _('Accept')

    code = models.CharField(max_length=2, unique=True, choices=MessageTypeOptions.choices,
                            default=MessageTypeOptions.RQ)
    status = models.CharField(max_length=25)

    objects = MessageTypeManager()

    def __str__(self):
        return self.status

    class Meta:
        ordering = ['status']
        verbose_name_plural = 'bookstatus'


class MessageOneOne(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.DO_NOTHING)
    receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.DO_NOTHING)
    book = models.ForeignKey(Book, related_name="book", on_delete=models.DO_NOTHING)
    msg_type = models.ForeignKey(MessageType, related_name="msg_type", on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=30, blank=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    def to_str(self):
        return f"{self.subject}"

    class Meta:
        ordering = ['created_at']
