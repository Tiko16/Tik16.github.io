from main.models import Contacts,socialmedia,slide,category,Post,Doctors,Comment,pagetext
from django.core.paginator import Paginator
import random
def GetContextGenerateData(request):
    all_story = list(Post.objects.all())
    recend = random.sample(all_story,3)
    
    context = {}
    
    context["number"] = Contacts.objects.all()
    context["social"] = socialmedia.objects.all()
    context["slidecontext"] = slide.objects.all()
    context["category"] = category.objects.all()
    context["Post"] = Post.objects.all()
    context["Doctors"] = Doctors.objects.all()
    context["news_text_page"] = pagetext.objects.filter(categoryi="0")
    context["shop_text_page"] = pagetext.objects.filter(categoryi="1")
    # context["shop_text_page"] = pagetext.objects.all()
    
    
    context["recent"] = recend
    # context["shop_text_page"] = pagetext.objects.last()
    
    
    return context