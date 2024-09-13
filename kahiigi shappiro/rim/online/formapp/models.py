from django.db import models


class PassengerInformation(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('NB', 'Non-binary'),
        ('Q', 'Genderqueer'),
        ('O', 'Other'),
        ('P', 'Prefer not to say'),
    )

    fullname = models.CharField(max_length=50)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=50)
    email_address = models.EmailField(null=True, blank=True)
    po_box_number = models.IntegerField(default=0)
    emergency_phone_number = models.CharField(max_length=10)
    passport_number = models.CharField(max_length=50)
    visa_documents = models.FileField(upload_to='uploads/', null=True)
    departure_city = models.CharField(max_length=50, blank=True)
    destination_city = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.fullname