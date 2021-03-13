from django import template
from App.models import Data_Source
from django.http import HttpResponse
from django.template.loader import get_template



register = template.Library()

def data_sources():
       return {'data_sources':Data_Source.objects.all()}   


users_template = get_template('Layout.html')
register.inclusion_tag(users_template,data_sources)