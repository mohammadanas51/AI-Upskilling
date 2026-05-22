import requests

baseURL = "https://api.restful-api.dev/"

def getObjectsById(id):
    try:
        url = f"{baseURL}/objects/{id}"
        response = requests.get(url)
        if(response.status_code == 200):
            print("API Response", response)
            jsonResponse = response.json()
            print("JSON response", jsonResponse)
            print("Device Name ", jsonResponse["name"])
            capacityExists = jsonResponse.get("data", {}).get("Capacity")
            if capacityExists:
                print("Device Capacity ", jsonResponse["data"]["Capacity"])
            else:
                print("Other data ", jsonResponse["data"])
    except:
        print("Something went wrong ")

def main():
    id = input("Enter the device's Id ")
    getObjectsById(id)

main()