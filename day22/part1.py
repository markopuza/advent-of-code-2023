from common import library

Brick = tuple[tuple[int, int, int], tuple[int, int, int]]

def read_brick(row: str) -> Brick:
    a, b = row.split('~')
    return tuple(map(int, a.split(','))), tuple(map(int, b.split(','))), 

bricks = [read_brick(r) for r in library.read_input(22)]
bricks.sort(key=lambda x:min(x[0][2], x[1][2]))
offsets = [None] * len(bricks)
supported = [None] * len(bricks)
covered = {}
for i, ((x1,y1,z1),(x2,y2,z2)) in enumerate(bricks):
	def isok(zofs):
		touching = set()
		if z1 - zofs <= 0 or z2 - zofs <= 0:
			touching.add(-1)
		for x in range(x1,x2+1):
			for y in range(y1,y2+1):
				for z in range(z1-zofs,z2-zofs+1):
					if (x,y,z) in covered:
						touching.add(covered[x,y,z])
		return touching
	zofs = 0
	while True:
		touch = isok(zofs + 1)
		if touch:
			break
		zofs = zofs + 1
	offsets[i] = zofs
	supported[i] = touch
	for x in range(x1,x2+1):
		for y in range(y1,y2+1):
			for z in range(z1-zofs,z2-zofs+1):
				covered[x,y,z] = i

#print(supported)
unremovable = set.union(*(i for i in supported if len(i) == 1))
unremovable.remove(-1)
print(len(bricks) - len(unremovable))

cascade = [None] * len(bricks)
for i in range(len(bricks)):
	fallen = {i}
	for j in range(i+1, len(bricks)):
		if not supported[j] - fallen:
			fallen.add(j)
	cascade[i] = len(fallen) - 1
print(sum(cascade))