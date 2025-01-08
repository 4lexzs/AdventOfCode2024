
def calcValues(schematic):
	values = [0, 0, 0, 0, 0]

	for line in schematic:
		for i in range(len(line)):
			if line[i] == "#":
				values[i] += 1
	return values


def getValues(schematics):
	keyValues = []
	lockValues = []

	for s in schematics:
		newS = []
		readingKey = False
		readingLock = False
		for i, line in enumerate(s):
			if i == 0 and line == len(line) * "#":
				readingKey = True
			elif i == 0 and line == len(line) * ".":
				readingLock = True
			newS.append(line)
		if readingKey:
			newS.pop(0)
			keyValues.append(calcValues(newS))
		elif readingLock:
			newS.pop()
			lockValues.append(calcValues(newS))
	
	return lockValues, keyValues


def solve(part):
	schematics = []
	ans = 0

	with open("25/input.txt", "r") as file:
		schematic = []
		for line in file:
			if line[0] == "\n":
				schematics.append(schematic)
				schematic = []
				continue
			schematic.append(line.strip())
		schematics.append(schematic)

	lockValues, keyValues = getValues(schematics)
	# calculate answer
	for lval in lockValues:
		for kval in keyValues:
			check = [x + y for x, y in zip(kval, lval) if x + y <= 5]
			if len(check) == 5:
				ans += 1

	print(ans)


if __name__ == "__main__":
	solve(1)