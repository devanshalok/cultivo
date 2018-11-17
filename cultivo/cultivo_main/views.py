from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from cultivo_main.models import *
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


# =======================================FOR WORK USING THE API OF WEATHER AND SOIL DETAILS=====================================


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
       
       temp=precise((data['main']['temp']-273.15),1)
       wind=precise((data['wind']['speed']*1.60934),2)
       dire=precise((data['wind']['deg']),2)

       values={
               'temperature':str(temp),
               'latitude':str(data['coord']['lat']),
               'longitude':str(data['coord']['lon']),
               'humidity':str(data['main']['humidity'])+'%',
               'pressure':str(data['main']['pressure'])+'hPa',
               'windspeed':str(wind)+'km/h',
               'winddirection':str(dire)+' degrees'
            #    'visibility':str(data['visibility'])+' metres',
               }
       
       return values



def precise(data,point):
    if type(data)==dict:
        a={}
        for i in data:
            if type(data[i])==float:
                data[i]=round(data[i],point)
                a[i]=data[i]
            else:
                a[i]=data[i]
    
    if type(data)==float:
        return round(data,point)
    
    if type(data)==list:
        a=[]
        for i in data:
            if type(i)==float:
                i=round(i,point)
                print(i)
                a.append(i)
            else:
                a.append(i)
    return a





# ==========================================MAIN DJANGO VIEWS=============================================



class TemplateView(generic.TemplateView):
    template_name='cultivo_main/footer.html'

def work(request):
    if request.method=='POST':
        area=request.POST['area'].upper()
        crop=request.POST['crop'].capitalize()


        #getting the atmosphere information
        data=api_for_weather(area)                  #getting the json details of the atmosphere
        coord=calculate_coord(data)                 #extracting the coordinates
        soil_info=get_soil_info(area,coord)         #dictionary cointaining soil info
        temp_det=print_temp_details(data)       #converting all the details into proper units for printing

        # soil_info_2=precise(soil_info,2)
        # temp_det_2=precise(temp_det,1)

        # filtering the objects

        first_datset=pred_one.objects.filter(crop=crop)
        sec_datset=prod_area.objects.filter(crop=crop,district=area)
        third_datset=pred_three.objects.filter(crop=crop)


        # #gettting dictionaries out of the returned values

        fir=list(first_datset.values())[0]['Gross_Production_Value_current_million_US_dollar']
        first_value={'Gross_Production_Value_current_million_US_dollar':fir}


        sec_values=list(sec_datset.values())[0]
        del sec_values['id']
        del sec_values['org_val']

        third_values=list(third_datset.values())[0]
        del third_values['id']
        del third_values['crop']


        final_dict={**sec_values,**third_values,**first_value}
        # del final_dict['id']

        valll=precise(first_value,2)
        return render(request,'cultivo_main/index.html',{'first':first_value,'second':sec_values,'third':third_values, 'temp_det':temp_det,'final':valll})
    else:
        raise Http404("You are unauthorised to access this page")
        
        # =====================================================for making the final prediction====================================
        




# ===================================================FOR IMPORTING CSV FILES TO DJANGO DBS============================================


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
        
        if value==False:
            res = pred_three()
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
