from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment ,AppRegs ,Category
from .forms import NewComment, PostCreateForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import CreateView, UpdateView, DeleteView ,ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import RegsForm
from django.http import HttpResponse 


def home(request):
    posts = Post.objects.all()

    
    context = {
        'title': 'الصفحة الرئيسية',
        'posts': posts,
        
    }
    return render(request, 'blog/index.html', context)


    # All Posts function
def allposts(request):
    posts = Post.objects.all()

    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_page)
    context = {
        'title': 'موضوعات متنوعه ',
        'posts': posts,
        'page': page,
    }
    return render(request, 'blog/all_posts.html', context)

# End Of All Posts function


# Application Form

def formm(request):


    if request.method == "POST":

        form = RegsForm (request.POST)

        if form.is_valid():
            appregister = AppRegs(companyName=form.cleaned_data['companyName'],
                            creationDate=form.cleaned_data['creationDate'],
                            status=form.cleaned_data['status'],
                            associatesNumber=form.cleaned_data['associatesNumber'],
                            employeesNumber=form.cleaned_data['employeesNumber'],
                            createdJobsNumber=form.cleaned_data['createdJobsNumber'],
                            fullAddress=form.cleaned_data['fullAddress'],
                            wilaya=form.cleaned_data['wilaya'],
                            ownersEmail=form.cleaned_data['ownersEmail'],
                            ownersLinkedin=form.cleaned_data['ownersLinkedin'],
                            contactEmail=form.cleaned_data['contactEmail'],
                            mobilePhoneNumber=form.cleaned_data['mobilePhoneNumber'],
                            mainPhoneNumber=form.cleaned_data['mainPhoneNumber'])
            
            appregister.save()

        return redirect('formm')

        
    context = {
        'form': RegsForm
    }
        
    return render(request, 'blog/formm.html',context)




   


    


# def adduser(request):
    
    
    

#     if request.method == "POST":
#         form = RegsForm (request.POST)
#         if form.is_valid():

            
#             appregister = AppRegs(companyName=form.cleaned_data['companyName'],
#                             creationDate=form.cleaned_data['creationDate'],
#                             status=form.cleaned_data['status'],
#                             associatesNumber=form.cleaned_data['associatesNumber'],
#                             employeesNumber=form.cleaned_data['employeesNumber'],
#                             createdJobsNumber=form.cleaned_data['createdJobsNumber'],
#                             fullAddress=form.cleaned_data['fullAddress'],
#                             wilaya=form.cleaned_data['wilaya'],
#                             ownersEmail=form.cleaned_data['ownersEmail'],
#                             ownersLinkedin=form.cleaned_data['ownersLinkedin'],
#                             contactEmail=form.cleaned_data['contactEmail'],
#                             mobilePhoneNumber=form.cleaned_data['mobilePhoneNumber'],
#                             mainPhoneNumber=form.cleaned_data['mainPhoneNumber'])
            
#             appregister.save()

#         return redirect('home')
	
 

    


def about(request):
    return render(request, 'blog/about.html', {'title': 'من أنا'})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(active=True)

    # check before save data from comment form
    if request.method == 'POST':
        comment_form = NewComment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            # Deprecated line to prevent form to post data when refresh a page
            # comment_form = NewComment()
            return redirect('detail', post_id)
    else:
        comment_form = NewComment()

    context = {
        'title': post,
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'blog/detail.html', context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ['title', 'content']
    template_name = 'blog/new_post.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class CatListView(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'catlist'



    def get_queryset(self):

        
        content = {

            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category']),
        }

        return content

def category_list(request):

    category_list = Category.objects.all()
    paginator = Paginator(category_list, 5)
    page = request.GET.get('page')
    try:
        category_list = paginator.page(page)
    except PageNotAnInteger:
        category_list = paginator.page(1)
    except EmptyPage:
        category_list = paginator.page(paginator.num_page)

    context = {
        "category_list": category_list,
        'page': page,
    }
    return context    

def application_list(request):
    
    application_list = AppRegs.objects.all()
    context = {
        "application_list": application_list,
    }
    return context    

def applist(request , app_id):
    applicationId = get_object_or_404(AppRegs,pk=app_id)
    # form=AppRegs.objects.all()
    
    context = {
        'applicationId': applicationId
    }
        
    return render(request, 'blog/table_data.html',context)     
    # return render(request, 'blog/application_detail.html',context)     
    # return render(request, 'blog/app_list.html',context)     

def admin_list(request):
    
    admin_list = AppRegs.objects.all()
    context = {
        "admin_list": admin_list,
    }
    return render(request,'blog/application_admin_detail.html',context)     
