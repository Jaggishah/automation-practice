#  shutil is module to copy the file wich will take source and destination
import shutil,os,pathlib
from pathlib import Path as pi

path = pi.home()

shutil.copy(source,destination)
#  copy folder
shutil.copytree(source,destination)
shutil.move(source,destination)