from django.conf.urls import include, url
from dashboard import views

urlpatterns = [
	url(r'^$', views.index, name='dashboard-home'),
	url(r'^admin_profile/$', views.admin_profile, name='dashboard-admin-profile'),
	url(r'^icons/$', views.icons, name='dashboard-icons'),
	url(r'^tables/$', views.tables, name='dashboard-tables'),
	url(r'^notifs/$', views.notifications, name='dashboard-notifs'),
	url(r'^upgrade/$', views.upgrade, name='dashboard-upgrade'),
]