# 11.1
from city_function import city_information

def test_city_information():
	city_info = city_information('santiago','chile')
	assert city_info == 'Santiago, Chile'

def test_city_country_population():
	city_info = city_information('santiago','chile',5000000)
	assert city_info == 'Santiago, Chile - population 5000000'

# over!!!