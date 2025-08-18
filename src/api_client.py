import requests
import ipdb

def get_location(ip=None):
    url = f'https://freeipapi.com/api/json/{ip}'
    response = requests.get(url)
    response.raise_for_status()
    data =  response.json()
    ipdb.set_trace()
    return {
        "countryName": data["countryName"],
        "regionName": data["regionName"],
        "capital": data["capital"],
        "cityName": data["cityName"],
    }

if __name__ == '__main__':
    data = get_location(ip='8.8.8.8')
    print(data)
