"""
Prints out all the melons in our inventory
"""

from melons import melon_attributes
from melons import add_melon
from melons import add_trait

def print_melon_basic(melon_name):
	melon_traits = melon_attributes[melon_name]

	have_or_have_not = 'have'
	if melon_traits["seedless"]:
		have_or_have_not = 'do not have'

	print "%ss %s seeds and are $%0.2f" % (melon_name, have_or_have_not, melon_traits["price"])

def print_melon_all(melon_name):
	melon_traits = melon_attributes[melon_name]
	
	print melon_name
	for trait, value in melon_traits.items():
		print "\t%s: %s" %(trait, value)

add_melon("Muskmelon", {"price": 0.99, "seedless": True, "flesh": "pink", "rind":"green", "avg_weight":4.0})
add_trait("On sale", False)

for melon in melon_attributes.keys():
    print_melon_all(melon)