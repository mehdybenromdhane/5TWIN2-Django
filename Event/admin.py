from django.contrib import admin


from .models import Event,Participation
# Register your models here.

# admin.site.register(Event)


class ParticipationInline(admin.TabularInline):
    model =Participation
    extra=2


def accept_state(ModelAdmin , request,queryset):
    
    queryset.update(state=True)




def refuse_state(ModelAdmin , request,queryset):
    
    queryset.update(state=False)
    
    
    

def changeSport(ModelAdmin , request,queryset):
    
    queryset.update(category='Sport')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    
    list_display=('title','description','category','state','evt_date','nbr_participants','organisateur',)
    list_per_page=5
    
    list_filter=('category','state','nbr_participants','organisateur',)
    
    search_fields=('title',)
    
    autocomplete_fields=('organisateur',)
    
    actions=[accept_state,refuse_state , changeSport]
    
    
    inlines=[ParticipationInline]
    
    









admin.site.register(Participation)