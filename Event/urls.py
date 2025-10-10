from django.urls import path

from .views import *
urlpatterns = [
   
   path('hi/', hello ),
   
   path('list/', listEvent , name="listEvents"),
   path('listClass/',ListEvents.as_view()),
   
   path('details/<int:ide>' , details  , name="eventDetails"   ),
   
   path('add/', addEvent, name="addEvent"),
   
   path('addClass/', CreateEvent.as_view() , name="addClass"),
   
   path('update/<int:pk>',UpdateEvent.as_view(),name="updateEvent"),
   
   path('delete/<int:pk>', DeleteEvent.as_view(), name="deleteEvent"),
   
   path('join/<int:idEvent>', participer, name="join"),
   
      path('cancel/<int:idEvent>', cancel, name="cancel")


]