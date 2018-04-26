# -*- coding: utf-8 -*-
"""
@author: Administrator
"""
import  xadmin
from xadmin import  views
from  .models import Sport
#

class SportAdmin(object):
    list_display = ['id','name','c_name']
    search_fields = ['name','c_name']
    list_filter = ['name','c_name']
    model_icon = 'fa fa-bookmark-o'

    import_excel = True



# xadmin.site.register(UserProfile,UserAdmin)
# xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(Sport,SportAdmin)