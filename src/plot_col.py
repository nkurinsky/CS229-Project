from varplot import *

ftable=getTable("../../data/training.fits")
#vhistplot(ftable, "mag_auto_g", save=False)
varplot(ftable,"mag_auto_y","fwhm_world_y")
