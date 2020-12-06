from django import forms
from .models import Comment, Post


class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(label='عنوان التدوينة')
    content = forms.CharField(label='نص التدوينة', widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ['title', 'content' , 'category']


class DateInput(forms.DateInput):
    
    input_type = 'date'
    

class RegsForm(forms.Form):

    
    companyName = forms.CharField(max_length=50,
                                  widget=forms.TextInput(attrs=
                                                          {'class':'form-control' , 
                                                           'placeholder':'companyName',
                                                           
                                                           }))
    
    creationDate = forms.DateField(widget=DateInput(attrs=
                                                          {'class':'form-control' , 
                                                           }))
    
    status = forms.CharField(max_length=50,
                                  widget=forms.TextInput(attrs=
                                                          {'class':'form-control' , 
                                                           'placeholder':'SARL/EURL/SPA...etc.',}))
    
    
    associatesNumber = forms.CharField(max_length=50,
                                  widget=forms.TextInput(attrs=
                                                          {'class':'form-control' , 
                                                           'placeholder':"Nombre d 'associées",}))
    
    
    employeesNumber=forms.CharField(max_length=50,
                                  widget=forms.TextInput(attrs=
                                                          {'class':'form-control' , 
                                                           'placeholder':"Nombre d'employés",}))
    
    
    
    createdJobsNumber=forms.CharField(max_length=50,
                                  widget=forms.TextInput(attrs=
                                                          {'class':'form-control' , 
                                                           'placeholder':"عدد الوظائف التي أنشأتها شركتك",}))
    
    
    
    fullAddress=forms.CharField(max_length=50,
                                  widget=forms.TextInput(attrs=
                                                          {'class':'form-control' , 
                                                           'placeholder':" العنوان الكامل",}))

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
    
    
    wilaya=forms.ChoiceField(choices = GEEKS_CHOICES ,
                                widget=forms.Select(attrs=
                                                          {'class':'form-control' , 
                                                           'placeholder':"الولاية",})) 
                                 
    
    ownersEmail=forms.CharField(max_length=50,
                                  widget=forms.EmailInput(attrs=
                                                          {'class':'form-control' , 
                                                           'placeholder':" عنوان البريد الإلكتروني للمدير ",}))
    
    
    ownersLinkedin=forms.URLField(max_length=50,
                                  widget=forms.TextInput(attrs=
                                                          {'class':'form-control' , 
                                                           'placeholder':"لينكدين المدير ",}))
    
    
    
    contactEmail=forms.CharField(max_length=50,
                                  widget=forms.EmailInput(attrs=
                                                          {'class':'form-control' , 
                                                           'placeholder':" عنوان البريد الإلكتروني للاتصال",}))
    
    
    
    mobilePhoneNumber=forms.CharField(max_length=50,
                                  widget=forms.TextInput(attrs=
                                                          {'class':'form-control' , 
                                                           'placeholder':"الهاتف المحمول",}))
    mainPhoneNumber=forms.CharField(max_length=50,
                                  widget=forms.TextInput(attrs=
                                                          {'class':'form-control' , 
                                                           'placeholder':"الهاتف الرئيسي",}))        
