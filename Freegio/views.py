from django.shortcuts import render
import requests
from . import models
from django.views.generic import ListView,DetailView
from datetime import datetime
from django.shortcuts import redirect 
from django.contrib import messages
from . models import Launches


# Create your views here.
def call(request):
    i=0

    check=models.Launches.objects.all()
    for check in check:
        i+=1
        break

    if i==1 : 
        messages.info(request,f'Details Already Downloaded ')
        return render(request,"home.html")
    else :
        response=requests.get('https://api.spacexdata.com/v3/launches')
        launch=response.json()
        
        
        for  launch in launch:
          Proto=models.Launches()
    
          Proto.Mission_name=launch['mission_name']
          Proto.Flight_Number=launch['flight_number']
          date=launch['launch_date_utc'][0:10]
          time=launch['launch_date_utc'][11:22]
          date_time=date+' '+time
          date_time_obj=datetime.strptime(date_time,'%Y-%m-%d %H:%M:%S.%f')
          Proto.Flight_date=date_time_obj
     


          Proto.Flight_date=launch['launch_date_utc']
          Proto.Rocket_Name=launch['rocket']['rocket_name']
          Proto.Rocket_Id=launch['rocket']['rocket_id']
          Proto.Mission_Patch_Link=launch['links']['mission_patch']
          Proto.Mission_Video_Link=launch['links']['video_link']
          Proto.Launch_site=launch['launch_site']['site_id']
          Proto.save()
         
        
        
    return render(request,"home.html")
    
    
   

class LaunchesListView(ListView):
    model=Launches
    template_name="Space X ListViews.html"
    context_object_name='launch'


def home(request):
    return render(request,"home.html")

def detail_view(request,obj_id):
    val5=models.Launches.objects.get(id=obj_id)
    val2=val5.Launch_site
    url="http://www.mapquestapi.com/geocoding/v1/address?key=eaZxlWiQTc5uFUWzSKLtR3sMzOdgadr1&location='{}'".format(val2)
    response=requests.get(url)
    coor=response.json()
    val1=coor['results'][0]['locations'][0]['displayLatLng']['lat']
    val2=coor['results'][0]['locations'][0]['displayLatLng']['lng']
    print(val2)
    
    
    return render(request,"Space x DetailView.html",{'val5':val5,'val2':val2,'val1':val1}) 





    
   
    

    
   
     

   
   