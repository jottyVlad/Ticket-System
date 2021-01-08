from django.contrib.auth.models import User
from django.db import models


class Ticket(models.Model):

    class TicketStatus(models.TextChoices):
        PENDING = "PD", "Pending"
        HAVE_ANSWER = "HA", "Have answer"
        CLOSED = "CD", "Closed"

    title = models.CharField(max_length=256)
    text = models.TextField()
    files = models.FileField(upload_to='ticket_files', null=True, blank=True)
    status = models.CharField(
        max_length=2,
        choices=TicketStatus.choices,
        default=TicketStatus.PENDING
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

