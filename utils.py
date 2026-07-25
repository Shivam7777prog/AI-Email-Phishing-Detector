import re

# List of suspicious phishing words
keywords = [
    "urgent",
    "verify",
    "password",
    "bank",
    "click",
    "account",
    "login",
    "winner",
    "gift",
    "otp",
    "security",
    "limited",
    "confirm",
    "update"
]

# Find suspicious words
def find_keywords(text):

    text = text.lower()

    found = []

    for word in keywords:
        if word in text:
            found.append(word)

    return found


# Find URLs
def count_urls(text):

    urls = re.findall(r'https?://\S+|www\.\S+', text)

    return urls