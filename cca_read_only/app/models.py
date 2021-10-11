from django.db import models

class WebsiteUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'website_user'

    def __str__(self):
        return self.name
