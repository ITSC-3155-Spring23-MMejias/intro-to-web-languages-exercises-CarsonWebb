import numpy
from numpy.random import default_rng

list=default_rng().random((10))
mean=numpy.mean(list)
median=numpy.median(list)
sdev=numpy.std(list)
print(f'Random numbers: {list}')
print(f'Mean: {mean}, Median: {median}, Standard Deviation: {sdev}')