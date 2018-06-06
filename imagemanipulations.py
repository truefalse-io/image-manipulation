#TrueFalse
import matplotlib
import numpy
import scipy

from matplotlib import pyplot
from matplotlib import cm
from scipy import ndimage
from scipy import signal

def main():
    '''Call functions'''
    filename = "f_211_193_171_1024.png"
    transpose_image(filename)
    color_separation(filename)
    grayscale(filename)
    sobel_filter(filename)

def transpose_image(filename):
    '''Transpose image '''
    array = scipy.ndimage.imread(filename)
    array_transposed = numpy.swapaxes(array, 0, 1)
    print "Dimensions is", array.shape
    print "Data type is", array.dtype
    pyplot.imshow(array_transposed)
    pyplot.legend()
    pyplot.title('Transposed image')
    pyplot.xlabel('X-axis [pixels]')
    pyplot.ylabel('Y-axis [pixels]')
    pyplot.savefig('transposed_image.pdf')
    pyplot.show()

def color_separation(filename):
    '''Color separation in red, green en blue'''
    ar = scipy.ndimage.imread(filename)
    ar_r = ar[:,:,0]
    ar_g = ar[:,:,1]
    ar_b = ar[:,:,2]
    pyplot.figure(1)
    pyplot.suptitle('Color separation')
    pyplot.subplot(221)
    pyplot.imshow(ar)
    pyplot.title('RGB-image')
    pyplot.xticks([])
    pyplot.yticks([])
    pyplot.subplot(222)
    pyplot.imshow(ar_r, cmap=cm.Reds_r)
    pyplot.title('Red channel')
    pyplot.xticks([])
    pyplot.yticks([])
    pyplot.subplot(223)
    pyplot.imshow(ar_g, cmap=cm.Greens_r)
    pyplot.title('Green channel')
    pyplot.xticks([])
    pyplot.yticks([])
    pyplot.subplot(224)
    pyplot.imshow(ar_b, cmap=cm.Blues_r)
    pyplot.title('Blue channel')
    pyplot.xticks([])
    pyplot.yticks([])
    pyplot.savefig('color_separation.pdf')
    pyplot.show()

def grayscale(filename):
    '''Plotting a grayscale image '''
    arr = scipy.ndimage.imread(filename)
    arr_r = arr[:,:,0]
    arr_g = arr[:,:,1]
    arr_b = arr[:,:,2]
    arr_gray = arr_r*0.299 + arr_g*0.587 + arr_b*0.114
    pyplot.imshow(arr_gray, cmap=cm.gray)
    pyplot.legend()
    pyplot.title('Grayscale image')
    pyplot.xlabel('X-axis [pixels]')
    pyplot.ylabel('Y-axis [pixels]')
    pyplot.savefig('grayscale.pdf')
    pyplot.show()

def sobel_filter(filename):
    '''Detecting edges using Sobel filter '''
    a = scipy.ndimage.imread(filename)
    a_r = a[:,:,0]
    a_g = a[:,:,1]
    a_b = a[:,:,2]
    a_gray = a_r*0.299 + a_g*0.587 + a_b*0.114
    gx = numpy.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
    gy = numpy.array([[-1, -2, -1],[0, 0, 0],[1, 2, 1]])
    a_gx = signal.convolve(a_gray, gx)
    a_gy = signal.convolve(a_gray, gy)
    g = numpy.sqrt((a_gx*a_gx) + (a_gy*a_gy))
    pyplot.figure(1)
    pyplot.suptitle('Sobel filtered images')
    pyplot.subplot(221)
    pyplot.imshow(a_gray, cmap=cm.gray)
    pyplot.title('Grayscale')
    pyplot.xticks([])
    pyplot.yticks([])
    pyplot.subplot(222)
    pyplot.imshow(a_gx, cmap=cm.gray)
    pyplot.title('x-gradient')
    pyplot.xticks([])
    pyplot.yticks([])
    pyplot.subplot(223)
    pyplot.imshow(a_gy, cmap=cm.gray)
    pyplot.title('y-gradient')
    pyplot.xticks([])
    pyplot.yticks([])
    pyplot.subplot(224)
    pyplot.imshow(g, cmap=cm.gray)
    pyplot.title('Sobel filtered')
    pyplot.xticks([])
    pyplot.yticks([])
    pyplot.savefig('sobel_filtered.pdf')
    pyplot.show()

if __name__=='__main__':
    main()
