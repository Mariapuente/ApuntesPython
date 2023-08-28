import pandas as pd
from MiPaquete.mimodulo2 import funcion_mimodulo2
import numpy as np



if __name__ == "__main__": # Este es el main de Python

   funcion_mimodulo2()

   d = {'col1':[1,2], 'col2':[3,4]}
   df = pd.DataFrame(data=d)
   print(df)  

   a = np.zeros((5,3)) # Le estoy pasando las dimensiones de mi array pero rellenandolo solo con ceros
   print(a)
   