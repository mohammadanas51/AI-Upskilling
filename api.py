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
            otherInfo = jsonResponse.get("data", {})
            print("Other info ")
            for key, values in otherInfo.items():
                print(f"{key} - {values}")
        elif response.status_code == 404:
            print("No device found for the given id")
        else:
            print("Unexpected error", response.status_code)
    except Exception as e :
        print("Something went wrong ", e)

def main():
    id = input("Enter the device's Id ")
    getObjectsById(id)

main()