from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
    return render(request,'student_dashboard_app/index.html')


def add_user(request):
    errors = User.objects.basic_validator(request.POST)
    print "FROM USER", request.POST
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
    else: 
        myrequest = request.POST

        # need to Bcrypt our password
        hash1 = bcrypt.hashpw( myrequest['password'].encode('utf8') , bcrypt.gensalt())
        user = User.objects.create(first_name=myrequest['first_name'], email=myrequest['email'], password=hash1, hired=myrequest['hired'])
        user.save()
    return redirect('/')


def login(request):
    if request.method == 'POST':
        myrequest = request.POST
        user = User.objects.filter(email=myrequest['email'])
        
        if len(user) == 0:
            errors = {}
            errors['user_not_registered'] = "Your email was never found, please try again!"
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            hash2 = user[0].password
            if bcrypt.checkpw(myrequest['password'].encode('utf8'), hash2.encode('utf8')):
                print "1232345323145"
                request.session['id'] = user[0].id
                request.session['first_name'] = user[0].first_name
                request.session['email'] = user[0].email
                request.session['hired'] = user[0].hired
                request.session['login'] = True
                return redirect('/dashboard')
            else:
                errors = {}
                errors['no_password_found'] = "Password hasn't match with any that we have here. Please try again!"
                for tag, error in errors.iteritems():
                    messages.error(request, error, extra_tags=tag)
                return redirect('/')

def wish_time(request):
    if 'login' not in request.session:
        return redirect('/')
    if request.session['login']==False:
        return redirect('/')
    print 'go to dashboard'
    data = {
        'reviews': Review.objects.all().order_by('-created_at')[:3],
        'books': Book.objects.all()
    }
    return render(request, 'student_dashboard_app/dashboard.html', data)

def wish_list(request, id):
    if 'login' not in request.session:
        return redirect('/')
    if request.session['login']==False:
        return redirect('/')
    
    all_wishes = Wish.objects.all()
    print all_wishes

    this_user = User.objects.get(id=request.session['id'])
    this_wish = Wish.objects.get(id=2)

    this_wish.users.add(this_user)

    return redirect('/dashboard')


def add_to_wishlist(request, id):

    this_user = User.objects.get(id=request.session['id'])
    this_wish = Wish.objects.get(id=id)
    this_wish.users.add(this_user)

    allobj = this_wish.users.filter(wishes_likes=request.session['id'])
    print "============================="
    print allobj

    return redirect('/dashboard')

def dashboard(request):
    me = User.objects.get(id=request.session['id'])

    data = {
        'user': User.objects.get(id=request.session['id']),
        'mywishes': Wish.objects.filter(users=request.session['id']).filter(users=request.session['id']),
        'madewishes': Wish.objects.filter(user=request.session['id']),
        'mylist': Wish.objects.filter().exclude(users=request.session['id'])
    }

    return render(request, 'student_dashboard_app/dashboard.html', data)

def remove(request, id):

    this_user = User.objects.get(id=request.session['id'])
    this_wish = Wish.objects.get(id=id)
    this_wish.users.remove(this_user)

    return redirect('/dashboard')


def delete(request, id):   
    a = Wish.objects.filter(id=id).delete()

    return redirect('/dashboard')


def add_wish(request):
    myrequest = request.POST
    u = User.objects.get(id=request.session['id'])
    r = Wish.objects.create(item=myrequest['item'], user=u)
    r.save()
    print r.id

    return redirect('/add_to_wishlist/'+str(r.id))


def make_wish(request):
    data = {
        'user': User.objects.get(id=request.session['id'])
    }
    return render(request, 'student_dashboard_app/wish_list.html', data)

def new_item(request, id):
    data = {
        'items_liked': User.objects.filter(wishes_likes=id),
        'wish': Wish.objects.get(id=id)
    }
    return render(request, 'student_dashboard_app/new_item.html', data)

def logout(request):
    request.session.clear()
    return redirect('/')