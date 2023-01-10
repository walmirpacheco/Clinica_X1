from django.db import models
from django.conf.urls import url
from stdimage.models import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo 

class Funcionario(Base):

    nome = models.CharField('Nome', max_length=100)
    endereco = models.CharField('Endereço', max_length=150, null=True, blank=False)        
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to='get_file_path', variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    tel01 = models.CharField('Celular', max_length=60, null=True, blank=False)
    tel02 = models.CharField('Tel. Residencial', max_length=60, null=True, blank=False)       
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome 
        
class Cliente(Base):

    cliente = models.CharField('Nome', max_length=100)     
    endereco = models.CharField('Endereço', max_length=150, null=True, blank=False)
    bio = models.TextField('Bio', max_length=200, null=True, blank=False)
    imagem = StdImageField('Imagem', upload_to='get_file_path', variations={'thumb': {'width': 75, 'height': 75, 'crop': True}})
    tel01 = models.CharField('Celular', max_length=60, null=True, blank=False)
    tel02 = models.CharField('Tel. Residencial', max_length=60, null=True, blank=False)       
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.cliente        
                     