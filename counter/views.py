from django.shortcuts import render

import requests
import json

# Create your views here.
def home(request):
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
        api_response = requests.get(api_url, headers={'X-Api-Key': 'g0JEDfQ6PODMiVqjvAhQPA==gWc0vuMdQQIEYy3e'})

        try: 
            api = json.loads(api_response.content)
            print(api_response)
        except Exception as e:
            api = "oops! something went wrong"
            print(e)
        
        return render(request, 'home.html', {'api':api})

    else:
        return render(request, 'home.html', {'query':'Enter a valid query'})


        