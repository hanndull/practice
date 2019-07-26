#### ASSIGNMENT ###############################################################

# Write a function (in any language) that accepts an array of objects each 
# containing a product name and list of locations 
# (e.g. [“Paris”, “France”, “Europe”]), and returns an array of location objects 
# with a list of names associated with each location. 


class Product():
    
    def __init__(self, name):
        self.name = name.title()
        self.locations = []

    def add_location(self, location):
        self.locations.append(location.title())

    def __repr__(self):
        """Info about product"""
        return f"<product={self.name}; available locations={self.locations}>"


class Location():

    def __init__(self, name):
        self.name = name.title()
        self.products = []

    def add_product(self, product):
        """Only to be used with product objects"""
        self.products.append(product)

    def __repr__(self):
        """Info about location"""
        return f"<location={self.name}; available products={self.products}>"


def product_to_location(arr):
    '''Takes in an array of product objects, w/ associated location availability.
    Returns array of newly instanciated location objects. 
    Each location object contains a list of products that exist there.
    '''

    location_dict = {}

    for product in arr:
        for location in product.locations:
            # Acknowledging that this is O(n^2), 
            # but haven't yet thought of a better optimized way
            if location not in location_dict:
                location_dict[location] = [product]
            else:
                location_dict[location] += [product]

    location_obj_array = []

    for key, value in location_dict.items():
        location = Location(key)
        for item in value:
            # Acknowledging that this is O(n^2), 
            # but haven't yet thought of a better optimized way
            location.add_product(item)
        location_obj_array.append(location)

    return location_obj_array


#### TESTING #################################################################

one = Product("kayaking")
one.add_location("arcata")
one.add_location("morro bay")

two = Product("cycling")
two.add_location("arcata")
two.add_location("davis")

result = product_to_location([one, two])

for item in result: 
    print(f"\nIn {item.name}, you can take part in the following activites:")

    for product in item.products:
        print(product.name)
