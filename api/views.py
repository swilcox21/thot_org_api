from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly
from api.models import Reminder, Daily, Day, Thot, Mindset
from api.serializers import UserSerializer, ReminderSerializer, DailySerializer, DaySerializer, ThotSerializer, MindsetSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.http import Http404
from django.shortcuts import get_object_or_404


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class ReminderView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    def get(self, request, reminder_id=None):
        print('request.data', self)
        if reminder_id is not None:
            reminder = get_object_or_404(Reminder.objects.all(), id = reminder_id)
            serialized_reminder = ReminderSerializer(reminder)
            return Response(serialized_reminder.data)
        all_reminders = Reminder.objects.filter(owner=request.user.id)
        serializer = ReminderSerializer(all_reminders, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ReminderSerializer(data=request.data, many=True)
        print('user', request.user)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        reminders = []
        for r in request.data:
            reminder = get_object_or_404(Reminder.objects.all(), id=r.get('id'))
            print('!!!!!USER:!!!!!!', r)
            ser_reminder = ReminderSerializer(instance=reminder, data=r, partial=True)
            print('!!!!!USER:!!!!!!', request)
            if ser_reminder.is_valid(raise_exception=True):
                ser_reminder.save()
            reminders.append(ser_reminder.data)
        return Response(reminders, status=status.HTTP_202_ACCEPTED)
    def delete(self,request,reminder_id):
        res = get_object_or_404(Reminder.objects.all(), id=reminder_id)
        reminder = get_object_or_404(Reminder.objects.all(), id=reminder_id)
        reminder.delete()
        return Response({"message": "reminder: `{}` has been deleted".format(res)}, status=status.HTTP_202_ACCEPTED)

class DailyView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    def get(self, request, daily_id=None):
        print('request.data', Day.objects.get(id=1).name)
        if daily_id is not None:
            daily = get_object_or_404(Daily.objects.all(), id = daily_id)
            serialized_daily = DailySerializer(daily)
            return Response(serialized_daily.data)
        all_dailies = Daily.objects.all()
        serializer = DailySerializer(all_dailies, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = DailySerializer(data=request.data, many=True)
        print('!!!!!USER:!!!!!!', request.data[0]['daily'])
        if serializer.is_valid():
            serializer.save(day=Day.objects.filter(id=request.data[0]['day'].get('id')).first())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        dailies = []
        for t in request.data:
            daily = get_object_or_404(Daily.objects.all(), id=t.get('id'))
            print('!!!!!USER:!!!!!!', t)
            ser_daily = DailySerializer(instance=daily, data=t, partial=True)
            print('!!!!!USER:!!!!!!', request)
            if ser_daily.is_valid(raise_exception=True):
                ser_daily.save()
            dailies.append(ser_daily.data)
        return Response(dailies, status=status.HTTP_202_ACCEPTED)

class DayView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    def get(self, request, day_id=None):
        print('request.data', self)
        if day_id is not None:
            day = get_object_or_404(Day.objects.all(), id = day_id)
            serialized_day = DaySerializer(day)
            return Response(serialized_day.data)
        all_days = Day.objects.filter(owner=request.user.id)
        serializer = DaySerializer(all_days, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = DaySerializer(data=request.data, many=True)
        print('user', request.user)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        days = []
        for f in request.data:
            day = get_object_or_404(Day.objects.all(), id=f.get('id'))
            print('!!!!!USER:!!!!!!', f)
            ser_day = DaySerializer(instance=day, data=f, partial=True)
            print('!!!!!USER:!!!!!!', request)
            if ser_day.is_valid(raise_exception=True):
                ser_day.save()
            days.append(ser_day.data)
        return Response(days.data, status=status.HTTP_202_ACCEPTED)
    def delete(self,request):
        days = []
        for f in request.data:
            day = get_object_or_404(Day.objects.all(), id=f.get('id'))
            days.append(day)
            day.delete()
        return Response({"message": "`{}` have been deleted".format(days)},status=status.HTTP_202_ACCEPTED)

class ThotView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    def get(self, request, thot_id=None):
        print('request.data', Mindset.objects.get(id=1).name)
        if thot_id is not None:
            thot = get_object_or_404(Thot.objects.all(), id = thot_id)
            serialized_thot = ThotSerializer(thot)
            return Response(serialized_thot.data)
        all_thots = Thot.objects.all()
        serializer = ThotSerializer(all_thots, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ThotSerializer(data=request.data, many=True)
        print('!!!!!USER:!!!!!!', request.data[0]['mindset'])
        if serializer.is_valid():
            serializer.save(mindset=Mindset.objects.filter(id=request.data[0]['mindset'].get('id')).first())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        thots = []
        for t in request.data:
            thot = get_object_or_404(Thot.objects.all(), id=t.get('id'))
            print('!!!!!USER:!!!!!!', t)
            ser_thot = ThotSerializer(instance=thot, data=t, partial=True)
            print('!!!!!USER:!!!!!!', request)
            if ser_thot.is_valid(raise_exception=True):
                ser_thot.save()
            thots.append(ser_thot.data)
        return Response(thots, status=status.HTTP_202_ACCEPTED)
    def delete(self,request):
        thots = []
        for t in request.data:
            thot = get_object_or_404(Thot.objects.all(), id=t.get('id'))
            thots.append(thot)
            thot.delete()
        return Response({"message": "thots: `{}` has been deleted".format(thots)}, status=status.HTTP_202_ACCEPTED)

class MindsetView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    def get(self, request, mindset_id=None):
        print('request.data', self)
        if mindset_id is not None:
            mindset = get_object_or_404(Mindset.objects.all(), id = mindset_id)
            serialized_mindset = MindsetSerializer(mindset)
            return Response(serialized_mindset.data)
        all_mindsets = Mindset.objects.filter(owner=request.user.id)
        serializer = MindsetSerializer(all_mindsets, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = MindsetSerializer(data=request.data, many=True)
        print('user', request.user)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        mindsets = []
        for f in request.data:
            mindset = get_object_or_404(Mindset.objects.all(), id=f.get('id'))
            print('!!!!!USER:!!!!!!', f)
            ser_mindset = MindsetSerializer(instance=mindset, data=f, partial=True)
            print('!!!!!USER:!!!!!!', request)
            if ser_mindset.is_valid(raise_exception=True):
                ser_mindset.save()
            mindsets.append(ser_mindset.data)
        return Response(mindsets.data, status=status.HTTP_202_ACCEPTED)
    def delete(self,request):
        mindsets = []
        for f in request.data:
            mindset = get_object_or_404(Mindset.objects.all(), id=f.get('id'))
            mindsets.append(mindset)
            mindset.delete()
        return Response({"message": "`{}` have been deleted".format(mindsets)},status=status.HTTP_202_ACCEPTED)