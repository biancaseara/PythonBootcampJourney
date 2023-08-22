programming_dictionary = {
    "Bug": "An error in a program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}

# RETRIEVING ITEMS FROM DICTIONARY 
#print(programming_dictionary['Bug']) # Watch out the typos and make sure of giving the keys the right data type

# ADDING NEW ITEMS TO DICTIONARY
# programming_dictionary['LOOP'] = "The action of doing something over and over again."
# print(programming_dictionary)

# CREATE AN EMPTY DICTIONARY
empty_dictionary = {}

# WIPE AN EXISTING DICTIONARY
# programming_dictionary = {}

# EDIT AN ITEM IN A DICTIONARY
programming_dictionary['Bug'] = "A moth in your computer."
print(programming_dictionary)

# LOOP THROUGH A DICTIONARY
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# NESTING
capitals= {
    "France": "Paris",
    "Germany": "Berlin",
}

# NESTING A LIST IN A DICTIONARY
# NESTING DICTIONARY IN A DICTIONARY
travel_log = {
    'France': {
    'cities_visited': ["Paris", 'Lille', 'Dijon'],
    "total_visits": 12,
    },
    'Germany': {
    'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'],
    "total_visits": 5,
    }, 
}

# NESTING DICTIONARY IN A LIST
travel_log = [
    {
    'country': 'France',
    'cities_visited': ["Paris", 'Lille', 'Dijon'],
    "total_visits": 12,
    },
    {
    'country': 'Germany',
    'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'],
    "total_visits": 5,
    }, 
]

