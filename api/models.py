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
    
class Day(models.Model):
    owner = models.ForeignKey('auth.User', related_name='days', on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    weather = models.CharField(max_length=5000, default="")
    bool1 = models.BooleanField(default=True)
    int1 = models.IntegerField(default=False)
    char1 = models.CharField(max_length=5000)
    char2 = models.CharField(max_length=5000)
    char3 = models.CharField(max_length=5000)
    int1 = models.IntegerField(default=1)
    int2 = models.IntegerField(default=0)
    int3 = models.IntegerField(default=0)
    int4 = models.IntegerField(default=0)
    int5 = models.IntegerField(default=0)
    int6 = models.IntegerField(default=0)
    bool1 = models.BooleanField(default=False)
    bool2 = models.BooleanField(default=False)
    bool3 = models.BooleanField(default=False)
    bool4 = models.BooleanField(default=False)
    bool5 = models.BooleanField(default=False)
    bool6 = models.BooleanField(default=False)
    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return self.name

class Daily(models.Model):
    day = models.ForeignKey('auth.User', related_name='dailys', on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    text = models.CharField(max_length=5000)
    order = models.IntegerField(default=1)
    show = models.BooleanField(default=False)
    char1 = models.CharField(max_length=5000)
    char2 = models.CharField(max_length=5000)
    char3 = models.CharField(max_length=5000)
    int1 = models.IntegerField(default=1)
    int2 = models.IntegerField(default=0)
    int3 = models.IntegerField(default=0)
    int4 = models.IntegerField(default=0)
    int5 = models.IntegerField(default=0)
    int6 = models.IntegerField(default=0)
    bool1 = models.BooleanField(default=False)
    bool2 = models.BooleanField(default=False)
    bool3 = models.BooleanField(default=False)
    bool4 = models.BooleanField(default=False)
    bool5 = models.BooleanField(default=False)
    bool6 = models.BooleanField(default=False)
    class Meta:
        ordering = ['order']
    def __str__(self):
        return self.text
    
class Day_1(models.Model):
    owner = models.ForeignKey('auth.User', related_name='days_1', on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    weather = models.CharField(max_length=5000, default="")
    bool1 = models.BooleanField(default=True)
    int1 = models.IntegerField(default=False)
    char1 = models.CharField(max_length=5000)
    char2 = models.CharField(max_length=5000)
    char3 = models.CharField(max_length=5000)
    int1 = models.IntegerField(default=1)
    int2 = models.IntegerField(default=0)
    int3 = models.IntegerField(default=0)
    int4 = models.IntegerField(default=0)
    int5 = models.IntegerField(default=0)
    int6 = models.IntegerField(default=0)
    bool1 = models.BooleanField(default=False)
    bool2 = models.BooleanField(default=False)
    bool3 = models.BooleanField(default=False)
    bool4 = models.BooleanField(default=False)
    bool5 = models.BooleanField(default=False)
    bool6 = models.BooleanField(default=False)
    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return self.name

class Daily_1(models.Model):
    day = models.ForeignKey(Day_1, related_name='dailys_1', on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    text = models.CharField(max_length=5000)
    order = models.IntegerField(default=1)
    show = models.BooleanField(default=False)
    char1 = models.CharField(max_length=5000)
    char2 = models.CharField(max_length=5000)
    char3 = models.CharField(max_length=5000)
    int1 = models.IntegerField(default=1)
    int2 = models.IntegerField(default=0)
    int3 = models.IntegerField(default=0)
    int4 = models.IntegerField(default=0)
    int5 = models.IntegerField(default=0)
    int6 = models.IntegerField(default=0)
    bool1 = models.BooleanField(default=False)
    bool2 = models.BooleanField(default=False)
    bool3 = models.BooleanField(default=False)
    bool4 = models.BooleanField(default=False)
    bool5 = models.BooleanField(default=False)
    bool6 = models.BooleanField(default=False)
    class Meta:
        ordering = ['order']
    def __str__(self):
        return self.text
    
class Mindset(models.Model):
    owner = models.ForeignKey('auth.User', related_name='mindsets', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, unique=True)
    order = models.IntegerField(default=1)
    image = models.CharField(max_length=5000, default="")
    char1 = models.CharField(max_length=5000)
    char2 = models.CharField(max_length=5000)
    char3 = models.CharField(max_length=5000)
    int1 = models.IntegerField(default=1)
    int2 = models.IntegerField(default=0)
    int3 = models.IntegerField(default=0)
    int4 = models.IntegerField(default=0)
    int5 = models.IntegerField(default=0)
    int6 = models.IntegerField(default=0)
    bool1 = models.BooleanField(default=False)
    bool2 = models.BooleanField(default=False)
    bool3 = models.BooleanField(default=False)
    bool4 = models.BooleanField(default=False)
    bool5 = models.BooleanField(default=False)
    bool6 = models.BooleanField(default=False)
    class Meta:
        ordering = ['order']
    def __str__(self):
        return self.name

class Thot(models.Model):
    mindset = models.ForeignKey(Mindset, related_name='thots', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=5000)
    order = models.IntegerField(default=1)
    show = models.BooleanField(default=True)
    char1 = models.CharField(max_length=5000)
    char2 = models.CharField(max_length=5000)
    char3 = models.CharField(max_length=5000)
    int1 = models.IntegerField(default=1)
    int2 = models.IntegerField(default=0)
    int3 = models.IntegerField(default=0)
    int4 = models.IntegerField(default=0)
    int5 = models.IntegerField(default=0)
    int6 = models.IntegerField(default=0)
    bool1 = models.BooleanField(default=False)
    bool2 = models.BooleanField(default=False)
    bool3 = models.BooleanField(default=False)
    bool4 = models.BooleanField(default=False)
    bool5 = models.BooleanField(default=False)
    bool6 = models.BooleanField(default=False)
    class Meta:
        ordering = ['order']
    def __str__(self):
        return self.text