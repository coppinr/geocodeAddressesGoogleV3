#!/usr/bin/env python
# Created by Rhiannon Coppin, Oct. 17, 2015
from geopy.geocoders import GoogleV3
import re
import time

def usage():
    return """\nUsage: batchGeocodeCSV_goole.py \n\t\t\t-i <input csv file (full address in each row; fields separated by semicolons, if anything, and nothing else)>\n\t\t\t-o <output file name>"""

class csvGeocoder:

    def __init__(self):
    	# input filename or URL
        self.__input_filename = ''
        self.__output_filename = ''
        self.__bank = [] 
      	self.__formatted_bank = []
      	      	
    def parseOptions(self, args):
    	import getopt
    	try:
    		optlist, arglist = getopt.getopt(args, 'i:o:')  #f is a switch and doesn't require an arg. 'a' too.
    	except getopt.GetoptError, e:
    		print e
    		return None
    	for option, value in optlist:
    		if option.lower() in ('-i', ):
    			self.__input_filename = value
    		elif option.lower() in ('-o', ):
    			self.__output_filename = value
        if not self.__input_filename:
            sys.exit("Error: input filename or URL not given")
        if not self.__output_filename:
            sys.exit("Error: output filename or URL not given")
                
    def loadCSV(self):
		try:
			f = open(self.__input_filename, 'r')
			raw_text = f.readline()
			while raw_text:
				self.__bank.append(raw_text.rstrip())
				raw_text = f.readline()
		except (OSError, IOError), e:
			print e
	
    def formatAddresses(self):
        for address in self.__bank:
            address = re.sub(',+',",+",re.sub('\s+',"+", address))
            self.__formatted_bank.append(address)

    def geocode(self):
        geolocator = GoogleV3()
    	for address in self.__formatted_bank:
			location = geolocator.geocode(address)
			print((location.latitude, location.longitude))
			self.__bank.append(''.join([self.__bank.pop(0),',',str(location.latitude),',',str(location.longitude)]))
			time.sleep(.1) # don't query too fast now
			print self.__bank
        	
    def outputCSV(self):
        f = open(self.__output_filename, 'w')
        print "Saving output CSV to "+self.__output_filename
        for line in self.__bank:
            f.write(line+'\n')
            print line
        f.close()

def main():
	import sys
	if len(sys.argv)<4:
		sys.exit(usage())

	coder = csvGeocoder()
	coder.parseOptions(sys.argv[1:])
	coder.loadCSV()
	coder.formatAddresses();
	coder.geocode()
	coder.outputCSV()
	#geolocator = GoogleV3()
	#location = geolocator.geocode("175 5th Avenue NYC")
	#print(location.address)
	#print((location.latitude, location.longitude))
	#print(location.raw)
	
if __name__=="__main__":
    main()