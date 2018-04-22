from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^abtus/$', views.aboutus, name='aboutus'),
url(r'^checked/(?P<id>\d+)/$', views.done, name='done'),
url(r'^home/(?P<area>.+)/(?P<loc>.+)/(?P<id>\d+)/$', views.filters, name='form2'),
url(r'^home/(?P<problem>.+)/(?P<discuss_id>\d+)_discuss/$', views.discuss),
    url(r'^(?P<user1>.+)/profile/$', views.profile),
url(r'^home/(?P<area>.+)/(?P<loc>.+)/(?P<prob>.+)/$', views.spec_problem, name='form2'),
    url(r'^home/(?P<area>.+)/(?P<loc>.+)/$', views.spec_locality, name='form2'),



    #url(r'^$', views.login,name="login"),
    #ul(r'^login-home$', views.login1,name="login-home"),
    url(r'^forum_page/$', views.forum, name='forum'),
url(r'^home/logout/$', views.logout_view, name='logout'),
url(r'^simplemap/$', views.simple, name='simple'),
url(r'^checked1/$', views.checked, name='simple'),



    url(r'^home/guest/$', views.goback, name='guest'),
    url(r'^register/$', views.register, name='register'),


    url(r'^register_once/$', views.register_once, name='register_once'),

    url(r'^login1/$', views.user_login, name='login'),
    url(r'^problem/(?P<problem1>.+)/all_json_models1/$', views.all_json_models1 ),
    url(r'^home/$', views.home, name='login'),
    url(r'^home/(?P<problem>.+)/$', views.form3, name='form2'),
    url(r'^area/(?P<area>.+)/all_json_models/$', views.all_json_models ),
    url(r'^account/reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', views.PasswordResetConfirmView.as_view(),name='reset_password_confirm'),
    url(r'^like/(?P<like>\d+)/all_json_model/$', views.all_json_model ),
    url(r'^like/(?P<like>\d+)/all_json_models2/$', views.all_json_models2 ),
url(r'^like/(?P<like>\d+)/all_json_models3/(?P<problem>.+)/$', views.all_json_models3 ),
    url(r'^account/reset_password', views.ResetPasswordRequestView.as_view(), name="reset_password"),



]