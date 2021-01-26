# Tuples

# tuple list of city and states
city_state = [('Seattle', 'WA'), ('Portland', 'OR'), ('San Francisco, CA')]
print(len(city_state))

# how to see first city in city state tuple list
first_city_state = city_state[0]
print(first_city_state)

# one way to view just city or just the state
print(first_city_state[0])
print(first_city_state[1])

# unpacks tuple to retrieve only the city
city, state = first_city_state
print(city)

# tuple of animals
animals = ('lion', 'puma', 'tiger')

# need to store as many items as there are in the tuple when unpacking, 2 animals would not be enough here
line, puma, tiger = animals
print(tiger)

# can return values from a function as a list of tuples
def get_distance():
    miles = 1000
    km = miles * 1.6
    return miles, km  # returns as list of tuples


distances = get_distance()
print(distances)
print(distances[0])

miles, km = distances
print(km)