#TrueFalse
import matplotlib
import numpy

from matplotlib import pyplot

def planck_function():
    '''Plot planck function'''
    h = 6.6262e-34
    c = 2.998e+17
    k_b = 1.38e-23
    temp1 = 5000
    temp2 = 6000
    w = numpy.linspace(100, 2000, num=100)
    planck = (2.0*h*c**2)/ ((w**5)*(numpy.exp(h*c/(w*k_b*temp1))-1.0))
    planck2 = (2.0*h*c**2)/ ((w**5)*(numpy.exp(h*c/(w*k_b*temp2))-1.0))
    pyplot.plot(w, planck, 'k', label='Temp = 3000 K')
    pyplot.plot(w, planck2, 'b', label='Temp = 5500 K')
    pyplot.legend()
    pyplot.title('Planck Function')
    pyplot.xlabel('Wavelength [nm]')
    pyplot.ylabel('Intensity [W sr^-1 m^-3]')
    pyplot.savefig('planck_function.pdf')
    pyplot.show()

if __name__=='__main__':
    planck_function()
