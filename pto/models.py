# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_text
#from twisted.persisted.aot import Instance
#from fileinput import filename


#Обьекты газовой сети   -----------------------------------------------------------------------

#Основания приема на Техническое обслуживания
class Osnovanie(models.Model):
    ge_osnovanie = models.CharField('Основание', max_length=100)
    
    class Meta:
        verbose_name = u'Основание'
        verbose_name_plural = u'Основания приема на Техническое обслуживания'
        
    def __str__(self):
        return self.ge_osnovanie


#Обьекты газовой сети
class Objekt(models.Model):
    ge_osnovanie = models.ForeignKey('Osnovanie', verbose_name = 'Основание')
    ge_nomereestr = models.CharField('Архивный номер', max_length=10)
    ge_nomeinvent = models.CharField('Инвентарный номер', max_length=10,
                                     default = '-')
    ge_naimenovanie = models.CharField('Название', max_length=100)
    ge_naimenovaniekr = models.CharField('Краткое название', max_length=100)
    ge_tobject = models.ForeignKey('Spr_tobject', verbose_name = 'Тип обьекта')
    ge_naznachenie = models.CharField('Назначение', max_length=100,
                                      default = '-')
    ge_godpostr = models.PositiveSmallIntegerField('Год постройки', default = 0)
    ge_godvvoda = models.PositiveSmallIntegerField('Год ввода в экспл.', default = 0)
    ge_opisanie = models.TextField('Описание', default = '-')
    ge_gradsituazia = models.CharField('Градостроительная ситуация', max_length=200,
                                       default = '-')
    ge_izmertel = models.CharField('Единица измерения', max_length=100, default = '-')
    ge_kolizmertel = models.DecimalField('Количество' ,max_digits=15, decimal_places=2,
                                         default = 0)
    ge_plzastr = models.DecimalField('Площадь застройки' ,max_digits=15, decimal_places=2,
                                     default = 0)
    ge_nombuhucset = models.CharField('Инвентарный номер бух. учета', max_length=10,
                                      default = '-')
    ge_stbalans = models.DecimalField('Балансовая стоимость' ,max_digits=15, decimal_places=2,
                                      default = 0)
    ge_databalans = models.DateField('Дата баланс. стоимости', null = True, blank = True)
    ge_proekt = models.CharField('Шифр проекта', max_length=10, default = '-')
    ge_kadastrnomer = models.CharField('Кадастровый номер', max_length=10, default = '-')
    ge_kadastrnomerdata = models.DateField('Дата постановки на кадастр. учет', null = True,
                                           blank = True)
    ge_techuchetnomer = models.CharField('Номер тех. паспорта', max_length=10, default = '-')
    ge_techuchetdata = models.DateField('Дата постановки на тех. учет', null = True, blank = True)
    ge_gosregister = models.CharField('Номер свидетельства гос. регистрации', max_length=20,
                                      default = '-')
    ge_gosregisterdata = models.DateField('Дата свидетельства гос. регистрации', null = True,
                                          blank = True)
    ge_primech = models.TextField('Примечание', default = '-')
    ge_dateobsled = models.DateField('Дата обследования', null = True, blank = True)
    ge_ispolnitel = models.CharField('Исполнитель', max_length=20, default = '-')
    
    class Meta:
        verbose_name = 'Обьект'
        verbose_name_plural = 'Обьекты газовой сети'
    
    def __str__(self):
        return "%s" %(self.ge_naimenovaniekr)

#Точка обьекта    
class PointObjekt(models.Model):
    ge_objekt = models.ForeignKey('Objekt', verbose_name = 'Обьект')
    ge_naimen = models.CharField('Наименование ', max_length=30)
    ge_nomer = models.CharField('Номер (литера) ', max_length=20)
    
    class Meta:
        verbose_name = 'Точка обьекта'
        verbose_name_plural = 'Точки обьекта'
       
    def __str__(self):
        return "%s %s %s" %(self.ge_naimen, self.ge_nomer, self.ge_objekt)

#Регулирующее устройство    
class Regulir_ustroystvo(PointObjekt):
    ge_regulir_ustroystvo = models.ForeignKey('Spr_regulir_ustroystvo', verbose_name = 
                                              'Регулирующее устройство')
    
    class Meta:
        verbose_name = 'Регулирующее устройство'
        verbose_name_plural = 'Регулирующее устройство'
                
    def save(self, force_insert=False, force_update=False, using=None, 
        update_fields=None):
        self.ge_naimen = 'Регулирующее устройство'
        return PointObjekt.save(self, force_insert=force_insert, force_update=force_update,
                                 using=using, update_fields=update_fields)
            
    def __str__(self):
        return self.ge_nomer

#Задвижки(краны)  
class Tap(PointObjekt):
    ge_tap = models.ForeignKey('Spr_tap', verbose_name = 'Отключающие устройства')
    
    class Meta:
        verbose_name = 'Отключающее устройство'
        verbose_name_plural = 'Отключающие устройства'
                
    def save(self, force_insert=False, force_update=False, using=None, 
        update_fields=None):
        self.ge_naimen = 'Отключающее устройство'
        return PointObjekt.save(self, force_insert=force_insert, force_update=force_update,
                                 using=using, update_fields=update_fields)
            
    def __str__(self):
        return self.ge_nomer


#Узлы газовой сети    
class Uzel(PointObjekt):
    ge_uzel = models.ForeignKey('Spr_uzel', verbose_name = 'Узел')
    
    class Meta:
        verbose_name = 'Узел газовой сети'
        verbose_name_plural = 'Узлы газовой сети'
                
    def save(self, force_insert=False, force_update=False, using=None, 
        update_fields=None):
        self.ge_naimen = 'Узел газовой сети'
        return PointObjekt.save(self, force_insert=force_insert, force_update=force_update, 
                                using=using, update_fields=update_fields)
            
    def __str__(self):
        return self.ge_nomer
#Труба  
class Pipe(models.Model):
    ge_objekt = models.ForeignKey('objekt', verbose_name = 'Обьект')
    ge_liter = models.CharField('Номер (литера) ', max_length=20)
    ge_naimen = models.CharField('Наименование ', max_length=100, default = '-')
    ge_godvvoda = models.PositiveSmallIntegerField('Год ввода в экспл.', default = 0)
    ge_material = models.ForeignKey('Spr_material', verbose_name = 'Материал')
    ge_pressure = models.ForeignKey('Spr_pressure', verbose_name = 'Давление')
    ge_dlina = models.DecimalField('Протяженность всего' ,max_digits=15, decimal_places=2)
    ge_dlinavl = models.DecimalField('Протяженность надземных линий' ,max_digits=15,
                                     decimal_places=2, default = 0)
    ge_dlinapl = models.DecimalField('Протяженность подземных линий' ,max_digits=15,
                                     decimal_places=2, default = 0)
    ge_glubina = models.DecimalField('Глубина заложения' ,max_digits=9, decimal_places=2,
                                     default = 0)
    ge_iznos = models.PositiveSmallIntegerField('Износ', default = 0)
    ge_iznosfakt = models.PositiveSmallIntegerField('Износ фактический', default = 0)
    ge_oporamaterial = models.CharField('Материал опор (колодцев)', max_length=100,
                                        default = '-')
    ge_oporakolvo = models.PositiveSmallIntegerField('Количество опор (колодцев)',
                                                     default = 0)
    ge_primech = models.TextField('Примечание', default = '-')
    
    class Meta:
        verbose_name = 'Труба '
        verbose_name_plural = 'Трубы '
        
    def __str__(self):
        return "%s %s"%(self.ge_liter, self.ge_naimen)

#Трасса
class Track(models.Model):
    ge_objekt = models.ForeignKey('objekt', verbose_name = 'Обьект')
    ge_startPoint = models.ForeignKey('PointObjekt', verbose_name = 'Начальная точка',
                                      related_name= 'startPoint')
    ge_pipe = models.ForeignKey('Pipe', verbose_name = 'Труба')
    ge_endPoint = models.ForeignKey('PointObjekt', verbose_name = 'Конечная точка',
                                    related_name= 'endPoint')
    ge_primech = models.TextField('Примечание', default = '-')
    
    class Meta:
        verbose_name = 'Трасса '
        verbose_name_plural = 'Трасса'
        unique_together =(('ge_objekt', 'ge_startPoint'), ('ge_objekt', 'ge_pipe'),
                          ('ge_objekt', 'ge_endPoint'))

#Файлы Обьекты газовой сети 
def objekt_upload_path(instance, filename):
    
    return 'pto/objekt/%s/%s' %(instance.ge_objekt_id, filename)
   
class ObjektFile(models.Model):
    ge_objekt = models.ForeignKey('objekt', verbose_name = 'Обьект')
    ge_objektFile = models.FileField(upload_to = objekt_upload_path)#, 
                                     #storage= objekt_upload_path)
    ge_uploaded_date = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        verbose_name = 'Документ '
        verbose_name_plural = 'Документы, файлы обьекта'
        
    def __str__(self):
        return "%s %s"%(self.ge_objekt, self.ge_objektFile)
   

# Справочники -----------------------------------------------------------------------------

# Справочник регулирующих устройств (ГРПШ)
class Spr_regulir_ustroystvo(models.Model):
    ge_ustroystvo = models.CharField('Регулирующие устройства(ГРПШ)', max_length=100)
    
    class Meta:
        verbose_name = 'Регулирующее устройство (ГРПШ)'
        verbose_name_plural = 'Справочник Регулирующих устройств (ГРПШ)'
        
    
    def __str__(self):
        return self.ge_ustroystvo
    

# Справочник Узлов (Переходы, тройники и т.д.)
class Spr_uzel(models.Model):
    ge_uzel = models.CharField('Узел', max_length=100)
    
    class Meta:
        verbose_name = u'Узел'
        verbose_name_plural = u'Справочник Узлы '
    
    def __str__(self):
        return self.ge_uzel

# Справочник Задвижек (кранов)    
class Spr_tap(models.Model):
    ge_tap = models.CharField(u'Задвижки(краны)', max_length=100)
    
    class Meta:
        verbose_name = u'Задвижка (кран)'
        verbose_name_plural = u'Справочник Задвижек (кранов)'
    
    def __str__(self):
        return self.ge_tap

# Справочник Типов трубы (материал диаметр)   
class Spr_material(models.Model):
    ge_material = models.CharField(u'Тип трубы', max_length=100)
    
    class Meta:
        verbose_name = u'Тип трубы'
        verbose_name_plural = u'Справочник Типов трубы '
    
    def __str__(self):
        return self.ge_material

# Справочник Давлений в трубе   
class Spr_pressure(models.Model):
    ge_pressure = models.CharField(u'Давление', max_length=100)
    
    class Meta:
        verbose_name = u'Давление'
        verbose_name_plural = u'Справочник Давление '
    
    def __str__(self):
        return self.ge_pressure
    
# Справочник Тип обьекта   
class Spr_tobject(models.Model):
    ge_tobject = models.CharField(u'Тип обьекта', max_length=20)
    
    class Meta:
        verbose_name = u'Тип объекта'
        verbose_name_plural = u'Справочник Тип объекта '
    
    def __str__(self):
        return self.ge_tobject

