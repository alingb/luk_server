from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='lukmsg'),
    url(r'/luktotalmsg$', lukTotalMsg, name='luktotalmsg'),
    url(r'/lukuser$', lukUser, name='lukuser'),
    url(r'/lukservice$', lukService, name='lukservice'),
    url(r'/luksensor$', lukSensor, name='luksensor'),
]