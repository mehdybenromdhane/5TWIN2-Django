from django.shortcuts import render,redirect,HttpResponse

from django.http import JsonResponse

from django.views.generic import ListView,CreateView,UpdateView,DeleteView
# Create your views here.

from django.urls import reverse_lazy

from .forms import EventForm
from .models import Event, Participation


from django.contrib.auth.decorators import login_required
from Person.models import Person
from google import genai

import json

def generate(title):
# The client gets the API key from the environment variable `GEMINI_API_KEY`.
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=f"generate a description for event with title : {title}"
    )
    return response.text



def generate_description(request):
    
    if request.method=="POST":
      data=  json.loads(request.body)
      title= data.get('title',)


      description = generate(title)  


    return JsonResponse({'description':description})



def hello(request):
    
    classe= "Bonjour 5TWIN2"
    
    return render(request,'event/bonjour.html', {'c1':classe})
    
def listEvent(request):
    
    events=  Event.objects.filter(state=True)
    
    
    return render(request, 'event/list.html',{'events':events})


class ListEvents(ListView):
    model=Event
    template_name='event/list.html'
    context_object_name="events"
    
    
def details(request,ide):



   btn =False 
   person = request.user
   event =  Event.objects.get(id=ide)
   
   result = Participation.objects.filter(person= person, event=event )
   
   if result:
       btn=True
       
   else:
       btn=False
       
   
   return render(request,'event/details.html',{'event':event , 'btn':btn})


@login_required
def addEvent(request):
    
    form = EventForm()
    
    if request.method=='POST':
    
    
        form = EventForm(request.POST , request.FILES)
        form.instance.organisateur = request.user

        form.save()
        
        return redirect('listEvents')
        
        

    return render(request, 'event/add.html',{'form' :form})
    
    

class CreateEvent(CreateView):
    model=Event
    form_class= EventForm
    template_name="event/add.html"
    success_url=reverse_lazy('listEvents')
    
    
    
    
class UpdateEvent(UpdateView):
    model=Event
    form_class=EventForm
    template_name="event/update.html"
    success_url=reverse_lazy('listEvents')



class DeleteEvent(DeleteView):
    model=Event
    template_name="event/delete.html"
    success_url=reverse_lazy('listEvents')
    
    
    
def participer(request, idEvent):


   
    p1 = request.user
    e1 = Event.objects.get(id=idEvent)
    
    participe =  Participation.objects.create(event=e1 , person=p1 )
    
    participe.save()
    
    e1.nbr_participants+= 1
    
    e1.save()
    
    return redirect('listEvents')
    
    
def cancel(request, idEvent):

    p1 = request.user
    e1 = Event.objects.get(id=idEvent)
    
    participe =  Participation.objects.get(event=e1 , person=p1 )
    
    participe.delete()
    
    e1.nbr_participants-= 1
    
    e1.save()
    
    return redirect('listEvents')
    
    
