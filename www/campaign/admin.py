from django.contrib import admin
from .models import Organizer, Fundraiser, Update, Comment, Contribution

# Register your models here.
admin.site.register(Organizer)
admin.site.register(Fundraiser)
admin.site.register(Update)
admin.site.register(Comment)
admin.site.register(Contribution)
