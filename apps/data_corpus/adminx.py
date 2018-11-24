# -*- coding: utf-8 -*-
"""
@author: Administrator
"""
import  xadmin
import xlrd
from xadmin import  views
from  .models import Library
#

class LibraryAdmin(object):
    list_display = ['id','pre_word','word', 'after_word','meaning','partofspeech','sport','source']
    search_fields = ['pre_word','word', 'after_word','source','meaning','partofspeech','sport']
    list_filter = ['pre_word','word', 'after_word','source','meaning','partofspeech','sport']
    model_icon = 'fa fa-list-alt'

    import_excel = True
    def post(self,request,*args,**kwargs):
        if 'excel' in request.FILES:
            wb = xlrd.open_workbook(filename=None, file_contents=request.FILES['excel'].read())
            table = wb.sheets()[0]
            row = table.nrows
            sql_list = []
            sport_id_list = []
            for i in range(1, row):
                col = table.row_values(i)
                sql = Library(
                    pre_word=col[0],
                    word=col[1],
                    after_word=col[2],
                    partofspeech=col[3],
                    meaning=col[4],
                    sport_id=col[5],
                )
                sql_list.append(sql)
            Library.objects.bulk_create(sql_list)
        return super(LibraryAdmin,self).post(request,args,kwargs)


# xadmin.site.register(UserProfile,UserAdmin)
# xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(Library,LibraryAdmin)