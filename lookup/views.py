from django.shortcuts import render

def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=D9C446DE-2742-435D-8F95-775BF1D11D85")
		try:
			api = json.loads(api_request.content)

		except Exception as e:
			api = "Error..."

		if api[0]['Category']['Name'] == "Good":
			category_description = "Enyou your outdoor activities."
			category_color = "good"

		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "Enyou your outdoor activities."
			category_color = "moderate"

		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = "Enyou your outdoor activities."
			category_color = "usg"

		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = "Enyou your outdoor activities."
			category_color = "unhealthy"

		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description = "Enyou your outdoor activities."
			category_color = "veryunhealthy"

		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "Enyou your outdoor activities."
			category_color = "hazardous"

		return render(request, 'lookup/home.html', {
                    'api': api,
                 			'category_description': category_description,
                 			'category_color': category_color
                })
	else:
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=D9C446DE-2742-435D-8F95-775BF1D11D85")
		try:
			api = json.loads(api_request.content)

		except Exception as e:
			api = "Error..."

		if api[0]['Category']['Name'] == "Good":
			category_description="Enyou your outdoor activities."
			category_color = "good"

		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "Enyou your outdoor activities."
			category_color = "moderate"

		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = "Enyou your outdoor activities."
			category_color = "usg"

		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = "Enyou your outdoor activities."
			category_color = "unhealthy"

		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description = "Enyou your outdoor activities."
			category_color = "veryunhealthy"

		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "Enyou your outdoor activities."
			category_color = "hazardous"

		

		return render(request,'lookup/home.html', {
			'api':api,
			'category_description':category_description, 
			'category_color':category_color
			})

def about(request):
	return render(request, 'lookup/about.html', {})
