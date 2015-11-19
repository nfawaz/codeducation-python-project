from decimal import *

print("New program, yeah")

print("How many hours have you been in this room? (in hours)"),
hours = input()

hours = Decimal(hours)

minutes = hours * Decimal(60)

print("Then you've been here for %f hours or %f minutes!"
	% (hours, minutes))