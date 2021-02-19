import re

s = raw_input("Do you agree?\n")

if re.search("y(es)?", s, re.IGNORECASE):
	print("Agreed.")
if re.search("n(o)?", s, re.IGNORECASE):
	print("Not agreed.")
