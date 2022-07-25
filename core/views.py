from django.shortcuts import render,HttpResponseRedirect
from designer.models import Designer,RoomCustomization
from customer.models import Customer, HostelCustomer,CustomerComplaint
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import MenuForm, RulesForm, WorkerDetailsForm
from .models import Menu, Rules, WorkerDetails
from django.conf import settings
from django.core.mail import send_mail
from django.urls import get_resolver
import datetime

# Create your views here.
def home(request):
    customers=HostelCustomer.objects.filter(admin_status=False)
    date=datetime.date.today()
    for customer in customers:
        if date>customer.check_in:
            customer=Customer.objects.get(user=customer.customer.user)
            user=User.objects.get(id=customer.user_id)
            customer.delete()
            user.delete() 
    menu=Menu.objects.all()
    rules=Rules.objects.get(id=1)
    return render(request,'core/home.html',{'rules':rules,'menus':menu})

def navbar(request):
    return render(request,'core/navbar.html')

def whats_new(request):
    room=RoomCustomization.objects.last()
    return render(request,'core/whatsnew.html',{'room':room})


def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()


def is_designer(user):
    return user.groups.filter(name='DESIGNER').exists()


def is_admin(user):
    if user.is_superuser==True:
        return True
    else:
        return False



def afterlogin(request):
    if(is_customer(request.user)):
        if request.session['next']:
            next=request.session['next']
            return HttpResponseRedirect(next)
        else:
            return HttpResponseRedirect('/customer/dashboard/')
    elif (is_designer(request.user)):
        approved=Designer.objects.filter(user=request.user,approved=True).exists()
        if approved:
            if request.session['next']:
                next=request.session['next'] 
                return HttpResponseRedirect(next)
            else:
                return HttpResponseRedirect('/designer/dashboard/') 
        else:
            return HttpResponseRedirect('/designer/notapproved/')
    elif (is_admin(request.user)):
        if request.session['next']:
            next=request.session['next']
            return HttpResponseRedirect(next)
        else:
            return HttpResponseRedirect('/admin-hostel-customers/')
        

def admin_sign_in(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            request.session['next']=False
            if request.POST.get('next'):
                next=request.POST.get('next')
                request.session['next']=next
            auth_form=AuthenticationForm(request=request,data=request.POST)
            if auth_form.is_valid():
                username=auth_form.cleaned_data.get('username')
                password=auth_form.cleaned_data.get('password')
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/afterlogin/')
        else:
            auth_form=AuthenticationForm()
        return render(request,'admin/signin.html',{'authform':auth_form})
    else:
       return HttpResponseRedirect('/afterlogin/')




# @login_required(login_url='admin-sign-in')
# def admin_dashboard(request):
#     return render(request,'admin/dashboard.html')



@login_required(login_url='admin-sign-in')
def admin_hostel_customers(request):
    hostel_customers=HostelCustomer.objects.filter(admin_status=True)
    return render(request,'admin/hostelcustomers.html',{'hostelcustomers':hostel_customers})


@login_required(login_url='admin-sign-in')
def admin_upcoming_hostel_customers(request):
    customers=HostelCustomer.objects.filter(admin_status=False)
    date=datetime.date.today()
    for customer in customers:
        if date>customer.check_in:
            customer=Customer.objects.get(user=customer.customer.user)
            user=User.objects.get(id=customer.user_id)
            customer.delete()
            user.delete() 
    return render(request,'admin/upcominghostelcustomers.html',{'customers':customers})

@login_required(login_url='admin-sign-in')
def admin_approving_customer(request,id):
    hostel_customer=HostelCustomer.objects.get(id=id)
    hostel_customer.admin_status=True
    hostel_customer.save()
    return HttpResponseRedirect('/admin-hostel-customers/')
    

@login_required(login_url='admin-sign-in')
def admin_rejecting_customer(request,id):
    hostel_customer=HostelCustomer.objects.get(id=id)
    customer=Customer.objects.get(customer=hostel_customer.customer)
    user=User.objects.get(id=customer.user_id)
    customer.delete()
    user.delete()
    return HttpResponseRedirect('/admin-hostel-customers/')

@login_required(login_url='admin-sign-in')
def admin_customer_view_details(request,id):
    hostel_user=HostelCustomer.objects.get(id=id)
    return render(request,'admin/customerviewdetails.html',{'hosteluser':hostel_user})


@login_required(login_url='admin-sign-in')
def admin_pending_designers(request):
    designers=Designer.objects.filter(approved=False)
    return render(request,'admin/pendingdesigners.html',{'designers':designers})



@login_required(login_url='admin-sign-in')
def admin_approving_designer(request,id):
    designer=Designer.objects.get(id=id)
    designer.approved=True
    designer.save()
    user=User.objects.get(id=designer.user_id)
    subject='Welcome to the Hostel'
    message='''
    Congratulations Mr. '''+user.username+'''
    Your designer account is been approved by the admin.
    Now you can add your customization ideas in your designer account.
    All the best for you designer career.
    
    If you have any queries please write to us at kvamshi340@gmail.com '''
    send_mail(subject,message,settings.EMAIL_HOST_USER,[user.email],fail_silently=True)
    return HttpResponseRedirect('/admin-approved-designers/')


@login_required(login_url='admin-sign-in')
def admin_rejecting_designer(request,id):
    designer=Designer.objects.get(id=id)
    user=User.objects.get(id=designer.user_id)
    subject='Welcome to the Hostel'
    message='''
    Mr. '''+user.username+'''
    We are sorry to inform you that your designer account is 
    been rejected by the admin.This is not the end of your 
    designing career.We Hope that you will be achieving your goals 
    if life.
    
    If you have any queries please write to us at kvamshi340@gmail.com '''
    send_mail(subject,message,settings.EMAIL_HOST_USER,[user.email],fail_silently=True)
    designer.delete()
    user.delete()
    return HttpResponseRedirect('/admin-pending-designers/')


@login_required(login_url='admin-sign-in')
def admin_approved_designers(request):
    designer=Designer.objects.filter(approved=True)
    return render(request,'admin/approveddesigners.html',{'designers':designer})


@login_required(login_url='admin-sign-in')
def admin_desginer_customized_rooms(request,id):
    designer=Designer.objects.get(id=id)
    rooms=RoomCustomization.objects.filter(designer=designer)
    return render(request,'admin/designercustomizedrooms.html',{'rooms':rooms})



@login_required(login_url='admin-sign-in')
def admin_designer_view_room(request,id):
    room=RoomCustomization.objects.get(id=id)
    return render(request,'admin/designerviewroom.html',{'room':room})



@login_required(login_url='admin-sign-in')
def admin_add_worker_details(request):
    if request.method=='POST':
        form=WorkerDetailsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin-worker-details/')
    else:
        form=WorkerDetailsForm()
    return render(request,'admin/addworkerdetails.html',{'form':form})



@login_required(login_url='admin-sign-in')
def admin_worker_details(request):
    workers=WorkerDetails.objects.all()
    return render(request,'admin/workerdetails.html',{'workers':workers})



@login_required(login_url='admin-sign-in')
def admin_worker_edit(request,id):
    worker=WorkerDetails.objects.get(id=id)
    if request.method=='POST':
        form=WorkerDetailsForm(request.POST,request.FILES,instance=worker)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin-worker-details/')
    else:
        form=WorkerDetailsForm(instance=worker)
    return render(request,'admin/workeredit.html',{'form':form})



@login_required(login_url='admin-sign-in')
def admin_worker_delete(request,id):
    worker=WorkerDetails.objects.get(id=id)
    worker.delete()
    return HttpResponseRedirect('/admin-worker-details/')


@login_required(login_url='admin-sign-in')
def admin_rules(request):
    rules=Rules.objects.get(id=1)
    if request.method=='POST':
        rules_form=RulesForm(request.POST,instance=rules)
        if rules_form.is_valid():
            rules_form.save()
    else:
        rules_form=RulesForm(instance=rules)
    return render(request,'admin/rules.html',{'rulesform':rules_form}) 


@login_required(login_url='admin-sign-in')
def admin_menu(request):
    menu=Menu.objects.all()
    return render(request,'admin/menu.html',{'menus':menu})


@login_required(login_url='admin-sign-in')
def admin_menu_edit(request,id):
    menu=Menu.objects.get(id=id)
    if request.method=='POST':
        menu_form=MenuForm(request.POST,instance=menu)
        if menu_form.is_valid():
            menu_form.save()
            return HttpResponseRedirect('/admin-menu/')
    else:
        menu_form=MenuForm(instance=menu)
    return render(request,'admin/menuedit.html',{'menuform':menu_form})




@login_required(login_url='admin-sign-in')
def admin_complaints(request):
    complaints=CustomerComplaint.objects.all()
    return render(request,'admin/complaints.html',{'complaints':complaints})

@login_required(login_url='admin-sign-in')
def admin_logout(request):
    logout(request)
    return HttpResponseRedirect('/admin-signin/')