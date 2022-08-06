from django.forms import Form, ModelForm
from .models import Comment
from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mptt.forms import TreeNodeChoiceField


class CommentForm(ModelForm):
    
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
                {"class": "form-control", "placeholder": "Name"}
            )
        self.fields["message"].widget.attrs.update(
                {"class": "form-control", "placeholder": "Text"}
            )   
        
        self.fields['parent'].widget.attrs.update(
            {'class':'d-none'}
        )
        self.fields['parent'].label = ''
        self.fields['parent'].required = False

    
    class Meta:
        model = Comment
        fields = ["name","message","image","parent"]
        
        
    def clean_title(self,*args, **kwargs):
        title = self.cleaned_data.get("name")
      
        if len(title) < 8:
          raise forms.ValidationError("This title invalid") 
        return title         


    def clean_title(self,*args, **kwargs):
        title = self.cleaned_data.get("name")
        
        if len(title) < 8 :
            raise forms.ValidationError("chi lini senc")
        
        return title
    


class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
        
    def  __init__(self,*args, **kwargs):
        super(CreateUserForm,self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class":"form-control","placeholder":"Name","id":"fullName"}
        )
        self.fields["email"].widget.attrs.update(
            {"class":"form-control","placeholder":"email","id":"emailAddress"}
        )
        self.fields["password1"].widget.attrs.update(
            {"class":"form-control","placeholder":"password","id":"subject"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class":"form-control","placeholder":"password2","id":"message"}
        )