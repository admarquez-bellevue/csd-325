def city_country(city, country, population=None, language=None):
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result

print(city_country("omaha", "united states"))
print(city_country("lima", "peru", 10092000))
print(city_country("paris", "france", 2102360, "french"))