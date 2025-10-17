


from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model

class UserRegistration(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['cin','first_name','last_name','username','email', 'password1','password2']
        
    def save(self , commit=True):
        
        user = super(UserRegistration,self).save(commit=False)

        if commit:
            user.save()
            
        return user