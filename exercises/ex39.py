#Dictionaries, Oh Lovely Dictionaries

#putting shit in Dictionaries(hashes)
# >>> stuff[1] = "Wow"
# >>> stuff[2] = "Neato"
# >>> print(stuff[1])
# Wow
# >>> print(stuff[2])
# Neato

#removing shit from Dictionaries (hashes)
# >>> del stuff['city']
# >>> del stuff[1]
# >>> del stuff[2]
# >>> stuff
# {'name': 'Zed', 'age': 39, 'height': 74}


# create a mapping of state to appreviation
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

#create a basic set of states and some cities in them
cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

#add some more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-' * 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

#print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then the cities dict
print('-' * 10)
# essentially combining two hashes to get the info we want
print("Michigan has: ",  cities[states['Michigan']])
print("Florida has: ",  cities[states['Florida']])

#print every state abbreviation
print('-' * 10)
#states.items() prints out the keys and values in an array.
# here it looks like:
# dict_items([('Oregon', 'OR'), ('Florida', 'FL'), ('California', 'CA'), ('New York', 'NY'), ('Michigan', 'MI')])
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated as {abbrev}")

#print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get an abbreviation by state that might not be there
state = states.get('Texas')

#if state doesn't exist do the following logic. (It doesn't exist)
if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
