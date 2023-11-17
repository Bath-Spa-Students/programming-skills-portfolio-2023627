#Rivers
rivers = {"Nile": "Egypt", "Chenab": "Pakistan", "Chorokhi": "Turkey" }

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

print("\nRivers:")
for river in rivers.keys():
    print(river)

print("\nCountries:")
for country in rivers.values():
    print(country)