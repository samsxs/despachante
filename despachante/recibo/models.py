# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Recibo(models.Model):
	name = models.CharField(max_length=60, verbose_name='Nome')
	address = models.CharField(max_length=100, verbose_name='Endereço')
	city = models.CharField(max_length=50, verbose_name='Cidade')
	cep = models.CharField(max_length=10, verbose_name='Cep')
	phone = models.CharField(max_length=20, verbose_name='Telefone')
	mobile = models.CharField(max_length=20, verbose_name='Celular')

	def __str__(self):
		return self.name

#	class Meta:
