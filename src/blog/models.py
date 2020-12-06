from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse



class Category(models.Model):

    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    category=models.ForeignKey(Category , on_delete=models.PROTECT , default=1)

    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # return '/detail/{}'.format(self.pk)
        return reverse('detail', args=[self.pk])

    class Meta:
        ordering = ('-post_date', )


class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name='الاسم')
    email = models.EmailField(verbose_name='البريد الإلكتروني')
    body = models.TextField(verbose_name='التعليق')
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return 'علق {} على {}.'.format(self.name, self.post)

    class Meta:
        ordering = ('-comment_date',)

class AppRegs(models.Model):
    
    
    companyName = models.CharField(max_length=50,blank=True, null=True)
    creationDate = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50,blank=True, null=True)
    associatesNumber = models.IntegerField(blank=True, null=True)
    employeesNumber = models.IntegerField(blank=True, null=True)
    createdJobsNumber = models.IntegerField(blank=True, null=True)
    fullAddress = models.CharField(max_length=50,blank=True, null=True)

    GEEKS_CHOICES = (

        ("أدرار" , "أدرار"),
        ("الشلف" , "الشلف"),
        ("الأغواط" , "الأغواط"),
        ("أم البواقي" , "أم البواقي"),
        ("باتنة" , "باتنة"),
        ("بجاية" , "بجاية"),
        ("بسكرة" , "بسكرة"),
        ("بشار" , "بشار"),
        ("البليدة" , "البليدة"),
        ("البويرة" , "البويرة"),
        ("تمنراست" , "تمنراست"),
        ("تبسة" , "تبسة"),
        ("تلمسان" , "تلمسان"),
        ("تيارت" , "تيارت"),
        ("تيزي وزو" , "تيزي وزو"),
        ("الجزائر" , "الجزائر"),
        ("الجلفة" , "الجلفة"),
        ("جيجل" , "جيجل"),
        ("سطيف" , "سطيف"),
        ("سعيدة" , "سعيدة"),
        ("سكيكدة" , "سكيكدة"),
        ("سيدي بلعباس" , "سيدي بلعباس"),
        ("عنابة" , "عنابة"),
        ("قالمة" , "قالمة"),
        ("قسنطينة" , "قسنطينة"),
        ("المدية" , "المدية"),
        ("مستغانم" , "مستغانم"),
        ("المسيلة" , "المسيلة"),
        ("معسكر" , "معسكر"),
        ("ورقلة" , "ورقلة"),
        ("وهران" , "وهران"),
        ("البيض" , "البيض"),
        ("إليزي" , "إليزي"),
        ("برج بوعريريج" , "برج بوعريريج"),
        ("بومرداس" , "بومرداس"),
        ("الطارف" , "الطارف"),
        ("تيندوف" , "تيندوف"),
        ("تيسمسيلت" , "تيسمسيلت"),
        ("وادي سوف" , "وادي سوف"),
        ("سوق أهراس" , "سوق أهراس"),
        ("تيبازة" , "تيبازة"),
        ("عين الدفلى" , "عين الدفلى"),
        ("النعامة" , "النعامة"),
        ("عين تيموشنت" , "عين تيموشنت"),
        ("غرداية" , "غرداية"),
        ("غليزان" , "غليزان"),
    )                                                       
    
    wilaya = models.CharField(max_length=100,choices = GEEKS_CHOICES,blank=True, null=True)
    ownersEmail = models.EmailField(blank=True, null=True)
    ownersLinkedin = models.URLField(blank=True, null=True)
    contactEmail = models.EmailField(blank=True, null=True)
    mobilePhoneNumber = models.CharField(max_length=50,blank=True, null=True)
    mainPhoneNumber = models.CharField(max_length=50,blank=True, null=True)
    
    
    def __str__(self):
        
        return self.companyName  

    def get_addmin_url(self):
        
        return reverse ('adminapp' , args=[self.pk])          


