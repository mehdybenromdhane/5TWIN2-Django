from django.db import models

# Create your models here.


from Person.models import Person

from datetime import datetime

category_list = (("Musique","Musique"),
                 ('Cinema', 'Cinema'),
                 ('Sport','Sport')
                 )

class Event (models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    image =models.ImageField(upload_to='images')
    category = models.CharField(max_length=20 , choices=category_list)
    state = models.BooleanField(default=True)
    nbr_participants = models.IntegerField(default=0)
    evt_date= models.DateTimeField()
    creation_date= models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    
    organisateur = models.ForeignKey(Person, on_delete=models.SET_NULL ,null=True )
    
    participant= models.ManyToManyField(Person, through="Participation" , related_name="participant")
    
    
    
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        constraints= [                               
            models.CheckConstraint(check= models.Q(evt_date__gt=datetime.now()), name="Please check event date")
        ]
        
        

class Participation(models.Model):
    
    event = models.ForeignKey(Event , on_delete=models.CASCADE)
    
    person = models.ForeignKey(Person , on_delete=models.CASCADE)
    
    participation_date =models.DateField(auto_now_add=True)
    
    
    class Meta:
        
        unique_together=['event', 'person']