
from django.db import models
from ckeditor.fields import RichTextField
from froala_editor.fields import FroalaField
from django.db.models import Q
from mptt.models import MPTTModel,TreeForeignKey
from PIL import Image 
from io import BytesIO
from django.core.files import File




class ProfileQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (
                        # Q(user__username__icontains=query)|
                        Q(title__icontains=query)
                        
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs


class PostManager(models.Manager):
    def get_queryset(self):
        return ProfileQuerySet(self.model,using=self._db)
    
    def search(self,query=None):
        return self.get_queryset().search(query=query)






Choicese = [
    ("number","հեռախոսահամար"),
    ("email","Ել․հասցե"),
    ("addres","Հասցե"),
    
]

class Contacts(models.Model):
    name = FroalaField("Մութքագրման դաշտ",max_length=50)
    chois = models.CharField("Տեսակ", choices=Choicese, max_length=15)
    
    def __str__(self):
       return self.name
   
    class Meta:
        
        verbose_name = 'Տվյալ'
        verbose_name_plural = 'Տվյալներ'
  
  
SocialChoicese = [
    ("facebook","facebook"),
    ("instagram","instagram"),
    ("telegarm","telegarm"),
    
]      
        
class socialmedia(models.Model):
    name = models.URLField("URL-հասցե")
    chois = models.CharField("Ցանկ",max_length=15,choices=SocialChoicese)
    
    def __str__(self):
        return self.name
    
    class  Meta:
        
        verbose_name = 'Սոցցանց'
        verbose_name_plural = 'Սոցցանցեր'
    
    
class slide(models.Model):
    
    slide = models.ImageField(upload_to="slide")
    
    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.slide = new_image
        super().save(*args, **kwargs)
    
    class Meta:
      
        verbose_name = 'Սլայդ'
        verbose_name_plural = 'Սլայդներ'
    
class Welcom(models.Model):
    title = models.CharField("վերնագր",max_length=68)
    text = RichTextField("տեքստ")
    image = models.ImageField("Նկար",upload_to="Welcom")
    
    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Գլխաոր"
        verbose_name_plural = "Գլխաոր"
    
class Doctors(models.Model):
    title = models.CharField("Անուն",max_length=100)
    categoris = models.CharField("մասնագիտություն",max_length=100)
    image = models.ImageField("նկար",upload_to="Doctors")
    text = RichTextField("նկարագիր")
    
    objects = PostManager()
    
    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Բժիշկ"
        verbose_name_plural = "Բժիշկներ"

   
    
class category(models.Model):
    title = models.CharField("կատեգորյայի-անվանում",max_length=200)
    text = RichTextField("գլխաոր-տեքստ")
    Paragraphtext = models.CharField("յեկրորտական-տքստ",max_length=165)
    file = models.FileField("նկար կամ վիդեո",upload_to="category")
    slug = models.SlugField("URI")

    
    def __str__(self):
        return self.title
    
    class Meta:
                
        verbose_name = 'կատեգորյա'
        verbose_name_plural = 'կատեգորյաներ'
 
class Post(models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE, verbose_name="Կատեգորյաներ", related_name="KeyCategori")  
    image = models.FileField("նկար կամ վիդեո",upload_to="Post")   
    title = models.CharField("նյութի վերնագիր",max_length=100)
    text = RichTextField("Նյութի բովանդակություն")
    doctory = models.ForeignKey(Doctors,on_delete=models.CASCADE, verbose_name="բժիշկը", related_name="KeyDoctots")
    data = models.DateTimeField("ժամանակ",auto_now_add=True)
    rec = models.BooleanField("գլխաոր-նյութում",default=False)
    
    objects = PostManager()

    def __str__(self):
        return self.title
    
    
    class Meta:
       
        verbose_name = 'Գլախաոր-Փոստ'
        verbose_name_plural = 'Գլախաոր-Փոստ'
      
      
class Comment(MPTTModel):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    parent = TreeForeignKey("self",on_delete=models.CASCADE,null=True,blank=True,related_name='children')

    name = models.CharField("Անվանում",max_length=24)
    message = models.TextField("մաեկնաբանություն")
    image = models.ImageField("նակար",upload_to="comment",null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    button = models.BooleanField("Հաստատել",default=False)
    
    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)
    
    class MPTTMeta:
        order_insertion_by = ['name']
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Կոմենտ'
        verbose_name_plural = 'Կոմենտներ'
        
    
class ShopCategory(models.Model):
    
    title = models.CharField("կատեգորյա",max_length=100)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Ապրանքիկատեգորյա'
        verbose_name_plural = 'Ապրանքիկատեգորյաներ'
        
class shop(models.Model):
    
    title = models.CharField("վերնագիր",max_length=17)
    category = models.ForeignKey(ShopCategory,related_name="comments",on_delete=models.CASCADE)
    price = models.SmallIntegerField("արժեք")
    image = models.ImageField("Նկար",upload_to="shop")
    objects = PostManager()
    
    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = 'Ապրանք'
        verbose_name_plural = 'Ապրանքներ'
  
textchoise = [
    ("0","news"),
    ("1","shop"),
    
]      
class pagetext(models.Model):
    
    
        
    categoryi = models.CharField("նշեք էջը",choices=textchoise,max_length=100)
    texti = RichTextField()
    
    def __str__(self):
        return self.categoryi
    
    
    class Meta:
        verbose_name = "Էջի մեկնաբանություն"
        verbose_name_plural = "Էջի մեկնաբանություներ"
        
class video(models.Model):
    
    video = models.URLField("URL")
    
    def __str__(self):
        return self.video
    
    class Meta:
        verbose_name="Մեդիա"
        verbose_name_plural = "Մեդիա"
        
        
class categoryfirst(models.Model):
    title = models.CharField("Վերնագիր",max_length=100)
    text = RichTextField("տեքստ")
    time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField("նկար",upload_to="categoryfirst")
    slug = models.SlugField()
    
    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Գլղավոր-Կատեգորյ"
        verbose_name_plural = "Գլղավոր-Կատեգորյաներ" 
        
        
class CategoryLast(models.Model):
    title = models.CharField("Վերնագիր",max_length=100)
    text = RichTextField("տեքստ")
    time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField("նկար",upload_to="categoryfirst")
    keylast = models.ForeignKey(categoryfirst,on_delete=models.CASCADE,related_name="kategorykey")
           
    def __str__(self):
        
        return self.title
    
    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)
        
    
    class Meta:
        verbose_name = "Յեկրերթական-Կատեգորյա"
        verbose_name_plural ="Յեկրերթական-Կատեգորյանոր "
    
    
def compress(image):
    im = Image.open(image)
    im_io = BytesIO() 
    im.save(im_io, 'JPEG', quality=50) 
    new_image = File(im_io, name=image.name)
    return new_image