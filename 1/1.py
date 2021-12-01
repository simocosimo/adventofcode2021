f_input = open("input.txt", "r")
lines = f_input.readlines()

prev = int(lines.pop(0))
count = 0
for l in lines:
    if int(l) > prev:
        count += 1
    prev = int(l)

print(f"Increments: {count}")
    
