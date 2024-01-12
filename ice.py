# -*- coding: utf-8 -*-
import arcpy
from arcpy.ia import *

def Model():

    #the goal of this is to carry out a raster calculator
    #it takes the two different ice inputs and takes the difference between them
    arcpy.env.overwriteOutput = False

    # Check out any necessary licenses.
    arcpy.CheckOutExtension("spatial")
    arcpy.CheckOutExtension("ImageAnalyst")

    # Model Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"G:\586\MyProject5\MyProject5.gdb", workspace=r"G:\586\MyProject5\MyProject5.gdb"):
        #2020 ice data. Red is higher ice and blue is lower
        Sea_ice_2022_tif = arcpy.Raster("Sea_ice_2022.tif")

        #same thing but in 1990.
        Sea_ice_1990_tif = arcpy.Raster("Sea_ice_1990.tif")

        # Process: Raster Calculator (2) (Raster Calculator) (ia)
        sea_ice_2022_2_ = "g:\\586\\myproject5\\myproject5.gdb\\sea_ice_2022"
        Raster_Calculator_2_ = sea_ice_2022_2_
        with arcpy.EnvManager(scratchWorkspace=r"G:\586\MyProject5\MyProject5.gdb", workspace=r"G:\586\MyProject5\MyProject5.gdb"):
            sea_ice_2022_2_ =  Sea_ice_2022_tif - Sea_ice_1990_tif
            sea_ice_2022_2_.save(Raster_Calculator_2_)


if __name__ == '__main__':
    Model()
