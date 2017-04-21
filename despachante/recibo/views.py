# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Recibo


# Create your views here.
def recibo_exibir(request):
	recibo = Recibo.objects.all()
	context = {'recibo': recibo}

	return render(request, 'recibo/recibo_exibir.html', context)