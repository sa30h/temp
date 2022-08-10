import requests

url = "https://weatherapi-com.p.rapidapi.com/history.json"

# country=['London','Canada','America','Japan','India']
# country=['Brazil']
country=['Canada','Brazil','Japan','India']
database_name=['Ottawa','Brasilia','Tsuboana','New_Delhi']

for i in country:

    querystring = {"q":i,"dt":"2022-08-05","lang":"en"}

    headers = {
        "X-RapidAPI-Key": "eba8bf64c0msha8d7872eae06eccp147836jsn25ca06e40347",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print("///start",i,"\n")
    
    print(response.json()['location']['name'])
    print(response.json()['location']['country'])
    print(response.json()['forecast']['forecastday'][0]['date'])
    print(response.json()['forecast']['forecastday'][0]['day']['maxtemp_f'])

    # print(response.json()['location']['country'])
    print('....end ',i,'\n')

