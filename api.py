import requests

baseURL = "https://api.restful-api.dev/"

def getObjectsById(id):
    url = f"{baseURL}/objects/{id}"
    response = requests.get(url)
    if(response.status_code == 200):
        print("API Response", response)
        jsonResponse = response.json()
        print("JSON response", jsonResponse)
    else:
        print("Something went wrong")


getObjectsById(10)