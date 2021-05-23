from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.views.generic.base import RedirectView, TemplateView, View
from .task import *
from .helper import *



# ---------------INFO on HOW methods are called --------------------

# http_method_names
# The list of HTTP method names that this view will accept.

# Default:

# ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
# Methods

# classmethod as_view(**initkwargs)¶
# Returns a callable view that takes a request and returns a response:

# response = MyView.as_view()(request)
# The returned view has view_class and view_initkwargs attributes.

# When the view is called during the request/response cycle, the setup() method assigns the HttpRequest to the view’s request attribute, and any positional and/or keyword arguments captured from the URL pattern to the args and kwargs attributes, respectively. Then dispatch() is called.

# setup(request, *args, **kwargs)¶
# Performs key view initialization prior to dispatch().

# If overriding this method, you must call super().

# dispatch(request, *args, **kwargs)¶
# The view part of the view – the method that accepts a request argument plus arguments, and returns a HTTP response.

# The default implementation will inspect the HTTP method and attempt to delegate to a method that matches the HTTP method; a GET will be delegated to get(), a POST to post(), and so on.

# By default, a HEAD request will be delegated to get(). If you need to handle HEAD requests in a different way than GET, you can override the head() method. See Supporting other HTTP methods for an example.

# http_method_not_allowed(request, *args, **kwargs)¶
# If the view was called with a HTTP method it doesn’t support, this method is called instead.

# The default implementation returns HttpResponseNotAllowed with a list of allowed methods in plain text.

# options(request, *args, **kwargs)¶
# Handles responding to requests for the OPTIONS HTTP verb. Returns a response with the Allow header containing a list of the view’s allowed HTTP method names.



#####--------------- Also check the below link ------------------------------####
# https://www.brennantymrak.com/articles/comprehending-class-based-views-view-base-class.html



# Create your views here.

# class to add new items and show the records
class UserAddShowView(TemplateView): # templateview inherits view class
    template_name =  'enroll/add_and_show.html'

    # for seeing data
    def get_context_data(self, *args, **kwargs):
        
        # sleepy(10)
        # sleepy.delay(10)

        # sendmail_without_celery()
        # send_mail_task.delay()
        send_mail_task

        context = super().get_context_data(**kwargs) # calling context from parent
        print(context)
        fm = StudentRegistration()
        stud = User.objects.all()
        # context = {'stu': stud, 'form': fm} # overriding context
        context['stu'] = stud # appending to context
        context['form'] = fm # appending to context
        print(context)

        return context

    # for post/adding data
    def post(self, request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            return HttpResponseRedirect('/') # redirects to home

    
# for deleting data
class UserDeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs): 
        print(kwargs) # stu.id from the template, received to url, and then to kwargs
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)
    


# for updating data
class UserUpdateData(View):
    def get(self, request, id): #id from template->urls.py->here, we can write kwargs too instead of id
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        return render(request,'enroll/update_student.html',{'form':fm})
    
    def post(self, request, id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')





