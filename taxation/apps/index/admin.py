from django import forms
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from .models import Index,City,Data


admin.AdminSite.site_header = '河南省税务大数据管理'
admin.AdminSite.site_title = '河南省税务大数据管理系统'

@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    list_display = ('id','name')
    search_fields = ('name',)
    list_per_page = 10



class DateaForm(forms.ModelForm):
    class Meta:
        widgets = {
            'province': forms.Select(),
            'city': forms.Select(),
            'district': forms.Select()
        }

@admin.register(Data)
class DataAdmin(ImportExportModelAdmin):
    form = DateaForm
    list_display = ('id','city', 'index4','season','index_value')
    search_fields = ('city__name','index4__name','season',)
    list_filter = ('city','season')
    list_per_page = 10
    change_form_template = 'data.html'

@admin.register(Index)
class IndexAdmin(ImportExportModelAdmin):
    list_display = ('id','name', 'parent','param')
    search_fields = ('name','parent__name')
    list_filter = ('parent',)
    list_per_page = 10

