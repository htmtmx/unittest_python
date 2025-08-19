import requests


def get_location(ip=None, country_code=None):
    url = f"https://freeipapi.com/api/json/{ip}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    # ipdb.set_trace()
    return {
        "country": data["countryName"],
        "region": data["regionName"],
        "capital": data["capital"],
        "city": data["cityName"],
        "country_code": data["countryCode"],
    }


if __name__ == "__main__":
    data = get_location(ip="8.8.8.8")
    print(data)
