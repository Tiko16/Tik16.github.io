
from modeltranslation.translator import register,TranslationOptions
from .models import Doctors,Post,Welcom,Contacts


@register(Doctors)
class TranslateDoctors(TranslationOptions):
    fields = ("title","categoris","text")
@register(Post)    
class TranslatePost(TranslationOptions):
    fields = ("title","text")
@register(Welcom)
class TranslateWelcom(TranslationOptions):
    fields = ("title","text")

