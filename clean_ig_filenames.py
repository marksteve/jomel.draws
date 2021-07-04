from glob import glob
from pathlib import Path

for image in glob("*.jpg*"):
    Path(image).rename(image.split('?')[0])
