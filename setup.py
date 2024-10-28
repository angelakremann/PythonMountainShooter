from ast import _new

import asset
from cx_Freeze import setup, Executable
import os

path= "./asset"
asset_list = os.listdir(path)
asset_list_completa = [os.path.join(path, asset).replace(_old:"\\", _new"\") for asset in asset_list]
print(asset_list_completa)

class Executable:
    pass


setup(
    name="MountainShooter",
    version="1.0",
    description="Mountain Shooter app",
    options= {"build_exe": dict(packages=["pygame"])},
    executables=executables

)


