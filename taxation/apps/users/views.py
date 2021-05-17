from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import date

from .models import User

class UserTotalCountView(APIView):
    # 指定管理员权限

    def get(self,request):
        # 获取当前日期
        now_date=date.today()
        # 获取所有用户总数
        count= User.objects.all().count()
        return Response({
            'count':count,
            'date':now_date
        })