from __future__ import division
import csv
import re
import json
import string

def fix_name(country):
	if country == 'Korea North':
		return 'North Korea'
	elif country == 'Korea South':
		return 'South Korea'
	elif country == 'United States':
		return 'United States of America'
	elif country == 'Serbia':
		return 'Republic of Serbia'
	elif country == 'Tanzania':
		return 'United Republic of Tanzania'
	elif country == 'Bahamas':
		return 'The Bahamas'
	elif country == 'Cote dIvoire':
		return 'Ivory Coast'
	elif country == 'Congo Democratic Republic':
		return 'Democratic Republic of the Congo'
	elif country == 'Congo':
		return 'Republic of the Congo'
	elif country == 'Cape Verde':
		return 'Cabo Verde'
	elif country == 'Czech Republic':
		return 'Czechia'
	elif country == 'Micronesia':
		return 'Federated States of Micronesia'
	elif country == 'GuineaBissau':
		return 'Guinea-Bissau'
	elif country == 'St Kitts and Nevis':
		return 'Saint Kitts and Nevis'
	elif country == 'St Lucia':
		return 'Saint Lucia'
	elif country == 'St Vincent and the Grenadines':
		return 'Saint Vincent and the Grenadines'
	elif country == 'TimorLeste':
		return 'East Timor'
	else:
		return country

table = str.maketrans(dict.fromkeys(string.punctuation))

file = open('militarization vars - militarization vars.csv', 'r')
gdp_file = open('country_gdp.csv', 'r')
gdppc_file = open('stuff/gdppc.csv', 'r')
countries_continents = open('Countries-Continents-csv.csv', 'r')

countries_continents_reader = csv.DictReader(countries_continents, delimiter=",")
#writefile = open('praetorian_by_country.json', 'w')
writefile = open('praetorian_by_country_3c.json', 'w')

reader = csv.DictReader(file, delimiter=',')

gdp_reader = csv.DictReader(gdp_file, delimiter=',')
gdppc_reader= csv.DictReader(gdppc_file, delimiter=',')
gdp_dict = dict()
gdppc_dict = dict()
c_c_dict = dict()
for c in countries_continents_reader:
	c_c_dict[c['Country']] = c
#for d in gdp_reader:
#	d['Country Name '] = d['Country Code']
	#print(d)
	#if d['Country Name'] in gdp_dict:
		#gdp_dict[d['Country Name']].append([d['Year'], d['Value']])
		#gdp_dict[d['Country Name']][d['Year']] = d['Value']
	#else:
		#gdp_dict[d['Country Name']] = dict()
		#gdp_dict[d['Country Name']][d['Year']] = d['Value']#[[d['Year'], d['Value']]]

"""for d in gdppc_reader:
	gdppc_dict[d['\ufeff"Country Name"']] = d['Country Code']

gdppc_dict['Bahamas'] = 'BHS'
gdppc_dict['Brunei'] = 'BRN'
gdppc_dict['Cote dIvoire'] = 'CIV'
gdppc_dict['Congo Democratic Republic'] = 'COD'
gdppc_dict['Congo'] = 'COG'
gdppc_dict['Cape Verde'] = 'CPV'
gdppc_dict['Czechoslovakia'] = 'CSK'
gdppc_dict['Germany East'] = 'GDR'
gdppc_dict['Germany West'] = 'FRG'
gdppc_dict['Egypt'] = 'EGY'
gdppc_dict['Micronesia'] = 'FSM'
gdppc_dict['Gambia'] = 'GMB'
gdppc_dict['GuineaBissau'] = 'GNB'
gdppc_dict['Iran'] = 'IRN'
gdppc_dict['Kyrgyzstan'] = 'KGZ'
gdppc_dict['St Kitts and Nevis'] = 'KNA'
gdppc_dict['Korea South'] = 'KOR'
gdppc_dict['Korea North'] = 'PRK'
gdppc_dict['Laos'] = 'LAO'
gdppc_dict['St Lucia'] = 'LCA'
gdppc_dict['Macedonia'] = 'MKD'
gdppc_dict['Russia'] = 'RUS'
gdppc_dict['Serbia and Montenegro'] = 'SCG'
gdppc_dict['USSR'] = 'SUN'
gdppc_dict['Slovakia'] = 'SVK'
gdppc_dict['Syria'] = 'SYR'
gdppc_dict['TimorLeste'] = 'TLS'
gdppc_dict['Taiwan'] = 'TWN'
gdppc_dict['St Vincent and the Grenadines'] = 'VCT'
gdppc_dict['Vietnam South'] = 'NOTHING' #empty
gdppc_dict['Venezuela'] = 'VEN'
gdppc_dict['Vietnam North']  = 'NOTHING' #empty
gdppc_dict['Tibet'] = 'TIB'
gdppc_dict['Yemen'] = 'YEM'
gdppc_dict['Yemen North'] = 'NOTHING'
gdppc_dict['Yemen South'] = 'NOTHING'
gdppc_dict['Yugoslavia'] = 'YUG'
print (gdppc_dict)"""
country_dict = dict()

for row in reader:
	year = row['year']
	scf_Praetorian = float(row['scf_Praetorian']) if row['scf_Praetorian'] != '.' else -1
	scf_ExpPerTroop = float(row['scf_ExpPerTroop']) if row['scf_ExpPerTroop'] != '.' else -1
	wdi_armedfper = float(row['wdi_armedfper']) if row['wdi_armedfper'] != '.' else -1
	wdi_expmilgdp = float(row['wdi_expmilgdp']) if row['wdi_expmilgdp'] != '.' else -1
	scf_milexp = float(row['scf_milexp']) if row['scf_milexp'] != '.' else -1
	country = re.search('\D+', row['cname_year'])
	country = country.group(0)
	country = country.translate(table)
	country = country.strip()
	print(country)
	#country_code = gdppc_dict[country]
	country_code = fix_name(country)
	print(country_code)

	continent = c_c_dict[country]['Continent']
	
	if country_code in country_dict:
		country_dict[country_code].append({'year': year,
									  'scf_Praetorian' : scf_Praetorian,
									  'scf_ExpPerTroop' : scf_ExpPerTroop,
									  'wdi_armedfper' : wdi_armedfper,
									  'wdi_expmilgdp' : wdi_expmilgdp,
									  'scf_milexp' : scf_milexp,
									  'continent' :  continent,
									  'country' : country})
		#country_dict[country].append(row)
	else:
		country_dict[country_code] = [{'year': year,
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

