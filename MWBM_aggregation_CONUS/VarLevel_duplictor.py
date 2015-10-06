# This file writes complete metadata files for each GF region on the
# MWBM database
def varWriter (xLines,climateDS,var,DSdim,region):
    newfile = open("d:/abock/Water_Balance/MetaData/MWBM_Thredds/MWBM_aggregation_CONUS/1_VarLevel/"+climateDS+"_"+var+"-"+DSdim+".ncml","w")
    xmlLines_copy=list(xLines)
    xmlLines_copy[2]=xmlLines_copy[2].replace("VAR",var)
    xmlLines_copy[2]=xmlLines_copy[2].replace("DSname",climateDS+"_"+var)
    xmlLines_copy[2]=xmlLines_copy[2].replace("DSdim",DSdim)
    xmlLines_copy[6]=xmlLines_copy[6].replace("DSname",climateDS)
    xmlLines_copy[2]=xmlLines_copy[6].replace("DSdim",DSdim)
    newfile.writelines(xmlLines_copy)
    newfile.close()
    del xmlLines_copy

from os import listdir
from os.path import isfile, join

region="r01"
varList=["AET","PET","PPT","RO","SOIL","SWE","TAVE"]
dim="byHRU"

#1 create/read-in necessary files
template="D:/abock/Water_Balance/MetaData/MWBM_Thredds/MWBM_aggregation_CONUS/VarLevelTemp.ncml"
netCDFs="F:/Yeti/ncdf_scripts/"+region
xmltemplate=open(template,"r")
# open the XML template of one GCM
xmlLines=xmltemplate.readlines()
xmltemplate.close()

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
    varWriter(xmlLines,gcm_only[i][11:],"AET","byHRU",region)
    varWriter(xmlLines,gcm_only[i][11:],"PET","byHRU",region)
    varWriter(xmlLines,gcm_only[i][11:],"PPT","byHRU",region)
    varWriter(xmlLines,gcm_only[i][11:],"RO","byHRU",region)
    varWriter(xmlLines,gcm_only[i][11:],"SOIL","byHRU",region)
    varWriter(xmlLines,gcm_only[i][11:],"SWE","byHRU",region)
    varWriter(xmlLines,gcm_only[i][11:],"TAVE","byHRU",region)
    varWriter(xmlLines,gcm_only[i][11:],"AET","bySEG",region)
    varWriter(xmlLines,gcm_only[i][11:],"PET","bySEG",region)
    varWriter(xmlLines,gcm_only[i][11:],"PPT","bySEG",region)
    varWriter(xmlLines,gcm_only[i][11:],"RO","bySEG",region)
    varWriter(xmlLines,gcm_only[i][11:],"SOIL","bySEG",region)
    varWriter(xmlLines,gcm_only[i][11:],"SWE","bySEG",region)
    varWriter(xmlLines,gcm_only[i][11:],"TAVE","bySEG",region)
