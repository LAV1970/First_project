def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone

def get_country_code(phone):
    country_codes = {
        "380": "UA",
        "81": "JP",
        "886": "TW",
        "65": "SG"
    }
    
    for code, country in country_codes.items():
        if phone.startswith(code):
            return country
    return "UA"

def get_phone_numbers_for_countries(list_phones):
    countries = {
        "UA": [],
        "JP": [],
        "TW": [],
        "SG": []
    }

    for phone in list_phones:
        cleaned_phone = sanitize_phone_number(phone)
        country_code = get_country_code(cleaned_phone)
        
        if country_code in countries:
            countries[country_code].append(cleaned_phone)

    return countries

list_phones = [
    '380998759405',
    '818765347',
    '8867658976',
    '657658976'
]

result = get_phone_numbers_for_countries(list_phones)
print(result)
