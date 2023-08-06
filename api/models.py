from django.db import models
 
# Create your models here.
class Reminder(models.Model):
    owner = models.ForeignKey('auth.User', related_name='reminders', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=1)
    dashboard = models.BooleanField(default=False)
    recurring = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    text = models.CharField(max_length=5000)
    date = models.DateField()
    char1 = models.CharField(max_length=5000)
    char2 = models.CharField(max_length=5000)
    char3 = models.CharField(max_length=5000)
    int1 = models.IntegerField(default=1)
    int2 = models.IntegerField(default=2)
    int3 = models.IntegerField(default=3)
    bool1 = models.BooleanField(default=False)
    bool2 = models.BooleanField(default=False)
    bool3 = models.BooleanField(default=False)
    bool4 = models.BooleanField(default=False)
    bool5 = models.BooleanField(default=False)
    bool6 = models.BooleanField(default=False)
    bool7 = models.BooleanField(default=False)
    bool8 = models.BooleanField(default=False)
    bool9 = models.BooleanField(default=False)
    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text
    