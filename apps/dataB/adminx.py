# -*- coding: utf-8 -*-
"""
@author: Administrator
"""
import  xadmin
from xadmin import  views
from  .models import Library
#

class LibraryAdmin(object):
    list_display = ['id','pre_word','word', 'after_word','source','meaning','partofspeech']
    search_fields = ['pre_word','word', 'after_word','source','meaning','partofspeech']
    list_filter = ['pre_word','word', 'after_word','source','meaning','partofspeech']



# xadmin.site.register(UserProfile,UserAdmin)
# xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(Library,LibraryAdmin)