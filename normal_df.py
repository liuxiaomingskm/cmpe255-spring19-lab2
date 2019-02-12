import numpy as np
import math
def normal_pdf(x, mu=0, sigma=1):
    y_sig = np.exp(-(x - mu) ** 2 /(2* sigma**2))/(math.sqrt(2*math.pi)*sigma)
    return y_sig