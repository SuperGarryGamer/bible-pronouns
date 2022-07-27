import re

pronouns = [
    "i", "me", "my", "mine", "myself",
    "you", "your", "yours", "yourself",
    "he", "him", "his", "himself",
    "she", "her", "hers", "herself",
    "they", "them", "their", "theirs", "themself",
    "it", "its", "itself",
    "we", "us", "our", "ours", "ourselves",
    "yourselves", "themselves",
    "thee", "thou", "thy", "thine", "thyself",
    "ye"
]

with open("asv.txt", "r") as f:
    f_data = f.read()
    pattern = re.compile(f"\\b({'|'.join(pronouns)})\\b")

    matches = re.findall(pattern, f_data)
    
    print(f"The ASV Bible countains at least {len(matches)} pronouns. \nAt least {str(len(matches) / len(f_data.split()) * 100)[:5]}% of words in the ASV Bible are pronouns.")