
import numpy as np
import sys

sys.path.append(r"C:\repos\po3\.env\Lib\site-packages\po3")

import po3

o = po3.axpy(
    2, 
    np.array([34], dtype=float), 
    np.array([34], dtype=float)
    )



print(o)