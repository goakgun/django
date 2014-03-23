from django.conf import settings
from django.contrib import messages
from django.contrib import auth
from django.shortcuts import render,render_to_response,RequestContext,HttpResponseRedirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from users.forms import UserForm

def home(request):
    return render_to_response("login.html",locals(),context_instance=RequestContext(request))

def contactus(request):
    return render_to_response("contactus.html",locals(),context_instance=RequestContext(request))

def aboutus(request):
    return render_to_response("aboutus.html",locals(),context_instance=RequestContext(request))


def signup(request):
    form=UserForm(request.POST or None)
    if form.is_valid():
        save_it=form.save(commit=False)
        save_it.save()
        messages.success(request,'Thank you for Joining us')
        return HttpResponseRedirect('/signup/')
    return render_to_response("signup.html",locals(),context_instance=RequestContext(request))

def logout(request): 
    return render_to_response("login.html",locals(),context_instance=RequestContext(request))

'''def aboutus(request):   
    return render_to_response("aboutus.html",locals(),context_instance=RequestContext(request))


def signin(request,template_name="accounts/user.html"):
    user_id = request.session.get('session_key')
    if user_id:
        name = request.user.username
        return render_to_response(template_name, {'username':name,'session_key':user_id})
    else:
        return render_to_response('noauth.html')
    language='tr_TR'
    session_language='tr_TR'
    if 'lang' in request.COOKIES:
        language=request.COOKIES['lang']
    if 'lang' in request.session:
        session_language=request.session['lang']
    return render_to_response("signin.html",{'language':language,'session_language':session_language})

def language(request,language='tr_TR'):
    response=HttpResponse("setting language to %s " % language)
    response.set_cookie('lang',language)
    request.session['lang'] =language
    
    return response

def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html',c)
def auth_view(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/accounts/loggedin/')
    else:
        return HttpResponseRedirect('/accounts/invalid/')
    
def loggedin(request):
    return render_to_response('loggedin.html',{'first_name':request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    #return render_to_response('logout.html')
    return render_to_response('homepage.html')

def singup(request):
    return render_to_response('signup.html')

def register(request):
    if request.method == 'POST':
        form=MyRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
    args={}
    args.update(csrf(request))
    args['form'] =  MyRegisterationForm()
    print args
    return render_to_response('register.html',args)

def register_success(request):
    return render_to_response('register_success.html')
'''
