from django.urls import path
from . import views


urlpatterns = [
    path('signup/',views.customer_sign_up,name='customer-sign-up'),
    path('signin/',views.customer_sign_in,name='customer-sign-in'),
    path('dashboard/',views.customer_dashboard,name='customer-dashboard'),

    path('roombooking/',views.customer_room_booking,name='customer-room-booking'),
    path('roomimages/',views.customer_room_images,name='customer-room-images'),
    path('roomregistration/<int:id>/',views.customer_room_registration,name='customer-room-registration'),
    path('roomdetails/',views.customer_room_details,name='customer-room-details'),


    path('variouscustomizations/',views.customer_various_customizations,name='customer-various-customizations'),
    path('viewroom/<int:id>/',views.customer_view_room,name='customer-view-room'),
    path('applycustomization/<int:id>/',views.customer_apply_customization,name='customer-apply-customization'),
    path('viewcustomizedroom/<int:id>/',views.customer_view_customized_room,name='customer-view-customized-room'),
    path('updatecustomizedroom/<int:id>/',views.customer_update_customized_room,name='customer-update-customized-room'),


    path('owncustomization/',views.customer_own_customization,name='customer-own-customization'),
    path('viewowncustomizedroom/',views.customer_view_own_customized_room,name='customer-view-own-customized-room'),
    path('updateowncustomizedroom/<int:id>/',views.customer_update_own_customized_room,name='customer-update-own-customized-room'),
    path('viewingowncustomizedroom/<int:id>/',views.customer_viewing_own_customized_room,name='customer-viewing-own-customized-room'),


    path('complaint/',views.customer_complaint,name='customer-complaint'),

    path('profile/',views.customer_profile,name='customer-profile'),
    path('editprofile/',views.customer_edit_profile,name='customer-edit-profile'),
    path('changepassword/',views.customer_change_password,name='customer-change-password'),

    path('hostelcustomerprofile/',views.hostel_customer_profile,name='hostel-customer-profile'),
    path('hostelcustomereditprofile/',views.hostel_customer_edit_profile,name='hostel-customer-edit-profile'),



    path('logout/',views.customer_logout,name='customer-logout'),

]
