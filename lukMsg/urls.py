from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='lukmsg'),
    url(r'luktotalmsg$', lukTotalMsg, name='luktotalmsg'),
    url(r'lukuser$', lukUser, name='lukuser'),
    url(r'lukservice$', lukService, name='lukservice'),
    url(r'luksensor$', lukSensor, name='luksensor'),
    url(r'lukAddUser$', lukAddUser, name='lukadduser'),
    url(r'lukServerMsg$', lukServerMsg, name='lukservermsg'),
    url(r'lukServiceMsg$', lukServiceMsg, name='lukservicermsg'),
    url(r'lukUserChange$', lukUserChange, name='lukuserchange'),
    url(r'lukAddMsg$', lukAddMsg, name='lukaddmsg'),
]