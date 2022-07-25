from django.shortcuts import render,HttpResponseRedirect
from .forms import *
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.mail import send_mail
from django.conf import settings
import datetime
from customer.models import CustomerRoom, CustomerRoomCustomization, HostelCustomer


# Create your views here.
def designer_sign_up(request):
    if request.method=='POST':
        designer_form=DesignerForm(request.POST,request.FILES)
        user_form=DesignerUserForm(request.POST)
        if designer_form.is_valid() and user_form.is_valid():
            user=user_form.save()
            username=user.username
            email=user.email
            designer=designer_form.save(commit=False)
            designer.user=user
            designer.save()
            subject='Welcome to the Hostel'
            message='''
            Mr. '''+username+'''Welcome to our Hostel 
            You have created successfully the designer account for our Hostel Website.
            Through our Website you can customize the rooms with your 
            innovating ideas.You can add your customization ideas in your designer
            account once your account is approved by the admin.
            This is the begining of your desginer career.All the best.

            Welcome to The Hostel Family.

            If you have any queries please write to us at kvamshi340@gmailcom .
            '''
            designer_group,created=Group.objects.get_or_create(name='DESIGNER')
            user.groups.add(designer_group)
            send_mail(subject,message,settings.EMAIL_HOST_USER,[email],fail_silently=True)
            return HttpResponseRedirect('/designer/signin/')
    else:
        designer_form=DesignerForm()
        user_form=DesignerUserForm()
    return render(request,'designer/signup.html',{'designerform':designer_form,'userform':user_form})



def designer_sign_in(request):
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
        return render(request,'designer/signin.html',{'authform':auth_form})
    else:
        return HttpResponseRedirect('/afterlogin/')




def designer_not_approved(request):
    return render(request,'designer/notapproved.html')

@login_required(login_url='designer-sign-in')  
def designer_dashboard(request):
    designer=Designer.objects.get(user=request.user)
    return render(request,'designer/dashboard.html',{'designer':designer})

@login_required(login_url='designer-sign-in')
def designer_profile(request):
    designer=Designer.objects.get(user=request.user)
    user=User.objects.get(id=designer.user_id)
    return render(request,'designer/profile.html',{'designer':designer,'user':user})


@login_required(login_url='designer-sign-in')
def designer_room_customization_form(request):
    designer=Designer.objects.get(user=request.user)
    if request.method=='POST':
        room_form=RoomCustomizationForm(request.POST,request.FILES)
        if room_form.is_valid():
            left=room_form.cleaned_data.get('left')
            right=room_form.cleaned_data.get('right')
            top=room_form.cleaned_data.get('top')
            bottom=room_form.cleaned_data.get('bottom')
            front=room_form.cleaned_data.get('front')
            back=room_form.cleaned_data.get('back')
            room_customization=RoomCustomization(designer=designer,left=left,right=right,top=top,bottom=bottom,front=front,back=back)
            room_customization.save()
            return HttpResponseRedirect('/designer/roomcustomization/')
    else:
        room_form=RoomCustomizationForm()
    return render(request,'designer/roomcustomizationform.html',{'roomform':room_form})



@login_required(login_url='designer-sign-in')
def designer_room_customization(request):
    designer=Designer.objects.get(user=request.user)
    room=RoomCustomization.objects.filter(designer=designer).last()
    return render(request,'designer/roomcustomization.html',{'room':room})


@login_required(login_url='designer-sign-in')
def designer_room_price(request,id):
    room=RoomCustomization.objects.get(id=id)
    if request.method=='POST':
        room_price_form=RoomPriceThemeForm(request.POST)
        if room_price_form.is_valid():
            price=room_price_form.cleaned_data.get('price')
            theme=room_price_form.cleaned_data.get('theme')
            room.price=price
            room.theme=theme
            room.save()
            return HttpResponseRedirect('/designer/roomscustomized/')
    else:
        room_price_form=RoomPriceThemeForm(instance=room)
    return render(request,'designer/roomprice.html',{'roompriceform':room_price_form})


@login_required(login_url='designer-sign-in')
def designer_room_update(request,id):
    room=RoomCustomization.objects.get(id=id)
    if request.method=='POST':
        room_update_form=RoomCustomizationForm(request.POST,request.FILES,instance=room)
        if room_update_form.is_valid():
            room_update_form.save()
            return HttpResponseRedirect('/designer/roomcustomization/')
    else:
        room_update_form=RoomCustomizationForm(instance=room)
    return render(request,'designer/roomcustomizationupdate.html',{'roomupdateform':room_update_form,'room':room})




@login_required(login_url='designer-sign-in')
def designer_room_delete(request,id):
    room=RoomCustomization.objects.get(id=id).delete()
    return HttpResponseRedirect('/designer/roomcustomizationform/')



@login_required(login_url='designer-sign-in')
def designer_rooms_customized(request):
    designer=Designer.objects.get(user=request.user)
    rooms=RoomCustomization.objects.filter(designer=designer)
    return render(request,'designer/roomscustomized.html',{'rooms':rooms})



@login_required(login_url='designer-sign-in')
def designer_room_orders(request):
    designer=Designer.objects.get(user=request.user)
    my_rooms=CustomerRoom.objects.filter(designer=designer)
    customer_rooms=CustomerRoomCustomization.objects.filter(designer=designer,designer_status=True)
    return render(request,'designer/roomorders.html',{'myrooms':my_rooms,'customerrooms':customer_rooms})


@login_required(login_url='designer-sign-in')
def designer_customer_own_customized_rooms(request):
    rooms=CustomerRoomCustomization.objects.filter(designer_status=False)
    return render(request,'designer/customerowncustomizedrooms.html',{'rooms':rooms})


@login_required(login_url='designer-sign-in')
def designer_viewing_customer_own_customized_room(request,id):
    room=CustomerRoomCustomization.objects.get(id=id)
    return render(request,'designer/viewingcustomerowncustomizedroom.html',{'room':room})


@login_required(login_url='designer-sign-in')
def designer_taking_customer_own_customized_room_order(request,id):
    designer=Designer.objects.get(user=request.user)
    room=CustomerRoomCustomization.objects.get(id=id)
    if request.POST:
        room_price_form=RoomPriceForm(request.POST)
        if room_price_form.is_valid():
            price=room_price_form.cleaned_data.get('price')
            room.designer_status=True
            room.designer=designer
            room.price=price
            room.save()
            subject='Welcome to the Hostel'
            message='''
            Congrtulations Mr. '''+str(room.customer.user)+ '''
            Mr. '''+request.user.username+''' decided to customize your 
            room for Rs.'''+str(price)+'''/-  .Very soon he will be contacting you.
            Hoping that you will love your room customization.

            If you have any queries please write to us at kvamshi340@gmail.com 
            
            '''
            send_mail(subject,message,settings.EMAIL_HOST_USER,[room.customer.user.email],fail_silently=True)
            return HttpResponseRedirect('/designer/roomorders/')
    else:
        room_price_form=RoomPriceForm()
    return render(request,'designer/takingcustomerowncustomizedroom.html',{'roompriceform':room_price_form})
    


@login_required(login_url='designer-sign-in')
def designer_room_price_customer_room_update(request,id):
    room=CustomerRoomCustomization.objects.get(id=id)
    if request.method=='POST':
        room_price_form=RoomPriceForm(request.POST,instance=room)
        if room_price_form.is_valid():
            price=room_price_form.cleaned_data.get('price')
            room.price=price
            room.updated_room=False
            room.save()
            return HttpResponseRedirect('/designer/roomorders/')
    else:
        room_price_form=RoomPriceForm(instance=room)
    return render(request,'designer/roompricecustomerroomupdate.html',{'roompriceform':room_price_form})



@login_required(login_url='designer-sign-in')
def designer_viewing_customer_order_room(request,id):
    room=RoomCustomization.objects.get(id=id)
    return render(request,'designer/viewingcustomerorderroom.html',{'room':room})


@login_required(login_url='designer-sign-in')
def designer_view_room(request,id):
    room=RoomCustomization.objects.get(id=id)
    return render(request,'designer/viewroomcustomization.html',{'room':room})



@login_required(login_url='designer-sign-in')
def designer_edit_profile(request):
    designer=Designer.objects.get(user=request.user)
    user=User.objects.get(id=designer.user_id)
    if request.method=='POST':
        designer_update_form=DesignerUpdateForm(request.POST,request.FILES,instance=designer)
        user_update_form=DesignerUserUpdateForm(request.POST,instance=user)
        if designer_update_form.is_valid() and user_update_form.is_valid():
            user=user_update_form.save()
            designer=designer_update_form.save(commit=False)
            designer.user=user
            designer.save()
            return HttpResponseRedirect('/designer/profile/')
    else:
        designer_update_form=DesignerUpdateForm(instance=designer)
        user_update_form=DesignerUserUpdateForm(instance=user)
    return render(request,'designer/editprofile.html',{'designerupdateform':designer_update_form,'userupdateform':user_update_form})



@login_required(login_url='designer-sign-in')
def designer_change_password(request):
    date=datetime.datetime.now()
    if request.method=='POST':
        password_form=PasswordChangeForm(user=request.user,data=request.POST)
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request,password_form.user)
            subject='Welcome to the Hostel'
            message='''
            Mr. '''+request.user.username+'''
            You have successfully changed your password.
            on  '''+str(date)+''' .
            
            If you any queries please write to us at kvamshi340@gmailcom '''
            send_mail(subject,message,settings.EMAIL_HOST_USER,[request.user.email],fail_silently=True)
            return HttpResponseRedirect('/designer/profile/')
    else:
        password_form=PasswordChangeForm(user=request.user)
    return render(request,'designer/changepassword.html',{'passwordform':password_form})



@login_required(login_url='designer-sign-in')
def designer_logout(request):
    logout(request)
    return HttpResponseRedirect('/designer/signin/')