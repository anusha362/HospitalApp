from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

class Department(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='department'
        verbose_name_plural='departments'

    def get_url(self):
        return reverse('doc_dept',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Doctor(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    img=models.ImageField(upload_to='product')
    desc=models.TextField()
    available=models.BooleanField()
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    def get_url(self):
        return reverse('details',args=[self.department.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)
