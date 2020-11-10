

dict={'a':'b', 'mark':'keys'}



key = list(dict.keys())[0]

print(key)
value = list(dict.values())[0]

print(value)

key = list(dict.keys())[1]

print(key)


value = list(dict.values())[1]

print(value)

print(dict)

api_key = 'e1cc3b06e32c686d42d4d4b44dd13cc285ee578c'

import meraki

m = meraki.DashboardAPI(api_key)

orgs = m.organizations.getOrganizations()

print(orgs)


