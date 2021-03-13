from django.shortcuts import render
from pyexcel_xls import get_data as xls_get
from pyexcel_xlsx import get_data as get_data
from .models import Data_Source , Data_Set , Test_Name
import csv
from django.http import JsonResponse ,HttpResponse
import json
from django.core import serializers


def home(request):

    return render(request , "xlsxForm.html",{'data_sources' : Data_Source.objects.all()})
# Create your views here.
def index(request):
    if request.method == "POST":
        excel_file = request.FILES['file']
        
        if str(excel_file).split('.')[-1] == 'xls':

           data = xls_get(excel_file )
        elif str(excel_file).split('.')[-1] == 'xlsx':
            data = get_data(excel_file)
        
        
        
      
        dataSet = data[list(data)[0]]
        insertedNumber = 0
        for row in dataSet:
            if dataSet.index(row) == 0 :
                next
            else:   
                 datasource = Data_Source.objects.filter(name=row[dataSet[0].index('Data_Source')])
                 testname = Test_Name.objects.filter(Name=row[dataSet[0].index('Result_Name')])
                
                 print(datasource)
                
                 if len(datasource) == 0 :
                    datasource =Data_Source()
                    datasource.name = row[dataSet[0].index('Data_Source')]
                    datasource.save()
                 if len(testname) == 0 :
                    testname = Test_Name()
                    datasource = Data_Source.objects.filter(name=row[dataSet[0].index('Data_Source')])
                    testname.Name = row[dataSet[0].index('Result_Name')]
                    testname.Data_Source = datasource[0]
                    testname.save()
                 dataset = Data_Set()
                 datasource = Data_Source.objects.filter(name=row[dataSet[0].index('Data_Source')])
                 testname = Test_Name.objects.filter(Name=row[dataSet[0].index('Result_Name')])
                 dataset.Name = row[dataSet[0].index('Result_Name')]
                 dataset.Member_ID = row[dataSet[0].index('Member_ID')]
                 dataset.Result_Name = row[dataSet[0].index('Result_Name')]
                 dataset.Source = row[dataSet[0].index('Data_Source')]
                 dataset.Data_Source = datasource[0]
                 dataset.Test_Name = testname[0]
                 dataset.Result_Description = row[dataSet[0].index('Result_Description')]
                 dataset.Numeric_Result = row[dataSet[0].index('Numeric_Result')]
                 dataset.Patient_DOB = row[dataSet[0].index('Patient_DOB')]
                 dataset.Patient_Gender = row[dataSet[0].index('Patient_Gender')]
                 dataset.Date_Resulted = row[dataSet[0].index('Date_Resulted')]
                 dataset.save()
        insertedNumber+=1
    return render(request , "xlsxForm.html" , {"insertedNumber":insertedNumber})
def datasource(request,id):
    return render(request ,"index.html" , {"testname":Test_Name.objects.filter(Data_Source=id) , 'datasource':Data_Source.objects.get(id=id) , 'data_sources' : Data_Source.objects.all() })

def dataset(request,id,name):
    data = serializers.serialize('json', Data_Set.objects.filter(Data_Source=id , Test_Name=name ))
    return JsonResponse(data , safe=False)
