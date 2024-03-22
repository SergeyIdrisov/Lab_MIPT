import numpy as np
import matplotlib.pyplot as plt
from math import log


def getting_k_b_from_data(x, y, sigma_x, sigma_y, need_b=True):
    if len(x) != len(y):
        return

    n = len(x)
    x = np.array(x)
    y = np.array(y)
    sigma_x = np.array(sigma_x)
    sigma_y = np.array(sigma_y)

    my = np.mean(y)
    mx = np.mean(x)
    mx2 = np.mean(x ** 2)
    my2 = np.mean(y ** 2)
    mxy = np.mean(y * x)

    if need_b:
        # y = kx + b
        k = (mxy - my * mx) / (mx2 - mx ** 2)
        # print(f"k = ({mxy} - {my} * {mx}) / ({mx2} - {mx}**2) = {k}")
        b = my - k * mx

        sigma_k = (1 / n ** 0.5) * ((my2 - my ** 2) / (mx2 - mx ** 2) - k ** 2) ** 0.5
        sigma_b = sigma_k * (mx2 - mx * mx) ** 0.5
        return x, y, sigma_x, sigma_y, k, sigma_k, b, sigma_b
    else:
        # y = kx
        k = mxy / mx2

        sigma_k = (1 / n ** 0.5) * (my2 / mx2 - k ** 2) ** 0.5

        return x, y, sigma_x, sigma_y, k, sigma_k