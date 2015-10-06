from os import listdir
from os.path import isfile, join

varList=["AET","PET","PPT","RO","SOIL","SWE","TAVE"]
dim="byHRU"

#1 create/read-in necessary files
template="D:/abock/Water_Balance/MetaData/MWBM_Thredds/MWBM_aggregation_CONUS/conus-byHRU.ncml"
ncmls="D:/abock/Water_Balance/MetaData/MWBM_Thredds/MWBM_aggregation_CONUS/1_VarLevel"
xmltemplate=open(template,"r")
# open the XML template of one GCM
xmlLines=xmltemplate.readlines()
xmltemplate.close()

# get all netCDF files in the directory
ncfiles = [f for f in listdir(ncmls) if isfile(join(ncmls,f))]
ncfiles_dim = filter(lambda x:dim in x,ncfiles)

newfile = open("D:/abock/Water_Balance/MetaData/MWBM_Thredds/MWBM_aggregation_CONUS/2_DatasetLevel/conus-"+dim+".ncml","a")
newfile.writelines(xmlLines[0:5])
newfile.writelines("        <netcdf location=GSD_AET-"+dim+".ncml enhance='"'true'"'/>\n")
newfile.writelines("        <netcdf location=GSD_PET-"+dim+"ncml enhance='"'true'"'/>\n")
newfile.writelines("        <netcdf location=GSD_PPT-"+dim+".ncml enhance='"'true'"'/>\n")
newfile.writelines("        <netcdf location=GSD_RO-"+dim+".ncml enhance='"'true'"'/>\n")
newfile.writelines("        <netcdf location=GSD_SOIL-"+dim+".ncml enhance='"'true'"'/>\n")
newfile.writelines("        <netcdf location=GSD_SWE-"+dim+".ncml enhance='"'true'"'/>\n")
newfile.writelines("        <netcdf location=GSD_TAVE-"+dim+".ncml enhance='"'true'"'/>\n")
for i in range (0,len(ncfiles_dim)):
    newfile.writelines("        <netcdf location="+ncfiles_dim[i]+" enhance='"'true'"'/>\n")
newfile.writelines(xmlLines[6:8])
newfile.close()