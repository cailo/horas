#encoding:utf-8
from django.db import models

class formulario(models.Model):
    numero = models.AutoField(u'Numero', primary_key=True)  
    descripcion = models.TextField(u'Descripcion')
    empleado = models.ForeignKey('dh01')
    porcentaje = (
        (100, '100%'),
        (50, '50%'),
    )
    porcentaje = models.CharField(max_length=4, choices=porcentaje, default=50)
    sueldo = models.IntegerField(max_length=5) 	
    estado = models.TextField(max_length=3)
    fecha = models.DateTimeField(auto_now=True)
	
    def __unicode__(self):
        return u'%s' % self.numero
        

class dh01 (models.Model):
    desc_appat = models.CharField(u'Apellido', max_length=60)    
    desc_nombr = models.CharField(u'Nombre', max_length=60)    
    nro_legaj = models.IntegerField(u'Legajo', max_length=4, primary_key=True)     
    tipo = (
        ('ci',u'CI'),
        ('dni',u'DNI'),
        ('lc',u'LC'),
        ('le',u'LE'),
        ('pas',u'PAS')
    )
    tipo_docum = models.CharField(u'Documento', max_length=3, choices=tipo)     
    nro_docum = models.IntegerField(u'Numero')
    sexo = (
        ('f',u'Femenino'),
        ('m',u'Masculino')
    )
    tipo_sexo = models.CharField(u'Sexo', max_length=1, choices=sexo)
    secr = models.ForeignKey('secretaria')
    
    def __getitem__(self):
        return self.nro_legaj

class secretaria(models.Model):
    name = models.CharField(u'Nombre', max_length=120)
    
    def __unicode__(self):
        return self.name
        