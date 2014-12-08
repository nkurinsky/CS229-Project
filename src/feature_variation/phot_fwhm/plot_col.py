from varplot import *

usedpts = 100000
ftable=getTable("training.fits",usedpts)

varplot(ftable, "mag_auto_i", "fwhm_world_i", save=False)

#or use trainplot("training.fits","mag_auto_g","fwhm_world_g")
