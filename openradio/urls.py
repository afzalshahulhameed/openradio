from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.edit import CreateView
from stationrunner.views import UserRegistration
from stationrunner.views import UserLogin
from stationrunner.views import UserHome
from stationrunner.views import StationCreate
from stationrunner.views import StationHome
from stationrunner.views import StationEdit
from stationrunner.views import ListStations
from stationrunner.views import ChannelCreate
from stationrunner.views import ChannelHome
from stationrunner.views import ChannelEdit
from stationrunner.views import ListChannels
#from stationrunner.views import ChannelManage


urlpatterns = patterns('',
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^', Home.as_view(), name='home'),
    url('^registration/', UserRegistration.as_view( ), name='userregistration'),
    url(r'^login/', UserLogin.as_view(), name='userlogin'),
    url(r'^(?P<pk>\d+)/', UserHome.as_view(), name='userhome'),
    #url(r'^(?P<username>\s+)/edit/', UserEdit.as_view(), name='useredit'),
    url(r'^stations/(?P<pk>\d+)/', StationHome.as_view(), name='viewstation'),
    url(r'^stations/create', StationCreate.as_view(), name='createstation'),
    url(r'^stations/edit/(?P<pk>\d+)/', StationEdit.as_view(), name='editstation'),
    url(r'^stations/list/', ListStations.as_view(), name='liststations'),    
    url(r'^channels/(?P<pk>\d+)/', ChannelHome.as_view(), name='homechannel'), #To Alen.. this is where you manage a channel
    url(r'^channels/create', ChannelCreate.as_view(), name='createchannel'),
    url(r'^channels/(?P<pk>\d+)/', ChannelHome.as_view(), name='viewchannel'),
    url(r'^channels/edit/(?P<pk>\d+)/', ChannelEdit.as_view(), name='editchannel'),
    url(r'^channels/list/', ListChannels.as_view(), name = 'listchannels'),

)       
