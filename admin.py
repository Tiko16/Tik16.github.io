
from django.contrib import admin
from main.models import Contacts,socialmedia,slide,Welcom,Doctors,category,Post,Comment,ShopCategory,shop,pagetext,video,categoryfirst,CategoryLast
from django.utils.safestring import mark_safe
from django.db.models.functions import TruncDay,TruncDate
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from modeltranslation.admin import TranslationAdmin
from django.contrib.auth.models import User, Group
from mptt.admin  import MPTTModelAdmin

import json
admin.site.unregister(Group)


admin.site.site_header = 'EsteLive-Ադմինիստրացիա'
# @admin.action(description='Mark selected stories as published')

# Register your models here.

class AdminWelcom(TranslationAdmin):
    
    list_display = ["title","return_img"]
    list_display_links = ["title","return_img"]
    readonly_fields = ["return_img"]
    
    fieldsets = (
        ("Վերնագիր-Տեքստ", {
            "fields": (
                'title','text','image'
            ),
        }),
 
    )
    
    def return_img(self, obj=None):
        return mark_safe(f"<img style='width:100px;'src='{obj.image.url}'></img>")

    return_img.short_description = "նկար"

    def return_title(self, obj=None):
        return obj.text[:20] + "..." if len(obj.text) > 20 else ""

    return_title.short_description = "Վերնագիր"
    
class AdminDoctors(TranslationAdmin):
    
    list_display = ["return_title","return_categoris","return_img"]
    list_display_links = ["return_title","return_categoris","return_img"]
    fieldsets = (
        ("Վերնագիր-Տեքստ", {
            "fields": (
                'title','categoris'
            ),
        }),
        ("Նկարագրություն-Նկար", {
            "fields": (
                'text','image'
            ),
        }),
 
    )
    def return_img(self, obj=None):
        return mark_safe(f"<img style='width:100px;'src='{obj.image.url}'></img>")
    
    def return_title(self, obj=None):
        return obj.title[:20] + "..." if len(obj.title) > 20 else obj.title
    
    def return_categoris(self, obj=None):
        return obj.categoris[:20] + "..." if len(obj.categoris) > 20 else obj.categoris

class AdminComment(MPTTModelAdmin):
    list_display = ["name","return_text","return_img","button"]    
    list_display_links = ["name","return_text","return_img"] 
    list_filter = ["button",]
    

    def return_text(self, obj=None):
        return obj.name[:20] + "..." if len(obj.name) > 20 else obj.name
    
    def return_img(self, obj=None):
        return mark_safe(f"<img style='width:100px'src='{obj.image.url}'></img>")
    
    
    
class AdminPost(TranslationAdmin):
    list_display = ["title","category",  "doctory","return_img"]
    
    

    
    def return_img(self, obj=None):
        return mark_safe(f"<img style='width:100px;'src='{obj.image.url}'></img>")
    
class Adminvideo(admin.ModelAdmin):
    list_display = ["video","return_video"]
    
    def return_video(self,obj=None):
        return mark_safe(f"<iframe width ='195' height='120' src='{obj.video}'></iframe>")

class AdminShop(admin.ModelAdmin):
    list_display  = ("title","category","price","return_img")
    list_display_links = ("title","category","price","return_img")
    
    
    def return_img(self, obj=None):
        return mark_safe(f"<img style='width:100px;'src='{obj.image.url}'></img>")

class ScoialAdmin(admin.ModelAdmin):
    
    list_display = ["name","logo"]
    
    list_display_links = ["name","logo"]
    def logo(self,obj=None):
        if obj.chois == "facebook":
            return mark_safe(f"<img style='width:90px' src='https://cdn.iconscout.com/icon/free/png-256/facebook-logo-2019-1597680-1350125.png' >")
        elif obj.chois == "instagram":
            return mark_safe(f"<img style='width:100px' src='https://cdn4.iconfinder.com/data/icons/social-media-2210/24/Instagram-512.png' >")
        elif obj.chois == "telegarm":
            return mark_safe(f"<img style='width:100px'  src='https://www.nataprint.com.ua/wp-content/uploads/2018/11/kisspng-telegram-computer-icons-apple-icon-image-format-telegram-icon-enkel-iconset-froyoshark-5ab08446a53055.4844118815215176386766.png' >")
        else:
            return mark_safe(f"<img style='width:100px'  src='https://i.pinimg.com/originals/39/44/6c/39446caa52f53369b92bc97253d2b2f1.png' >")
    
     
admin.site.register(Contacts)
admin.site.register(Post,AdminPost)
admin.site.register(socialmedia,ScoialAdmin)
admin.site.register(slide)
admin.site.register(Comment,AdminComment)
admin.site.register(category)
admin.site.register(ShopCategory)
admin.site.register(shop,AdminShop)
admin.site.register(Welcom,AdminWelcom)
admin.site.register(Doctors,AdminDoctors)
admin.site.register(pagetext)
admin.site.register(video,Adminvideo)
admin.site.register(categoryfirst)
admin.site.register(CategoryLast)



# @admin.register(Comment)
# class EmailSubscriberAdmin(admin.ModelAdmin):
#     list_display = ("post", "name", "created_at")
#     ordering = ("-created_at",)
#     change_list_template = "admintemplate.html"


#     def changelist_view(self, request, extra_context=None):
#         # Aggregate new subscribers per day
#         chart_data = (
#             Comment.objects.annotate(date=TruncDay("created_at"))
#             .values("date")
#             .annotate(y=Count("created_at"))
#             .order_by("-date")
#         )

#         # Serialize and attach the chart data to the template context
#         as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
#         extra_context = extra_context or {"chart_data": as_json}

#         # Call the superclass changelist_view to render the page
#         return super().changelist_view(request, extra_context=extra_context)


