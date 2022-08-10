# from django_cron import CronJobBase, Schedule
# from .models import Covidcases
# import requests
# import datetime

# class MyCronJob(CronJobBase):
#     RUN_EVERY_MINS = 24*60*60 # every 24 hours

#     schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
#     code = 'application.my_cron_job'  

#     def do(self):

#         try: 
#             url = "https://covid-193.p.rapidapi.com/statistics"

#             headers = {
#                 "X-RapidAPI-Key": "eba8bf64c0msha8d7872eae06eccp147836jsn25ca06e40347",
#                 "X-RapidAPI-Host": "covid-193.p.rapidapi.com"
#                 }

#             response = requests.request("GET", url, headers=headers)

#             # print(response.json())

#             for i in range(0,20):
#                 country=response.json()['response'][i]['country']
#                 total_case=response.json()['response'][i]['cases']['total']
#                 date=response.json()['response'][i]['day']
#                 c=Covidcases(country=country,total_case=total_case,date=date)
#                 c.save()

#         except:
#             print('can not run get data in application view')