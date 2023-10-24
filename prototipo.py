#Prototipo#

from datetime import *
from pandas import *
from random import *
from numpy import *
import scipy.stats

print("Inicio",datetime.now()) #hora de inicio#

lam=10 #parámetro para entradas en unidades por hora#
dias=6 #duración de la simulación en días#
tmax=dias*16 #tiempo total de simulación#
mu=1 #media para distribución de tiempos de atención#

print("Generación de entradas") #Generación de entradas#
n=0 #contador de elementos#
leaux=[] #lista de tiempos de entrada generados#
te=0 #variable tiempo#
le=[] #lista de tiempos de entrada#
while te < tmax: #condición para detener la generación#
    n=n+1 #aumento de contador de entradas#
    eiaux=-log(random.uniform(0,1))/lam #generar tiempos de entradas#
    leaux.append(eiaux) #agregar a la lista de tiempos generados#
    te=te+eiaux #acumular tiempo#
    le.append(te) #agregar a la lista de tiempos de entrada#
print(le)

#m.to_csv("C:/Users/gueta/OneDrive/Documentos/Hafith Docs/ESFM/Tesis")

print("Fin",datetime.now()) #hora de fin#
