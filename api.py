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

def insertNewDevice():
    try :
        url = f"{baseURL}/objects"
        dataToInsert = {
            "name": "Dell G15 3350",
            "data": {
                "year": 2026,
                "price": 787987,
                "CPU model": "Inter I10 ",
                "Hard disk size": "12TB"
            }
        }
        response = requests.post(url, json=dataToInsert)
        print("Raw API Response", response)
        jsonResponse = response.json()
        print("JSON Response ", jsonResponse)
    except Exception as e :
        print("Something went wrong ", e)


def main():
    print("1. Get Device By Id")
    print("2. Insert New Device")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        id = input("Enter the device's Id ")
        getObjectsById(id)
    elif(choice == 2):
        insertNewDevice()

main()