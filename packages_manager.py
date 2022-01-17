from msilib.schema import Directory
import yaml
import os

packagesFolder="Packages"

class PackadgeManager():

    def __init__():
        pass

    def loadPackages():
        packages = {}
        packs = [dI for dI in os.listdir(packagesFolder) if os.path.isdir(os.path.join(packagesFolder,dI))]
        for p in packs:
            loc = packagesFolder+"/"+p+"/package.cfg"
            dir = packagesFolder+"/"+p+"/"
            if not os.path.isfile(loc):
                continue
            with open(loc, "r") as stream:
                try:
                    data = yaml.safe_load(stream)
                    if os.path.isfile(dir+"/DISABLED"):
                        data['disabled']=True
                    packages[data['name']] = data
                except:
                    print("error")
        return packages