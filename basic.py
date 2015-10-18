#!/usr/bin/env python
from geopy.geocoders import GoogleV3


def main():
	geolocator = GoogleV3()
	location = geolocator.geocode("175 5th Avenue NYC")
	print(location.address)
	print((location.latitude, location.longitude))
	print(location.raw)
	
if __name__=="__main__":
    main()