country_code = {"India" : "0091",
                "Australia" : "0025",
                "Nepal" : "00977"}

#Search dictionary for country code of India
print("Country Code for India: ")
print(country_code.get("India", "Not Found"))

#Search dictionary for country code of Japan
print("Country Code for Japan: ")
print(country_code.get("Japan", "Not Found"))