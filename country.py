
from countryinfo import CountryInfo

count = input("Enter country name: ")
country = CountryInfo(count)
print("Capital is: ", country.capital())
print("Currencies is: ", country.currencies())
print("Borders is: ", country.borders())
print("Languages is: ", country.languages())
print("Region is: ", country.region())
print("Subregion is: ", country.subregion())
print("States is: ", country.provinces())
print("Area is: ", country.area())
print("Code is: ", country.calling_codes())
print("Research more on : ", country.wiki())
print("Population is: ", country.population())
print("spelling is: ", country.alt_spellings())
print("Timezone is: ", country.timezones())
