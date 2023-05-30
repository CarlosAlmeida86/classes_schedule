from django.db import models

# Create your models here.
class Classes(models.Model):
    scheduled_date = models.DateTimeField("Data do agendamento")
    issue = models.CharField(max_length=200)
    is_checked = models.BooleanField()

    def __str__(self):
        return self.scheduled_date.__str__()
