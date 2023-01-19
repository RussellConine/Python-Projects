from django.db import models

# Create your models here.
class UniversityCampus(models.Model):
    # create campus_name and state as fields
    # id primary key will be created by default
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)

    object = models.Manager()

    def __str__(self):
        # returns the campus name as the value in the browser
        return self.campus_name


    # display "University Campus" in the browser
    class Meta:
        verbose_name_plural = "University Campus"