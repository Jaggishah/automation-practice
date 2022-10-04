import os
from pathlib import Path as pi
import send2trash

for filename in pi.home().glob('*.txt'):
    # os.unlink(filename)
    send2trash.send2trash(filename)
    print(filename)