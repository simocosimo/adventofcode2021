f_input = open("input.txt", "r")
lines = f_input.readlines()

#building the first 3wide measure
prev = int(lines.pop(0))
prev += int(lines[0]) + int(lines[1])

count = 0
for i in range(0, len(lines)-2):
    threeWindow = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
    if threeWindow > prev:
        count += 1
    prev = threeWindow

print(f"Increments: {count}")
