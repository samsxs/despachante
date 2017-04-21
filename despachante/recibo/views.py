# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def recibo_exibir(request):
	return render(request, 'recibo/recibo_exibir.html', {})