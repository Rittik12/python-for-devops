import re

text = "The quick brown fox"
pattern = "quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match)
else:
    print("No match")