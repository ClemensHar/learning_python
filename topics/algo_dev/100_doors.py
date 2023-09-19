doors = [False] * 101  # ignore the first door and use the doornumber as index
print(doors[1:])

for ipass in range(1, len(doors)):
    print(f"Pass: {ipass}")
    idoor = ipass
    while idoor < len(doors):
        print(f"Toggle door: {idoor}")
        doors[idoor] = not doors[idoor]
        idoor = idoor + ipass

for door_number in range(1, len(doors)):
    if doors[door_number]:
        print(door_number)

# alternative
doors = [False] * 101
print(doors)

for ipass in range(1, len(doors)):
    for idoor in range(ipass, len(doors), ipass):
        doors[idoor] = not doors[idoor]

for door_number in range(1, len(doors)):
    if doors[door_number]:
        print(door_number)
