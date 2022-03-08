from django.db import models
from django.urls import reverse
import uuid
from datetime import datetime


# fundraiser campaign model
class Organizer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} <{self.email}>'


class Fundraiser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organizer = models.ForeignKey(Organizer, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    created_datetime = models.DateTimeField(default=datetime.now, blank=True)
    modified_datetime = models.DateTimeField
    about = models.TextField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('fundraiser-detail', args=[str(self.id)])


class Update(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fundraiser = models.ForeignKey(Fundraiser, on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(default=datetime.now, blank=True)
    update = models.TextField()

    def __str__(self):
        return self.update

    def get_absolute_url(self):
        return reverse('update-detail', args=[str(self.id)])


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fundraiser = models.ForeignKey(Fundraiser, on_delete=models.CASCADE)
    comment = models.TextField()
    created_datetime = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('comment-detail', args=[str(self.id)])


class Contribution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fundraiser = models.ForeignKey(Fundraiser, on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(default=datetime.now, blank=True)
    amount = models.DecimalField(max_digits=16, decimal_places=12)
    type = models.CharField(max_length=16)
    message = models.TextField(blank=True)

    def __str__(self):
        return f'{self.fundraiser.title}: {self.amount} {self.type}'

    def get_absolute_url(self):
        return reverse('contribution-detail', args=[str(self.id)])
