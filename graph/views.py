
from multiprocessing import context
from django.shortcuts import render,HttpResponse
import requests
from .models import *
import datetime
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
# Create your views here.
from .serializer import TempSerializer
from rest_framework.response import Response


def Graph(request):
    database_country=['Canada','Brazil','Japan','India']
    database_name=['Ottawa','Brasilia','Tsuboana','New_Delhi']
    if request.GET:
        context={}
        date=request.GET.get('getdate')
       
        # datelist=[]options: {}
        # namelist=[]
        # temp_flist=[]
        today = date
        five_day_before = today - datetime.timedelta(days=5)
        res={}
        for i in database_country:
            tempdict={}
            temp=Temp.objects.filter(country=i,date__gte=five_day_before).values('date','temp_f')
            for j in temp:
                tempdict[str(j['date'])]=float(j['temp_f'])
                # print(j)

            datelist=list(tempdict.keys())  
            temp_flist=list(tempdict.values())
            res[i]={'date':datelist,'temp_f':temp_flist}

        # print('res',res)

        CanadaDatelist=res['Canada']['date']
        Canadatemp_flist=res['Canada']['temp_f']

        BrazilDatelist=res['Brazil']['date']
        Braziltemp_flist=res['Brazil']['temp_f']

        JapanDatelist=res['Japan']['date']
        Japantemp_flist=res['Japan']['temp_f']

        IndiaDatelist=res['India']['date']
        Indiatemp_flist=res['India']['temp_f']

        # print(CanadaDatelist,Canadatemp_flist)
        # print(BrazilDatelist,Braziltemp_flist)
        # print(JapanDatelist,Japantemp_flist)
        # print(IndiaDatelist,Indiatemp_flist)

        context['CanadaDatelist']=CanadaDatelist
        context['Canadatemp_flist']=Canadatemp_flist
        context['BrazilDatelist']=BrazilDatelist
        context['Braziltemp_flist']=Braziltemp_flist 
        context['JapanDatelist']=JapanDatelist
        context['Japantemp_flist']=Japantemp_flist
        context['Indiatemp_flist']=Indiatemp_flist
        context['IndiaDatelist']=IndiaDatelist  

       

        # context['countrylist']=countrylist
        # context['totalcaselist']=totalcaselist
        # # context['base']="USD"
        # context['date']=str(date)
        # # print(context['date'])
        # print(countrylist,totalcaselist)
        # return render(request,'application/dashboard.html',context)

    context={}
    context={}
    date=request.GET.get('getdate')
    tempdict={}
    datelist=[]
    namelist=[]
    temp_flist=[]
    today = datetime.datetime.today().date()
    five_day_before = today - datetime.timedelta(days=5)
    
    res={}
    for i in database_country:
        tempdict={}
        temp=Temp.objects.filter(country=i,date__gte=five_day_before).values('date','temp_f')
        for j in temp:
            tempdict[str(j['date'])]=float(j['temp_f'])
            # print(j)

        datelist=list(tempdict.keys())  
        temp_flist=list(tempdict.values())
        res[i]={'date':datelist,'temp_f':temp_flist}

    print('res',res)

    CanadaDatelist=res['Canada']['date']
    Canadatemp_flist=res['Canada']['temp_f']

    BrazilDatelist=res['Brazil']['date']
    Braziltemp_flist=res['Brazil']['temp_f']

    JapanDatelist=res['Japan']['date']
    Japantemp_flist=res['Japan']['temp_f']

    IndiaDatelist=res['India']['date']
    Indiatemp_flist=res['India']['temp_f']


    context['CanadaDatelist']=CanadaDatelist
    context['Canadatemp_flist']=Canadatemp_flist
    context['BrazilDatelist']=BrazilDatelist
    context['Braziltemp_flist']=Braziltemp_flist 
    context['JapanDatelist']=JapanDatelist
    context['Japantemp_flist']=Japantemp_flist
    context['Indiatemp_flist']=Indiatemp_flist
    context['IndiaDatelist']=IndiaDatelist        

    return render(request,'graph/graph.html',context)


def get_data(request):

    try: 
        
        date=datetime.datetime.today().date()
        url = "https://weatherapi-com.p.rapidapi.com/history.json"

        country=['Canada','Brazil','Japan','India']

        for i in country:

            # querystring = {"q":i,"dt":"2022-08-09","lang":"en"}
            querystring = {"q":i,"dt":str(date),"lang":"en"}

            headers = {
                "X-RapidAPI-Key": "eba8bf64c0msha8d7872eae06eccp147836jsn25ca06e40347",
                "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            name=response.json()['location']['name']
            country_res=response.json()['location']['country']
            date_res=response.json()['forecast']['forecastday'][0]['date']
            temp_f=response.json()['forecast']['forecastday'][0]['day']['maxtemp_f']
            t=Temp(name=name,country=country_res,date=date_res,temp_f=str(temp_f))
            t.save()

        return HttpResponse("Data successfully added !")            

    except:
        # print('can not run get data in application view')
        return HttpResponse("Data not added !")


class Getallapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Temp.objects.all()
    serializer_class=TempSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def  post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

        
        
        

class Getbyid(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset=Temp.objects.all()
    serializer_class=TempSerializer
    lookup_field="id"

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

   

class Getbydate(GenericAPIView):
    queryset=Temp.objects.all()
    serializer_class=TempSerializer
    def get(self,request,date=None):
        queryset            =   Temp.objects.filter(date=date)
        serialize           =   TempSerializer(queryset,many=True,context={'request': request})

        return Response(serialize.data)

class Getbycountry(GenericAPIView):
    queryset=Temp.objects.all()
    serializer_class=TempSerializer
    def get(self,request,country=None):
        queryset            =   Temp.objects.filter(country=country)
        serialize           =   TempSerializer(queryset,many=True,context={'request': request})
        return Response(serialize.data)






