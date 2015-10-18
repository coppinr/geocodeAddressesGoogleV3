# geocodeAddressesGoogleV3

This script uses geopy ("pip install geopy") to geocode a list of addresses.

The addresses are to be in a list, one per line, in a CSV text file in the following sample format:

> 1330 Chess Street, Vancouver, BC

Spaces don't matter. If addreses have extra commas, the whole will have to be escaped with quotes:

> "Suite 702, 777 W Broadway", Vancouver, BC


The returned latitude and longitude will be appended to the address, along with separating commas, and the entire string will become a new line in the output file.

Note: This script is set up to geocode with GoogleV3, which has a daily limit of 2,500 from one IP address, and a speed limit of 10 requests per second. The geopy library has other options. Find out more here: [https://github.com/geopy/geopy]https://github.com/geopy/geopy

###Quick Start:

Usage: **python batchGeocodeCSV_google.py -i inputfile.csv -o outputfile.csv**