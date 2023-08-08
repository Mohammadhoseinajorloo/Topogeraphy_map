import rasterio
import matplotlib.pyplot as plt


file = rasterio.open('data\blank.gif')
dataset = file.read()
print(dataset.shape)
