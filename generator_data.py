import numpy as np
import matplotlib.pyplot as plt

def gen_data_2d(ndp, solapamiento):

    #solapamiento
    spd = int(round(ndp*solapamiento,0))
    spi = -int(round(ndp*solapamiento,0))

    #elementos totales
    tdp = ndp+spd

    #Clase 1
    y1 = (-1 * np.random.randn(tdp) - 2) / 4
    x1 = np.arange(start = -ndp, stop= spd) / tdp
    z1 = np.repeat(0, y1.size)

    #Clase 2
    y2 = (np.random.randn(tdp) + 2) / 4
    x2 = np.arange(start = spi, stop=ndp) / tdp
    z2 = np.repeat(1, y2.size)

    #Uniendo Clase 1 y Clase 2
    x = np.append(x1,x2)
    y = np.append(y1,y2)
    z = np.append(z1,z2)

    #estandarizando
    y = y/y.max()

    #Creando la matriz
    d =np.array([x,y,z])

    #Graficando
    plt.scatter(d[0],d[1], c = d[2])

    #Visualizando
    plt.show()

    return d