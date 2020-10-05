import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import morphology


image = np.load('ps.npy.txt')

struct = np.array([
    [1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
])

sum_bra = 0
sum_rec = 0

result = morphology.binary_hit_or_miss(image, structure1=struct)
bra = np.sum(result)
sum_bra += bra
print("Bracket 1: ", bra)

struct = np.rot90(struct)
result = morphology.binary_hit_or_miss(image, structure1=struct)
bra = np.sum(result)
sum_bra += bra
print("Bracket 2: ", bra)

struct = np.rot90(struct)
result = morphology.binary_hit_or_miss(image, structure1=struct)
bra = np.sum(result)
sum_bra += bra
print("Bracket 3: ", bra)

struct = np.rot90(struct)
result = morphology.binary_hit_or_miss(image, structure1=struct)
bra = np.sum(result)
sum_bra += bra
print("Bracket 4: ", bra)

print("Brackets at all: ", sum_bra)


struct = np.array([
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
])

result = morphology.binary_hit_or_miss(image, structure1=struct)
rec = np.sum(result)
sum_rec += rec
print("Rectangle 1: ", rec)

struct = np.rot90(struct)
result = morphology.binary_hit_or_miss(image, structure1=struct)
rec = np.sum(result)
sum_rec += rec
print("Rectangle 2: ", rec)

print("Rectangles at all: ", sum_rec)

plt.figure()
ax1 = plt.subplot(121)
plt.imshow(image)
ax2 = plt.subplot(122, sharex=ax1, sharey=ax1)
plt.imshow(result)
plt.show()