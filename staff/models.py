from django.db import models

class Staff(models.Model):
    ADMIN = 'AD'
    EDITOR = 'ED'
    STAFF = 'ST'
    WRITER = 'WR'

    ROLE_CHOICES = {
        ADMIN: 'Admin',
        EDITOR: 'Editor',
        STAFF: 'Staff',
        WRITER: 'Writer',
    }

    name = models.CharField(max_length=255)
    birthday = models.DateField()
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default=STAFF)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

