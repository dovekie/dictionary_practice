melon_attributes = {
	#melon name: price, seedlessness true/false, flesh, rind
    "Honeydew": {"price": 0.99, "seedless": True, "flesh": "pink", "rind":"green", "avg_weight":4.0},
    "Crenshaw": {"price": 2.00, "seedless": False, "flesh": "pink", "rind":"green", "avg_weight":4.0},
    "Crane": {"price": 2.50, "seedless": False, "flesh": "pink", "rind":"green", "avg_weight":2.0},
    "Casaba": {"price": 2.50, "seedless": False, "flesh": "pink", "rind":"green", "avg_weight":5.0},
    "Cantaloupe": {"price": 0.99, "seedless": False, "flesh": "pink", "rind":"green", "avg_weight":3.0},
}

def add_melon(melon_name, melon_traits):
	if melon_name in melon_attributes.keys():
		print "Error: attempted to overwrite existing melon: %s" % melon_name
	else:
		melon_attributes[melon_name] = melon_traits
		print "Successfully added %s to the master melon list." % melon_name
		
def add_trait(trait, default_value):
	if trait in melon_attributes:
		print "Error: attempted to overwrite existing trait: %" % trait
	else:
		for melon in melon_attributes.keys():
			melon_attributes[melon][trait] = default_value
		print "added %s to the list of traits." %trait