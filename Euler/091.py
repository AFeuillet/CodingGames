from utils import *

def dist(x0, y0, x1, y1):
	return (x1 - x0) ** 2 + (y1 - y0) ** 2

maxi = 50
total = 0
pythas = []
for i in range(0, maxi + 1):
	for j in range(0, maxi + 1):
		AB = dist(0, 0, i, j)
		for k in range(0, maxi + 1):
			for l in range(0, maxi + 1):
				AC = dist(0, 0, k , l)
				BC = dist(i, j, k , l)
				area = i * l - k * j
				if area != 0 and is_pytha(AB, AC, BC):
					total += 1
print(int(total / 2))
