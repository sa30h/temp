from django_cron import CronJobBase, Schedule
from .models import Temp
import requests
import datetime

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 24*60*60 # every 24 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'application.my_cron_job'  

    def do(self):

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

        except:
            print('failed')