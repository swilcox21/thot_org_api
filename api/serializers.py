from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Reminder, Day, Daily, Mindset, Thot


class ReminderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    text = serializers.CharField(required=False, allow_blank=True, max_length=5000, trim_whitespace=False)
    char1 = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    char2 = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    char3 = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    class Meta:
        model = Reminder
        fields = ['text','id','owner','recurring','completed','order','char1','char2','char3','int1','int2','int3','bool1','bool2','bool3','bool4','bool5','bool5','bool6','bool7','bool8','bool9']
    def update(self, instance, validated_data):
        instance.order = validated_data.get('order', instance.order)
        instance.recurring = validated_data.get('recurring', instance.recurring)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.text = validated_data.get('text', instance.text)
        instance.char1 = validated_data.get('char1', instance.char1)
        instance.char2 = validated_data.get('char2', instance.char2)
        instance.char3 = validated_data.get('char3', instance.char3)
        instance.int1 = validated_data.get('int1', instance.int1)
        instance.int2 = validated_data.get('int2', instance.int2)
        instance.int3 = validated_data.get('int3', instance.int3)
        instance.bool1 = validated_data.get('bool1', instance.bool1)
        instance.bool2 = validated_data.get('bool2', instance.bool2)
        instance.bool3 = validated_data.get('bool3', instance.bool3)
        instance.bool4 = validated_data.get('bool4', instance.bool4)
        instance.bool5 = validated_data.get('bool5', instance.bool5)
        instance.bool6 = validated_data.get('bool6', instance.bool6)
        instance.bool7 = validated_data.get('bool7', instance.bool7)
        instance.bool8 = validated_data.get('bool8', instance.bool8)
        instance.bool9 = validated_data.get('bool9', instance.bool9)
        instance.save()
        return instance
    def create(self, validated_data):
        order = len(Reminder.objects.all())
        print("REMINDER:", order)
        return Reminder.objects.create(order=order + 1, **validated_data)

class _DaySerializer(serializers.ModelSerializer): 
    owner = serializers.ReadOnlyField(source='owner.username')
    name = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    class Meta:                                 
        model = Day
        fields = ['name','id','owner']
class _DailySerializer(serializers.ModelSerializer): 
    class Meta:                                 
        model = Daily
        fields = ['text','id','show','order']

class DailySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    day = _DaySerializer(required=False)
    date = serializers.DateField(read_only=False)
    text = serializers.CharField(required=False, allow_blank=True, max_length=5000, trim_whitespace=False)
    char1 = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    char2 = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    char3 = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    class Meta:
        model = Reminder
        fields = ['date','text','id','owner','recurring','completed','order','char1','char2','char3','int1','int2','int3','int4','int5','int6','bool1','bool2','bool3','bool4','bool5','bool5','bool6']
    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.order = validated_data.get('order', instance.order)
        instance.recurring = validated_data.get('recurring', instance.recurring)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.text = validated_data.get('text', instance.text)
        instance.char1 = validated_data.get('char1', instance.char1)
        instance.char2 = validated_data.get('char2', instance.char2)
        instance.char3 = validated_data.get('char3', instance.char3)
        instance.int1 = validated_data.get('int1', instance.int1)
        instance.int2 = validated_data.get('int2', instance.int2)
        instance.int3 = validated_data.get('int3', instance.int3)
        instance.int4 = validated_data.get('int4', instance.int4)
        instance.int5 = validated_data.get('int5', instance.int5)
        instance.int6 = validated_data.get('int6', instance.int6)
        instance.bool1 = validated_data.get('bool1', instance.bool1)
        instance.bool2 = validated_data.get('bool2', instance.bool2)
        instance.bool3 = validated_data.get('bool3', instance.bool3)
        instance.bool4 = validated_data.get('bool4', instance.bool4)
        instance.bool5 = validated_data.get('bool5', instance.bool5)
        instance.bool6 = validated_data.get('bool6', instance.bool6)
        instance.save()
        return instance
    def create(self, validated_data):
        order = len(Reminder.objects.all())
        print("REMINDER:", order)
        return Reminder.objects.create(order=order + 1, **validated_data)

class DaySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    name = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    weather = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    char1 = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    char2 = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    char3 = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    dailies = _DailySerializer(many=True, required=False)
    class Meta:
        model = Day
        fields = ['name','id','owner','order','image','thots','char1','char2','char3','int1','int2','int3','int4','int5','int6','bool1','bool2','bool3','bool4','bool5','bool5','bool6']
    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.name = validated_data.get('name', instance.name)
        instance.char1 = validated_data.get('char1', instance.char1)
        instance.char2 = validated_data.get('char2', instance.char2)
        instance.char3 = validated_data.get('char3', instance.char3)
        instance.int1 = validated_data.get('int1', instance.int1)
        instance.int2 = validated_data.get('int2', instance.int2)
        instance.int3 = validated_data.get('int3', instance.int3)
        instance.int4 = validated_data.get('int4', instance.int4)
        instance.int5 = validated_data.get('int5', instance.int5)
        instance.int6 = validated_data.get('int6', instance.int6)
        instance.bool1 = validated_data.get('bool1', instance.bool1)
        instance.bool2 = validated_data.get('bool2', instance.bool2)
        instance.bool3 = validated_data.get('bool3', instance.bool3)
        instance.bool4 = validated_data.get('bool4', instance.bool4)
        instance.bool5 = validated_data.get('bool5', instance.bool5)
        instance.bool6 = validated_data.get('bool6', instance.bool6)
        instance.save()
        return instance
    def create(self, validated_data):
        order = len(Mindset.objects.all())
        return Mindset.objects.create(order=order + 1,**validated_data)

class _MindsetSerializer(serializers.ModelSerializer): 
    owner = serializers.ReadOnlyField(source='owner.username')
    name = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    class Meta:                                 
        model = Mindset
        fields = ['name','id','owner']
class _ThotSerializer(serializers.ModelSerializer): 
    class Meta:                                 
        model = Thot
        fields = ['text','id','show','order']

class ThotSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    mindset = _MindsetSerializer(required=False)
    text = serializers.CharField(required=False, allow_blank=True, max_length=5000, trim_whitespace=False)
    char1 = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    char2 = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    char3 = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    class Meta:
        model = Thot
        fields = ['text','mindset','id','created_date','order','show','char1','char2','char3','int1','int2','int3','int4','int5','int6','bool1','bool2','bool3','bool4','bool5','bool5','bool6']   
    def update(self, instance, validated_data):
        instance.mindset = validated_data.get('mindset', instance.mindset)
        instance.text = validated_data.get('text', instance.text)
        instance.order = validated_data.get('order', instance.order)
        instance.show = validated_data.get('show', instance.show)
        instance.char1 = validated_data.get('char1', instance.char1)
        instance.char2 = validated_data.get('char2', instance.char2)
        instance.char3 = validated_data.get('char3', instance.char3)
        instance.int1 = validated_data.get('int1', instance.int1)
        instance.int2 = validated_data.get('int2', instance.int2)
        instance.int3 = validated_data.get('int3', instance.int3)
        instance.int4 = validated_data.get('int4', instance.int4)
        instance.int5 = validated_data.get('int5', instance.int5)
        instance.int6 = validated_data.get('int6', instance.int6)
        instance.bool1 = validated_data.get('bool1', instance.bool1)
        instance.bool2 = validated_data.get('bool2', instance.bool2)
        instance.bool3 = validated_data.get('bool3', instance.bool3)
        instance.bool4 = validated_data.get('bool4', instance.bool4)
        instance.bool5 = validated_data.get('bool5', instance.bool5)
        instance.bool6 = validated_data.get('bool6', instance.bool6)
        instance.save()
        return instance
    def create(self, validated_data):
        order = len(Thot.objects.filter(mindset=validated_data.get('mindset')))
        return Thot.objects.create(order=order + 1, **validated_data)

class MindsetSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    name = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    char1 = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    char2 = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    char3 = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    thots = _ThotSerializer(many=True, required=False)
    class Meta:
        model = Mindset
        fields = ['name','id','owner','order','image','thots','char1','char2','char3','int1','int2','int3','int4','int5','int6','bool1','bool2','bool3','bool4','bool5','bool5','bool6']
    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.name = validated_data.get('name', instance.name)
        instance.char1 = validated_data.get('char1', instance.char1)
        instance.char2 = validated_data.get('char2', instance.char2)
        instance.char3 = validated_data.get('char3', instance.char3)
        instance.int1 = validated_data.get('int1', instance.int1)
        instance.int2 = validated_data.get('int2', instance.int2)
        instance.int3 = validated_data.get('int3', instance.int3)
        instance.int4 = validated_data.get('int4', instance.int4)
        instance.int5 = validated_data.get('int5', instance.int5)
        instance.int6 = validated_data.get('int6', instance.int6)
        instance.bool1 = validated_data.get('bool1', instance.bool1)
        instance.bool2 = validated_data.get('bool2', instance.bool2)
        instance.bool3 = validated_data.get('bool3', instance.bool3)
        instance.bool4 = validated_data.get('bool4', instance.bool4)
        instance.bool5 = validated_data.get('bool5', instance.bool5)
        instance.bool6 = validated_data.get('bool6', instance.bool6)
        instance.save()
        return instance
    def create(self, validated_data):
        order = len(Mindset.objects.all())
        return Mindset.objects.create(order=order + 1,**validated_data)


class UserSerializer(serializers.ModelSerializer):
    reminders = ReminderSerializer(many=True, required=False)
    class Meta:
        model = User
        fields = ['username','id','email','reminders']

        