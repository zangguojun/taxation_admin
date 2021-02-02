from django.db import models


class Index(models.Model):
    id = models.CharField(max_length=8,primary_key=True,verbose_name="编号",help_text="编码规则：变长，最大长度8位。其中，一级指标占2位，二级指标2位，三级指标2位，四级指标2位。")
    index_name = models.CharField(max_length=100,verbose_name="指标名称",help_text="指标名称")
    parent_id = models.ForeignKey('self',related_name='subs',on_delete=models.CASCADE,verbose_name="上级指标",help_text="如果是一级指标，则该字段值为00")
    description = models.CharField(max_length=100,blank=True,verbose_name="指标说明",help_text="对指标解决说明（支撑点）")
    param = models.DecimalField(max_digits=5,decimal_places=4,blank=True,verbose_name="参数",help_text="ax，a为参数，值固定，小数位占4位。")
    memo = models.CharField(max_length=100,blank=True,verbose_name="备注",help_text="备注")
    class Meta:
        db_table = 'tax_index'
        verbose_name = '指标表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.index_name

class Data(models.Model):
    id = models.AutoField(max_length=8,primary_key=True,verbose_name="编号",help_text="自增")
    index_id = models.OneToOneField('Index',related_name='data',on_delete=models.CASCADE)
    city = models.CharField(max_length=20,verbose_name="地市",help_text="地市")
    season = models.CharField(max_length=20,verbose_name="季度",help_text="例如202101，2021年第一季度")
    index_value = models.DecimalField(max_digits=20,decimal_places=10,verbose_name="指标值",help_text="指标值")
    memo = models.CharField(max_length=100,verbose_name="备注",help_text="备注")
    class Meta:
        db_table = 'tax_data'
        verbose_name = '指标数据表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.index_id