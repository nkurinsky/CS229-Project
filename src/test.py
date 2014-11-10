import pyfits

f = pyfits.open("../Data/round1/round1_test_set.fits")
tbdata = f[1].data
print tbdata[:2]