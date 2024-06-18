import re

#1
#Task 1. 
text = "Contact emails are: john.doe@example.com and jane.doe@example.com."

emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text, re.IGNORECASE)
print(emails)

#2
#Task 1. 
text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com)[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", text)
print(emails)

#3
#Task 1.
text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"

occupation_match = re.search(r"Occupation: ([^;]+)", text)
if occupation_match:
    occupation = occupation_match.group(1)
    print(f"Occupation: {occupation}")
else:
    print("Occupation not found in the text.")

#4.
#Task 1. 
descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]

keyword_categories = {
    "Smartphone": "Electronics",
    "Cotton t-shirt": "Apparel",
    "Stainless steel kitchen knife set": "Home & Kitchen"
}

tagged_products = []
for desc in descriptions:
    for keyword, category in keyword_categories.items():
        if keyword.lower() in desc.lower():
            tagged_products.append((desc, category))
            break  

for product, category in tagged_products:
    print(f"Product: {product} | Category: {category}")

#5.
#Task 1. 