# -*- coding: utf-8 -*-
"""
@author: Administrator
"""
import  xadmin
from xadmin import  views
from  .models import Xiangmu
#

class  XiangmuAdmin(object):
    list_display = ['id','name', ]
    search_fields = ['id','name',]
    list_filter = ['id','name',]



# xadmin.site.register(UserProfile,UserAdmin)
# xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(Xiangmu,XiangmuAdmin)