# -*- coding: utf-8 -*-
"""
@author: Administrator
"""
import  xadmin
from xadmin import  views
from  .models import Library
#

class LibraryAdmin(object):
    list_display = ['pre_word','word', 'after_word']
    search_fields = ['pre_word','word', 'after_word']
    list_filter = ['pre_word','word', 'after_word']



# xadmin.site.register(UserProfile,UserAdmin)
# xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(Library,LibraryAdmin)