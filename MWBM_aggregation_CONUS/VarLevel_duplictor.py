# This file writes complete metadata files for each GF region on the
# MWBM database
def varWriter (xLines,climateDS,DSdim,region):
    newfile = open("d:/abock/Water_Balance/MetaData/MWBM_Thredds/MWBM_aggregation_CONUS/1_VarLevel/"+climateDS+"-"+DSdim+".ncml","w")
    xmlLines_copy=list(xLines)
    xmlLines_copy[2]=xmlLines_copy[2].replace("DSname",climateDS)
    xmlLines_copy[2]=xmlLines_copy[2].replace("DSdim",DSdim)
    xmlLines_copy[5]=xmlLines_copy[5].replace("DSname",climateDS)
    xmlLines_copy[5]=xmlLines_copy[5].replace("DSdim",DSdim)
    xmlLines_copy[8]=xmlLines_copy[8].replace("DSname",climateDS)
    xmlLines_copy[8]=xmlLines_copy[8].replace("DSdim",DSdim)
    xmlLines_copy[11]=xmlLines_copy[11].replace("DSname",climateDS)
    xmlLines_copy[11]=xmlLines_copy[11].replace("DSdim",DSdim)
    xmlLines_copy[14]=xmlLines_copy[14].replace("DSname",climateDS)
    xmlLines_copy[14]=xmlLines_copy[14].replace("DSdim",DSdim)
    xmlLines_copy[17]=xmlLines_copy[17].replace("DSname",climateDS)
    xmlLines_copy[17]=xmlLines_copy[17].replace("DSdim",DSdim)
    xmlLines_copy[20]=xmlLines_copy[20].replace("DSname",climateDS)
    xmlLines_copy[20]=xmlLines_copy[20].replace("DSdim",DSdim)
    xmlLines_copy[24]=xmlLines_copy[24].replace("DSname",climateDS)
    xmlLines_copy[24]=xmlLines_copy[24].replace("DSdim",DSdim)
    newfile.writelines(xmlLines_copy)
    newfile.close()
    del xmlLines_copy

from os import listdir
from os.path import isfile, join

region="r01"
varList=["AET","PET","PPT","RO","SOIL","SWE","TAVE"]
dim="byHRU"

#1 create/read-in necessary files
template="D:/abock/Water_Balance/MetaData/MWBM_Thredds/MWBM_aggregation_CONUS/VarLevelTemp_"+dim+".ncml"
netCDFs="F:/Yeti/ncdf_scripts/"+region
xmltemplate=open(template,"r")
# open the XML template of one GCM
xmlLines=xmltemplate.readlines()
xmltemplate.close()
# using suffix for ncml
# http://www.unidata.ucar.edu/software/thredds/v4.3/tds/tutorial/NcML.htm


# get all netCDF files in the directory
ncfiles = [ f for f in listdir(netCDFs) if isfile(join(netCDFs,f)) ]
bcsd = filter(lambda x:'BCSD'in x,ncfiles)
bcsd_hru = filter(lambda x:'SEG'in x,bcsd)
gcm_only=[f[12:-9] for f in bcsd_hru]
#gcmNames=[]
#gcmNames=str.split(bcsd,"-")

#allStr=[words for segments in bcsd for words in segments.split("-")]
#gcmStr=yohoho[6::8]

for i in range(0,len(gcm_only)):
    varWriter(xmlLines,gcm_only[i][11:],dim,region)

