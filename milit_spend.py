from __future__ import division
import csv
import re
import json
import string


table = str.maketrans(dict.fromkeys(string.punctuation))

file = open('militarization vars - militarization vars.csv', 'r')
gdp_file = open('country_gdp.csv', 'r')
gdppc_file = open('stuff/gdppc.csv', 'r')
countries_continents = open('Countries-Continents-csv.csv', 'r')

countries_continents_reader = csv.DictReader(countries_continents, delimiter=",")

writefile = open('praetorian_by_country.json', 'w')

reader = csv.DictReader(file, delimiter=',')

gdp_reader = csv.DictReader(gdp_file, delimiter=',')
gdppc_reader= csv.DictReader(gdppc_file, delimiter=',')
gdp_dict = dict()
gdppc_dict = dict()
c_c_dict = dict()
for c in countries_continents_reader:
	c_c_dict[c['Country']] = c
for d in gdp_reader:
	#print(d)
	if d['Country Name'] in gdp_dict:
		#gdp_dict[d['Country Name']].append([d['Year'], d['Value']])
		gdp_dict[d['Country Name']][d['Year']] = d['Value']
	else:
		gdp_dict[d['Country Name']] = dict()
		gdp_dict[d['Country Name']][d['Year']] = d['Value']#[[d['Year'], d['Value']]]

for d in gdppc_reader:
	gdppc_dict[d['\ufeff"Country Name"']] = d


country_dict = dict()

for row in reader:
	year = row['year']
	scf_Praetorian = float(row['scf_Praetorian']) if row['scf_Praetorian'] != '.' else 0
	scf_ExpPerTroop = float(row['scf_ExpPerTroop']) if row['scf_ExpPerTroop'] != '.' else 0
	wdi_armedfper = float(row['wdi_armedfper']) if row['wdi_armedfper'] != '.' else 0
	wdi_expmilgdp = float(row['wdi_expmilgdp']) if row['wdi_expmilgdp'] != '.' else 0
	scf_milexp = float(row['scf_milexp']) if row['scf_milexp'] != '.' else 0
	country = re.search('\D+', row['cname_year'])
	country = country.group(0)
	country = country.translate(table)
	country = country.strip()

	continent = c_c_dict[country]['Continent']
	
	if country in country_dict:
		country_dict[country].append({'year': year,
									  'scf_Praetorian' : scf_Praetorian,
									  'scf_ExpPerTroop' : scf_ExpPerTroop,
									  'wdi_armedfper' : wdi_armedfper,
									  'wdi_expmilgdp' : wdi_expmilgdp,
									  'scf_milexp' : scf_milexp,
									  'continent' :  continent,
									  'country' : country})
		#country_dict[country].append(row)
	else:
		country_dict[country] = [{'year': year,
									  'scf_Praetorian' : scf_Praetorian,
									  'scf_ExpPerTroop' : scf_ExpPerTroop,
									  'wdi_armedfper' : wdi_armedfper,
									  'wdi_expmilgdp' : wdi_expmilgdp,
									  'scf_milexp' : scf_milexp,
									  'continent' :  continent, 
									  'country' : country}]
		#country_dict[country] = [row]

	#print(country.group(0))

#for country in country_dict:
#	print(country)
#	print (country_dict[country])

#print (country_dict['United States'])
"""ex_co = country_dict['United States']

for d in ex_co:

	for t in d:
		#print (type(t))
		if t == 'year' or t == "cname_year" :
			#print('hi')
			-1
		else:
			if d[t] == '.':
				d[t] = -1
			else:
				d[t] = float(d[t])
	#print (d)
	#print (gdp_dict['United States'][d['year']])
	year_gdp = float(gdp_dict['United States'][d['year']])
	year_gdppc = float(gdppc_dict['United States'][d['year']])
	scf_milexp = d['wdi_expmilgdp'] * year_gdp * .01
	scf_ExpPerTroop = scf_milexp/(d['wdi_armedf'] +1.1)
	scf_Praetorian = scf_ExpPerTroop/year_gdppc
	print (d['year'])
	print (scf_Praetorian)"""

#print (gdppc_dict['United States'])
json.dump(country_dict, writefile, indent=4)

