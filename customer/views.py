from django.shortcuts import render,HttpResponseRedirect
from .forms import *
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import *
from core.models import *
from designer.models import *
from designer.forms import RoomCustomizationForm
import random
from django.core.mail import send_mail
from django.conf import settings
import datetime



# Create your views here.
def customer_sign_up(request):
    if request.method=='POST':
        user_form=CustomerUserForm(request.POST)
        customer_form=CustomerForm(request.POST,request.FILES)
        if user_form.is_valid() and customer_form.is_valid():
            user=user_form.save()
            username=user.username
            email=user.email
            customer=customer_form.save(commit=False)
            customer.user=user
            customer.save()
            subject='Welcome to the Hostel'
            message='''
            Mr. '''+username+'''Welcome to our Hostel 
            You have created successfully the customer account for our Hostel Website
            Through our website you can view the hostel rooms and even book the rooms
            as well.If you have agreed to live in the hostel for more than 1 year
            then room customization feature is also available which means you can
            even customize you room based on your own ideas.

            If you have any queries please write to us at kvamshi340@gmailcom.
            '''
            customer_group,created=Group.objects.get_or_create(name='CUSTOMER')
            user.groups.add(customer_group)
            send_mail(subject,message,settings.EMAIL_HOST_USER,[email],fail_silently=True)
            return HttpResponseRedirect('/customer/signin/')
    else:
        user_form=CustomerUserForm()
        customer_form=CustomerForm()
    return render(request,'customer/signup.html',{'userform':user_form,'customerform':customer_form})




def customer_sign_in(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            request.session['next']=False
            if bool(request.POST.get('next')): 
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
        return render(request,'customer/signin.html',{'authform':auth_form})
    else:
        return HttpResponseRedirect('/afterlogin/')


@login_required(login_url='customer-sign-in')
def customer_dashboard(request):
    customer=Customer.objects.get(user=request.user)
    hostel_customer=HostelCustomer.objects.filter(customer=customer).exists()
    if hostel_customer:
        hostel_user=HostelCustomer.objects.get(customer=customer)
        return render(request,'customer/dashboard.html',{'customer':customer,'hostelcustomer':hostel_customer,'hosteluser':hostel_user or None})
    return render(request,'customer/dashboard.html',{'customer':customer,'hostelcustomer':hostel_customer}) 
    



@login_required(login_url='customer-sign-in')
def customer_room_booking(request):
    customer=Customer.objects.get(user=request.user)
    hostel_customer=HostelCustomer.objects.filter(customer=customer).exists()
    if hostel_customer:
        hostel_user=HostelCustomer.objects.get(customer=customer)
        return render(request,'customer/roombooking.html',{'customer':customer,'hostelcustomer':hostel_customer,'hosteluser':hostel_user})
    return render(request,'customer/roombooking.html',{'customer':customer,'hostelcustomer':hostel_customer})




@login_required(login_url='customer-sign-in')
def customer_room_images(request):
    room_images=Room.objects.all()
    context={
        'singleroom':room_images[0],
        'doubleroom':room_images[1],
        'tripleroom':room_images[2],
        'quadroom':room_images[3],
        'hexaroom':room_images[4],
    }
    return render(request,'customer/roomimages.html',context=context)



@login_required(login_url='customer-sign-in')
def customer_room_registration(request,id):
    room=Room.objects.get(id=id)
    room_customization=False
    total_fees=0
    room_number=0
    customer=Customer.objects.get(user=request.user)
    user=User.objects.get(id=customer.user_id)
    customer_form=CustomerForm(instance=customer)
    user_form=CustomerUserUpdateForm(instance=user)
    initial_data={
        'room':room,
    }
    if request.method=='POST':
        room_form=CustomerRoomRegistration(request.POST,initial=initial_data)
        customer_form=CustomerForm(request.POST,instance=customer)
        user_form=CustomerUserUpdateForm(request.POST,instance=user)
        if room_form.is_valid() :
            if customer_form.is_valid() and user_form.is_valid(): 
                user=user_form.save()
                customer=customer_form.save(commit=False)
                customer.user=user
                room=room_form.cleaned_data.get('room')
                if room.id==1:
                    room_number=random.randrange(100,201)
                elif room.id==2:
                    room_number=random.randrange(201,301)
                elif room.id==3:
                    room_number=random.randrange(301,401)
                elif room.id==4:
                    room_number=random.randrange(401,501)
                elif room.id==5:
                    room_number=random.randrange(601,701)

                customer.room_number=room_number
                customer.save()
                date_of_birth=room_form.cleaned_data.get('date_of_birth')
                age=room_form.cleaned_data.get('age')
                check_in=room_form.cleaned_data.get('check_in')
                duration=room_form.cleaned_data.get('duration')
                occupation=room_form.cleaned_data.get('occupation')
                work_place=room_form.cleaned_data.get('work_place')
                profession=room_form.cleaned_data.get('profession')
                caste=room_form.cleaned_data.get('caste')
                contact_number=room_form.cleaned_data.get('contact_number')
                guardian_name=room_form.cleaned_data.get('guardian_name')
                guardian_relation=room_form.cleaned_data.get('guardian_relation')
                guardian_contact_number=room_form.cleaned_data.get('guardian_contact_number')
                emergency_contact_number=room_form.cleaned_data.get('emergency_contact_number')
                permanent_address=room_form.cleaned_data.get('permanent_address')
                city=room_form.cleaned_data.get('city')
                state=room_form.cleaned_data.get('state')
                pincode=room_form.cleaned_data.get('pincode')
                if '3' in duration:
                    total_fees=room.room_fees*3
                elif '6' in duration:
                    total_fees=room.room_fees*6
                elif '9' in duration:
                    total_fees=room.room_fees*9
                elif '12' in duration:
                    total_fees=room.room_fees*12
                elif 'more' in duration:
                    total_fees=room.room_fees*12

                hostel_customer=HostelCustomer(customer=customer,room=room,room_number=room_number,date_of_birth=date_of_birth,age=age,check_in=check_in,duration=duration,occupation=occupation,work_place=work_place,profession=profession,caste=caste,contact_number=contact_number,guardian_name=guardian_name,guardian_relation=guardian_relation,guardian_contact_number=guardian_contact_number,emergency_contact_number=emergency_contact_number,permanent_address=permanent_address,city=city,state=state,pincode=pincode,total_fees=total_fees)
                hostel_customer.save()
                if 'more' in duration:
                    room_customization=True

                subject='Welcome to the Hostel'
                message1='''
                Mr. '''+request.user.username+'''
                You have successfully booked a '''+str(room.room_type)+'''
                of room number :'''+str(room_number)+'''and you have decided to 
                stay in hostel for '''+str(duration)+'''.
                Don't forget to check in the hostel on '''+str(check_in)+'''

                Welcome to Hostel Family..

                If you have any queries please write to us at kvamshi340@gmail.com
                '''

                message2='''
                Mr. '''+request.user.username+'''
                You have successfully booked a '''+str(room.room_type)+'''
                of room number'''+str(room_number)+'''and you have decided to 
                stay in hostel for '''+str(duration)+'''.
                Now you can even customize your room.please go through
                some room customization ideas from our designers or you can even 
                customize your room with your own room customization ideas.
                Don't forget to check in the hostel on '''+str(check_in)+'''

                Welcome to Hostel Family..

                If you have any queries please write to us at kvamshi340@gmail.com
                '''

                if room_customization==False:
                    send_mail(subject,message1,settings.EMAIL_HOST_USER,[request.user.email],fail_silently=True)
                if room_customization:
                    send_mail(subject,message2,settings.EMAIL_HOST_USER,[request.user.email],fail_silently=True)
                return HttpResponseRedirect('/customer/roomdetails/')
    else:
        room_form=CustomerRoomRegistration(initial=initial_data)
    return render(request,'customer/roomregistration.html',{'customerform':customer_form,'userform':user_form,'roomform':room_form})





@login_required(login_url='customer-sign-in')
def customer_room_details(request):
    customer=Customer.objects.get(user=request.user)
    user=User.objects.get(id=customer.user_id)
    hostel_customer=HostelCustomer.objects.filter(customer=customer).exists()
    hostel_user=HostelCustomer.objects.get(customer=customer)
    return render(request,'customer/roomdetails.html',{'hostelcustomer':hostel_customer,'customer':customer,'user':user,'hosteluser':hostel_user})



@login_required(login_url='customer-sign-in')   
def customer_profile(request):
    customer=Customer.objects.get(user=request.user)
    user=User.objects.get(id=customer.user_id)
    hostel_customer=HostelCustomer.objects.filter(customer=customer).exists()
    if hostel_customer:
        hostel_user=HostelCustomer.objects.get(customer=customer)
        return render(request,'customer/hostelcustomerprofile.html',{'customer':customer,'user':user,'hostelcustomer':hostel_customer,'hosteluser':hostel_user})
    return render(request,'customer/profile.html',{'customer':customer,'user':user,'hostelcustomer':hostel_customer})


@login_required(login_url='customer-sign-in')
def customer_various_customizations(request):
    customer=Customer.objects.get(user=request.user)
    hostel_customer=HostelCustomer.objects.filter(customer=customer).exists()
    rooms=RoomCustomization.objects.all()
    if hostel_customer:
        room_customized=CustomerRoom.objects.filter(customer=customer).exists()
        hostel_user=HostelCustomer.objects.get(customer=customer)
        if room_customized:
            room=CustomerRoom.objects.get(customer=customer)
            return render(request,'customer/variouscustomizations.html',{'rooms':rooms,'hostelcustomer':hostel_customer,'hosteluser':hostel_user,'roomcustomized':room_customized,'room':room})
        elif not room_customized:
            room_customized=CustomerRoomCustomization.objects.filter(customer=customer).exists()
            if room_customized:
                room_own_customized=True
                room=CustomerRoomCustomization.objects.get(customer=customer)
                return render(request,'customer/variouscustomizations.html',{'rooms':rooms,'hostelcustomer':hostel_customer,'hosteluser':hostel_user,'room':room,'roomcustomized':room_customized,'room_own_customized':room_own_customized})
            else:
                return render(request,'customer/variouscustomizations.html',{'rooms':rooms,'hostelcustomer':hostel_customer,'hosteluser':hostel_user})
        return render(request,'customer/variouscustomizations.html',{'rooms':rooms,'hostelcustomer':hostel_customer,'hosteluser':hostel_user,'roomcustomized':room_customized})
    





@login_required(login_url='customer-sign-in')
def customer_view_room(request,id):
    customer=Customer.objects.get(user=request.user)
    hostel_customer=HostelCustomer.objects.filter(customer=customer).exists()
    room=RoomCustomization.objects.get(id=id)
    if hostel_customer:
        hostel_user=HostelCustomer.objects.get(customer=customer)
        return render(request,'customer/viewroom.html',{'room':room,'hostelcustomer':hostel_customer,'hosteluser':hostel_user})
    return render(request,'customer/viewroom.html',{'room':room})




@login_required(login_url='customer-sign-in')
def customer_apply_customization(request,id):
    customer=Customer.objects.get(user=request.user)
    room=RoomCustomization.objects.get(id=id)
    room_customization=CustomerRoom(room=room,customer=customer,price=room.price,designer=room.designer)
    room_customization.save()
    subject='Welcome to the Hostel'
    message='''
    Congraulations Mr. '''+request.user.username+'''
    So you have decided to customize your room and selected a 
    customization.Our designer team will be contacting you soon.
    Incase if you want to update your customization,please update it 
    before our designer contact you.
    Hoping that you will love your customization.
    
    If you have any queries please write to us at kvamshi340@gmail.com
    '''
    send_mail(subject,message,settings.EMAIL_HOST_USER,[request.user.email],fail_silently=True)
    return HttpResponseRedirect('/customer/variouscustomizations/')



@login_required(login_url='customer-sign-in')
def customer_view_customized_room(request,id):
    customer=Customer.objects.get(user=request.user)
    hostel_customer=HostelCustomer.objects.filter(customer=customer).exists()
    room=RoomCustomization.objects.get(id=id)
    if hostel_customer:
        hostel_user=HostelCustomer.objects.get(customer=customer)
        return render(request,'customer/viewcustomizedroom.html',{'room':room,'hostelcustomer':hostel_customer,'hosteluser':hostel_user})
    return render(request,'customer/viewcustomizedroom.html',{'room':room})



@login_required(login_url='customer-sign-in')
def customer_update_customized_room(request,id):
    customer=Customer.objects.get(user=request.user)
    hostel_customer=HostelCustomer.objects.filter(customer=customer).exists()
    room=RoomCustomization.objects.get(id=id)
    if request.method=='POST':
        room_update_form=RoomCustomizationForm(request.POST,request.FILES,instance=room)
        if room_update_form.is_valid():
            left=room_update_form.cleaned_data.get('left')
            right=room_update_form.cleaned_data.get('right')
            top=room_update_form.cleaned_data.get('top')
            bottom=room_update_form.cleaned_data.get('bottom')
            front=room_update_form.cleaned_data.get('front')
            back=room_update_form.cleaned_data.get('back')
            customer_old_room=CustomerRoom.objects.get(room=room).delete()
            customer_new_room=CustomerRoomCustomization(customer=customer,left=left,right=right,top=top,bottom=bottom,front=front,back=back)
            customer_new_room.save()
            return HttpResponseRedirect('/customer/variouscustomizations/')
    else:
        room_update_form=RoomCustomizationForm(instance=room)
        if hostel_customer:
            hostel_user=HostelCustomer.objects.get(customer=customer)
            return render(request,'customer/updatecustomizedroom.html',{'roomupdateform':room_update_form,'hostelcustomer':hostel_customer,'hosteluser':hostel_user,'room':room})
    return render(request,'customer/updatecustomizedroom.html',{'roomupdateform':room_update_form,'room':room})



@login_required(login_url='customer-sign-in')
def customer_own_customization(request):
    customer=Customer.objects.get(user=request.user)
    if request.method=='POST':
        room_form=CustomerRoomCustomizationForm(request.POST,request.FILES)
        if room_form.is_valid():
            left=room_form.cleaned_data.get('left')
            right=room_form.cleaned_data.get('right')
            top=room_form.cleaned_data.get('top')
            bottom=room_form.cleaned_data.get('bottom')
            front=room_form.cleaned_data.get('front')
            back=room_form.cleaned_data.get('back')
            customer_room=CustomerRoomCustomization(customer=customer,left=left,right=right,top=top,bottom=bottom,front=front,back=back)
            customer_room.save()
            subject='Welcome to the Hostel'
            message='''
            Congraulations Mr. '''+request.user.username+'''
            So you have decided to customize your room and customized your room
            with your own ideas.We appreciated your hard work.
            Our designer team will be contacting you soon.
            Incase if you want to update your customization,please update it 
            before our designer contact you.
            Hoping that you will love your customization.
            
            If you have any queries please write to us at kvamshi340@gmail.com
            '''
            send_mail(subject,message,settings.EMAIL_HOST_USER,[request.user.email],fail_silently=True)
            return HttpResponseRedirect('/customer/viewowncustomizedroom/')
    else:
        room_form=CustomerRoomCustomizationForm()
        hostel_customer=HostelCustomer.objects.filter(customer=customer).exists()
        if hostel_customer:
            hostel_user=HostelCustomer.objects.get(customer=customer)
            return render(request,'customer/owncustomization.html',{'roomform':room_form,'hostelcustomer':hostel_customer,'hosteluser':hostel_user})
    return render(request,'customer/owncustomization.html',{'roomform':room_form})




@login_required(login_url='customer-sign-in')
def customer_view_own_customized_room(request):
    customer=Customer.objects.get(user=request.user)
    room=CustomerRoomCustomization.objects.filter(customer=customer).last()
    hostel_customer=HostelCustomer.objects.filter(customer=customer).exists()
    if hostel_customer:
        hostel_user=HostelCustomer.objects.get(customer=customer)
        return render(request,'customer/viewowncustomizedroom.html',{'room':room,'hostelcustomer':hostel_customer,'hosteluser':hostel_user})
    return render(request,'customer/viewowncustomizedroom.html',{'room':room})



@login_required(login_url='customer-sign-in')
def customer_viewing_own_customized_room(request,id):
    room=CustomerRoomCustomization.objects.get(id=id)
    customer=Customer.objects.get(user=request.user)
    hostel_customer=HostelCustomer.objects.filter(customer=customer).exists()
    if hostel_customer:
        hostel_user=HostelCustomer.objects.get(customer=customer)
        return render(request,'customer/viewingowncustomizedroom.html',{'room':room,'hostelcustomer':hostel_customer,'hosteluser':hostel_user})
    return render(request,'customer/viewingowncustomizedroom.html',{'room':room})



@login_required(login_url='customer-sign-in')
def customer_update_own_customized_room(request,id):
    room=CustomerRoomCustomization.objects.get(id=id)
    customer=Customer.objects.get(user=request.user)
    if request.method=='POST':
        room_update_form=CustomerRoomCustomizationForm(request.POST,request.FILES,instance=room)
        if room_update_form.is_valid():
            if room.designer_status:
                room.updated_room=True 
            room.save()
            room_update_form.save()
            return HttpResponseRedirect('/customer/variouscustomizations/')
    else:
        room_update_form=CustomerRoomCustomizationForm(instance=room)
        hostel_customer=HostelCustomer.objects.filter(customer=customer).exists()
        if hostel_customer:
            hostel_user=HostelCustomer.objects.get(customer=customer)
            return render(request,'customer/updateowncustomizedroom.html',{'roomupdateform':room_update_form,'hostelcustomer':hostel_customer,'hosteluser':hostel_user,'room':room})
    return render(request,'customer/updateowncustomizedroom.html',{'roomupdateform':room_update_form})



@login_required(login_url='customer-sign-in')
def customer_edit_profile(request):
    customer=Customer.objects.get(user=request.user)
    user=User.objects.get(id=customer.user_id)
    hostel_customer=HostelCustomer.objects.filter(customer=customer).exists()
    if request.method=='POST':
        customer_update_form=CustomerForm(request.POST,request.FILES,instance=customer)
        user_update_form=CustomerUserUpdateForm(request.POST,instance=user)
        if customer_update_form.is_valid() and user_update_form.is_valid():
            user=user_update_form.save()
            customer=customer_update_form.save(commit=False)
            customer.user=user
            customer.save()
            return HttpResponseRedirect('/customer/profile/')
    else:
        customer_update_form=CustomerForm(instance=customer)
        user_update_form=CustomerUserUpdateForm(instance=user)
        if hostel_customer:
            hostel_user=HostelCustomer.objects.get(customer=customer)
            return render(request,'customer/editprofile.html',{'customer':customer,'customerupdateform':customer_update_form,'userupdateform':user_update_form,'hostelcustomer':hostel_customer,'hosteluser':hostel_user})
    return render(request,'customer/editprofile.html',{'customer':customer,'customerupdateform':customer_update_form,'userupdateform':user_update_form,'hostelcustomer':hostel_customer})



@login_required(login_url='customer-sign-in')
def hostel_customer_profile(request):
    customer=Customer.objects.get(user=request.user)
    user=User.objects.get(id=customer.user_id)
    hostel_customer=HostelCustomer.objects.filter(customer=customer).exists()
    if hostel_customer:
        hostel_user=HostelCustomer.objects.get(customer=customer)
        return render(request,'customer/hostelcustomerprofile.html',{'user':user,'customer':customer,'hostelcustomer':hostel_customer,'hosteluser':hostel_user})


@login_required(login_url='customer-sign-in')
def hostel_customer_edit_profile(request):
    customer=Customer.objects.get(user=request.user)
    user=User.objects.get(id=customer.user_id)
    hostel_customer=HostelCustomer.objects.filter(customer=customer).exists()
    if hostel_customer:
        hostel_user=HostelCustomer.objects.get(customer=customer)
        if request.method=='POST':
            customer_update_form=CustomerForm(request.POST,request.FILES,instance=customer)
            user_update_form=CustomerUserUpdateForm(request.POST,instance=user)
            hostel_user_update_form=HostelCustomerUpdateform(request.POST,instance=hostel_user)
            if customer_update_form.is_valid() and user_update_form.is_valid() and hostel_user_update_form.is_valid():
                user=user_update_form.save()
                customer=customer_update_form.save(commit=False)
                customer.user=user
                customer.save()
                hostel=hostel_user_update_form.save()
            return HttpResponseRedirect('/customer/hostelcustomerprofile/')
        else:
            customer_update_form=CustomerForm(instance=customer)
            user_update_form=CustomerUserUpdateForm(instance=user)
            hostel_user_update_form=HostelCustomerUpdateform(instance=hostel_user)
        return render(request,'customer/hostelcustomereditprofile.html',{'hostelcustomer':hostel_customer,'hosteluser':hostel_user,'userupdateform':user_update_form,'customerupdateform':customer_update_form,'hosteluserupdateform':hostel_user_update_form})



@login_required(login_url='customer-sign-in')
def customer_complaint(request):
    customer=Customer.objects.get(user=request.user)
    if request.method=='POST':
        complaint_form=CustomerComplaintForm(request.POST)
        if complaint_form.is_valid():
            complaint=complaint_form.cleaned_data.get('complaint')
            hostelcustomer=HostelCustomer.objects.get(customer=customer)
            customer_complaint=CustomerComplaint(hostel_customer=hostelcustomer,complaint=complaint)
            customer_complaint.save()
            return HttpResponseRedirect('/customer/complaint/')
    else:
        hostel_customer=HostelCustomer.objects.filter(customer=customer).exists()
        if hostel_customer:
            hostel_user=HostelCustomer.objects.get(customer=customer)
            complaint_form=CustomerComplaintForm()
            return render(request,'customer/complaint.html',{'hostelcustomer':hostel_customer,'hosteluser':hostel_user,'complaintform':complaint_form})



@login_required(login_url='customer-sign-in')
def customer_change_password(request):
    customer=Customer.objects.get(user=request.user)
    hostel_customer=HostelCustomer.objects.filter(customer=customer).exists()
    if request.method=='POST':
        password_form=PasswordChangeForm(user=request.user,data=request.POST)
        if password_form.is_valid():
            password_form.save()
            date=datetime.datetime.now()
            update_session_auth_hash(request,password_form.user)
            subject='Welcome to the Hostel'
            message='''
            Mr. '''+request.user.username+'''
            You have successfully changed your password.
            on  '''+str(date)+''' .
            
            If you any queries please write to us at kvamshi340@gmailcom'''
            send_mail(subject,message,settings.EMAIL_HOST_USER,[request.user.email],fail_silently=True)
            return HttpResponseRedirect('/customer/profile/')
    else:
        password_form=PasswordChangeForm(user=request.user)
        if hostel_customer:
            hostel_user=HostelCustomer.objects.get(customer=customer)
            return render(request,'customer/changepassword.html',{'passwordform':password_form,'hostelcustomer':hostel_customer,'hosteluser':hostel_user})
    return render(request,'customer/changepassword.html' ,{'passwordform':password_form,'hostelcustomer':hostel_customer})



@login_required(login_url='customer-sign-in')
def customer_logout(request):
    logout(request)
    return HttpResponseRedirect('/customer/signin/')
