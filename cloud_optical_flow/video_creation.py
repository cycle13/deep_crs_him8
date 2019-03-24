import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import xarray as xr


fig = plt.figure()
ds = xr.open_dataset("/data/sat_precip/H8_Flow.nc")
print(ds)
print(ds.time)

ims = []
for i in range(350):
    im = plt.imshow(ds["B7"][i,:,:], animated=True)
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)

ani.save('clouds.mp4')
