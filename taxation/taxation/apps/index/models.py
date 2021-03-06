from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class Index(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="编号",help_text="例如0,1,12,99")
    name = models.CharField(max_length=100,unique=True,verbose_name="指标名称",help_text="指标名称")
    parent = models.ForeignKey('self',related_name='subs',null=True,blank=True,
                                  on_delete=models.CASCADE,verbose_name="上级指标",
                                  help_text="如果是一级指标，则该字段值为null")
    description = models.CharField(max_length=100,blank=True,verbose_name="指标说明",help_text="对指标解决说明（支撑点）")
    param = models.DecimalField(max_digits=5,decimal_places=4,blank=True,verbose_name="参数",help_text="ax，a为参数，值固定，小数位占4位。")
    memo = models.CharField(max_length=100,blank=True,verbose_name="备注",help_text="备注")

    class Meta:
        db_table = 'tax_index'
        verbose_name = '指标表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class City(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="编号",help_text="例如0,1,12,99")
    name = models.CharField(max_length=20,verbose_name="地市",unique=True,help_text="地市")
    class Meta:
        db_table = 'tax_city'
        verbose_name = '地市表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Data(models.Model):
    id = models.AutoField(max_length=8,primary_key=True,verbose_name="编号",help_text="自增")
    city = models.ForeignKey(City,related_name='city_data',on_delete=models.PROTECT,verbose_name='地市')
    index1 = models.ForeignKey(Index,related_name='index1_data',on_delete=models.PROTECT,verbose_name='一级类别')
    index2 = models.ForeignKey(Index,related_name='index2_data',on_delete=models.PROTECT,verbose_name='二级类别')
    index3 = models.ForeignKey(Index,related_name='index3_data',on_delete=models.PROTECT,verbose_name='三级类别')
    index4 = models.ForeignKey(Index,related_name='index4_data',on_delete=models.PROTECT,verbose_name='四级类别')
    season = models.CharField(max_length=20,verbose_name="季度",help_text="例如202101，2021年第一季度")
    index_value = models.DecimalField(max_digits=20,decimal_places=10,verbose_name="指标值",help_text="指标值")
    memo = models.CharField(max_length=100,verbose_name="备注",help_text="备注")

    class Meta:
        db_table = 'tax_data'
        verbose_name = '指标数据表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.index1)+'-'+str(self.index2)+'-'+str(self.index3)+'-'+str(self.index4)