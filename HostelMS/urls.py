"""HostelMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from core import views
from django.views.i18n import JavaScriptCatalog


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('navbar/',views.navbar,name='navbar'),
    path('whatsnew/',views.whats_new,name='whatsnew'),
    path('afterlogin/',views.afterlogin,name='afterlogin'),
    path('jsiq87/',JavaScriptCatalog.as_view(),name='js-catalog'),




    path('customer/',include('customer.urls')),
    path('designer/',include('designer.urls')),




    #admin urls
    path('admin-signin/',views.admin_sign_in,name='admin-sign-in'),
    # path('admin-dashboard/',views.admin_dashboard,name='admin-dashboard'),
    path('admin-logout/',views.admin_logout,name='admin-logout'),
    path('admin-hostel-customers/',views.admin_hostel_customers,name='admin-hostel-customers'),
    path('admin-upcoming-hostel-customers/',views.admin_upcoming_hostel_customers,name='admin-upcoming-hostel-customers'),
    path('admin-approving-customer/<int:id>/',views.admin_approving_customer,name='admin-approving-customer'),
    path('admin-rejecting-customer/<int:id>/',views.admin_rejecting_customer,name='admin-rejecting-customer'),
    path('admin-customer-view-details/<int:id>/',views.admin_customer_view_details,name='admin-customer-view-details'),
    path('admin-pending-designers/',views.admin_pending_designers,name='admin-pending-designers'),
    path('admin-approving-designer/<int:id>/',views.admin_approving_designer,name='admin-approving-designer'),
    path('admin-rejecting-designer/<int:id>/',views.admin_rejecting_designer,name='admin-rejecting-designer'),
    path('admin-approved-designers/',views.admin_approved_designers,name='admin-approved-designers'),
    path('admin-designer-customized-rooms/<int:id>/',views.admin_desginer_customized_rooms,name='admin-designer-customized-rooms'),
    path('admin-designer-view-room/<int:id>/',views.admin_designer_view_room,name='admin-designer-view-room'),
    path('admin-add-worker-details/',views.admin_add_worker_details,name='admin-add-worker-details'),
    path('admin-worker-details/',views.admin_worker_details,name='admin-worker-details'),
    path('admin-worker-edit/<int:id>/',views.admin_worker_edit,name='admin-worker-edit'),
    path('admin-worker-delete/<int:id>/',views.admin_worker_delete,name='admin-worker-delete'),
    path('admin-rules/',views.admin_rules,name='admin-rules'),
    path('admin-menu/',views.admin_menu,name='admin-menu'),
    path('admin-menu-edit/<int:id>/',views.admin_menu_edit,name='admin-menu-edit'),
    path('admin-complaints/',views.admin_complaints,name='admin-complaints')


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


