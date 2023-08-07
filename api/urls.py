# from unicodedata import name
from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, ReminderView, DayView, DailyView, MindsetView, ThotView

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('reminder/', ReminderView.as_view()),
    path('reminder/<int:reminder_id>', ReminderView.as_view()),
    path('day/', DayView.as_view()),
    path('day/<int:day_id>', DayView.as_view()),
    path('daily/', DailyView.as_view()),
    path('daily/<int:daily_id>', DailyView.as_view()),
    path('mindset/', MindsetView.as_view()),
    path('mindset/<int:mindset_id>', MindsetView.as_view()),
    path('thot/', ThotView.as_view()),
    path('thot/<int:thot_id>', ThotView.as_view()),
]