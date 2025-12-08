zeroesfound = 0
location = 50
with open("Q1 inputs.txt") as file:
    for line in file:
        amount = int(line.strip()[1:])
        multiplier = 1 if line[0] == "R" else -1
        location = (location + (amount * multiplier)) % 100
        zeroesfound += 1 if location == 0 else 0
print(f"There were {zeroesfound} zeroes.")