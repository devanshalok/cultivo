from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import *
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from tablib import Dataset
from rapidconnect import RapidConnect    #to use a rapid api
import pprint       #pretty print a json
import requests     #access apis
import datetime     #get current date and time
import statistics   #calculate mean

count=0


#to get the current temperature and weather information
def api_for_weather(place):
    result=requests.get('http://api.openweathermap.org/data/2.5/weather?q='+place+'&appid=26215a2614573c7ce3405f3338415d10')
    data=result.json()
    return data


def calculate_coord(data):
        coord=[data['coord']['lat'],data['coord']['lon']]
        return coord


#to get the information about the soil of the region or district

def get_soil_info(place,coord):
    def api_for_geocon(place):
        now = datetime.datetime.now()
        start_date=str(now.year)+'-'+str(now.month-1)+'-'+str(now.day)
        end_date=str(now.year)+'-'+str(now.month+1)+'-'+str(now.day)
    #    result=requests.get('https://api.weatherbit.io/v2.0/history/agweather?lat='+str(coord[0])+'&lon='+str(coord[1])+'&start_date='+start_date+'&end_date='+end_date+'&key=283a77fe5cbe46718430e4d5418be6c1')
        result=requests.get('https://api.weatherbit.io/v2.0/forecast/agweather?lat='+str(coord[0])+'&lon='+str(coord[1])+'&key=3d6dc8552cb74208866db831e6cc7724')
        data=result.json()
        return data
    
    def cal_mean(data):
        mean_vals=[]
        summ_vals_dict={}
        keywords=['bulk_soil_density','skin_temp_avg','precip','specific_humidity','pres_avg','soilt_0_10cm','soilm_0_10cm','wind_10m_spd_avg']
        for k in keywords:
            summ=0
            for i in range(0,9):
                summ+=data['data'][i][k]
            summ_vals_dict[k]=summ
        for key in summ_vals_dict:
            summ_vals_dict[key]=(summ_vals_dict[key])/9
    
        return summ_vals_dict
    
    
    daaa=api_for_geocon(place)
    return cal_mean(daaa)



def print_temp_details(data):
       values={
               'temperature':str(data['main']['temp']-273.15)+' Celcius',
               'latitude':str(data['coord']['lat']),
               'longitude':str(data['coord']['lon']),
               'humidity':str(data['main']['humidity'])+' %',
               'pressure':str(data['main']['pressure'])+' hPa',
               'wind-speed':str(data['wind']['speed']*1.60934)+' kmph',
               'wind-direction':str(data['wind']['deg'])+' degrees',
               'visibility':str(data['visibility'])+' metres',
               }
       
       return values




























class TemplateView(generic.TemplateView):
    template_name='cultivo_main/footer.html'

def work(request):
    if request.method=='POST':
        area=request.POST['area']
        crop=request.POST['crop']


        #getting the atmosphere information
        data=api_for_weather() 
        coord=calculate_coord(data)                 #getting the json details of the atmosphere
        soil_info=get_soil_info(area,coord)         #dictionary cointaining soil info
        temp_det=print_temp_details(data)       #converting all the details into proper units for printing


        first_datset=pred_one.objects.filter(crop=crop)
        sec_datset=prod_area.objects.filter(crop=crop,district=area)
        # third_datset=one.objects.filter(crop=crop)
        # four_datset=two.objects.filter(crop=crop,area=area)

        sec_values=list(sec_datset.values())[0]



        


def val_of_pred_area()


def simple_upload(request):
    if request.method == 'POST':
        value=True

        res = predone()
        value=vv(res)

        if value==False:
            res = prodarea()
            value=vv(res)
        
        if value==False:
            res = one()
            value=vv(res)

        if value==False:
            res = two()
            value=vv(res)

        if value==False:
            res = three()
            value=vv(res)
       
    return render(request, 'core/simple_upload.html')


def vv(request,res):
    dataset = Dataset()
    new = request.FILES['myfile']

    imported_data = dataset.load(new.read())
    result = res.import_data(dataset, dry_run=True)  # Test the data import

    if not result.has_errors():
        value=True
        res.import_data(dataset, dry_run=False)  # Actually import now
    
    else:
        value=False
    return value
