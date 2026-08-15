import sys

type = sys.argv[1]
if type == "t2.micro":
    print("okay, charge is $2")
elif type == "t2.large":
    print("charge is $3")
elif type == "t2.medium":
    print("charge is $4")
else:
    print("sorry, input is not valid")