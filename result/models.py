from django.db import models

class User(models.Model):
    Rollnumber = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    U_E_Marks = models.CharField(max_length=100, default='')
    IA_CA = models.CharField(max_length=100, default='')
    Total_Marks = models.CharField(max_length=100, default='')
    Grade = models.CharField(max_length=100, default='')  # Add default value as an empty string
    Total_Marks = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.Rollnumber

    class Meta:
        app_label = 'result'
