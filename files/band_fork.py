import calculation.makematrix
from matplotlib import pyplot as plt
import calculation.effectivemass as ef
import numpy as np

#Valence band calculation of SiGe on Si by k-p

#Plank constant / 2pi [Js]
HBAR = 1.054571596e-34

#electron mass [kg]
EM0 = 9.10938188e-31

#elementary charge [C]
EL = 1.602176462e-19

#unit of energy [eV]
e_unit = HBAR**2*1e20/(2*EM0*EL)

#SiGex
x = 0.3

Number = 100

wavenumber= np.linspace(0,0.1,Number)

filename = open("E-k_SiGe_on_Si_x{}.txt".format(x),"w")
filename.write('k[1/A]\tHH\tLH\tSO\n')

eg = ef.mass(x)
energy1 = eg[3]
energy2 = eg[4]
energy3 = eg[5]


for i in range(0,Number): 
  filename.write('{}\t{}\t{}\t{}\n'.format(wavenumber[i], energy1[i],energy2[i], energy3[i]))

plt.plot(wavenumber,energy1, 'o', label="HH")
plt.plot(wavenumber,energy2, 'o', label = "LH")
plt.plot(wavenumber,energy3,'o' ,label = "SO")
plt.xlabel(r'$Wavenumber[m^{-1}]$')
plt.ylabel("Energy[eV]")
plt.legend()
plt.show()


