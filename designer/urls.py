from django.urls import path
from . import views



urlpatterns = [
    path('signup/',views.designer_sign_up,name='designer-sign-up'),
    path('signin/',views.designer_sign_in,name='designer-sign-in'),
    path('dashboard/',views.designer_dashboard,name='designer-dashboard'),
    path('profile/',views.designer_profile,name='designer-profile'),
    path('notapproved/',views.designer_not_approved,name='designer-not-approved'),

    path('roomcustomizationform/',views.designer_room_customization_form,name='designer-room-customization-form'),
    path('roomcustomization/',views.designer_room_customization,name='designer-room-customization'),
    path('roomprice/<int:id>/',views.designer_room_price,name='designer-room-price'),
    path('roomupdate/<int:id>/',views.designer_room_update,name='designer-room-update'),
    path('roomdelete/<int:id>/',views.designer_room_delete,name='designer-room-delete'),
    path('roomscustomized/',views.designer_rooms_customized,name='designer-rooms-customized'),
    path('roomorders/',views.designer_room_orders,name='designer-room-orders'),
    path('viewroom/<int:id>/',views.designer_view_room,name='designer-view-room'),
    path('viewingcustomerorderroom/<int:id>/',views.designer_viewing_customer_order_room,name='designer-viewing-customer-order-room'),
    path('customerowncustomizedrooms/',views.designer_customer_own_customized_rooms,name='designer-customer-own-customized-rooms'),
    path('viewingcustomerowncustomizedroom/<int:id>/',views.designer_viewing_customer_own_customized_room,name='designer-viewing-customer-own-customized-room'),
    path('takingcustomerowncustomizedroomorder/<int:id>/',views.designer_taking_customer_own_customized_room_order,name='designer-taking-customer-own-customized-room-order'),
    path('roompricecustomerroomupdate/<int:id>/',views.designer_room_price_customer_room_update,name='designer-room-price-customer-room-update'),

    
    path('editprofile/',views.designer_edit_profile,name='designer-edit-profile'),
    path('changepassword/',views.designer_change_password,name='designer-change-password'),

    path('logout/',views.designer_logout,name='designer-logout'),
]
