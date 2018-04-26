# -*- coding: utf-8 -*-
"""
@author: Administrator
"""
import  xadmin
from xadmin import  views
from  .models import XunlianDate, XunlianSh
#

class  XunlianDateAdmin(object):
    list_display = ['xingming','riqi','xiangmu' ]
    search_fields = ['xingming','riqi','xiangmu' ]
    list_filter = ['xingming','riqi','xiangmu' ]

class  XunlianShAdmin(object):
    list_display = ['xingming','riqi','gaotong']
    search_fields = ['xingming','riqi','gaotong']
    list_filter = ['xingming','riqi','gaotong']
    data_charts = {
            "user_count": {'title': u"训练-生化", "x-field": "riqi", "y-field": ("gaotong", ), "order": ('riqi',)},
            # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
        }

# xadmin.site.register(UserProfile,UserAdmin)
# xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(XunlianDate,XunlianDateAdmin)
xadmin.site.register(XunlianSh,XunlianShAdmin)