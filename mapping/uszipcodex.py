from uszipcode import SearchEngine, SimpleZipcode, state_abbr

search = SearchEngine(simple_zipcode=True)
states = state_abbr.STATE_ABBR_LONG_TO_SHORT.keys()


# def get_results(city):
#     cities = set()
#     results = search.by_city(city, returns=100000)
#     for result in results:
#         cities.add(result.major_city)
#     return cities


# a = get_results('Anchorage')
# print(len(a))

print(states)