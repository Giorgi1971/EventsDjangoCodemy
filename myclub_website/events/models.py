from django.db import models


class Venue(models.Model):
    name =      models.CharField('Venue Name', max_length=120)
    address =   models.CharField(max_length=220)
    zip_code =  models.CharField('Zip Code', max_length=15)
    phone =     models.CharField('Contact Phone', max_length=120)
    web =       models.URLField('Website Address')
    email_address = models.EmailField('Email Address')

    def __str__(self) -> str:
        return self.name

class MyClubUser(models.Model):
    first_name =    models.CharField(max_length=244)
    last_name =    models.CharField(max_length=244)
    Email =    models.EmailField('User Email')

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
    name =      models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField()
    # venue  =    models.CharField(max_length=120)
    venue  =    models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager =   models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)

    def __str__(self) -> str:
        return self.name