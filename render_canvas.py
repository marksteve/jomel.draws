from colorthief import ColorThief
from PIL import Image
import spectra

from pathlib import Path
from glob import glob

image_size = 320
cols = 12
rows = 8

if __name__ == "__main__":
    images = sorted(glob("style_images/*.jpg"))
    image_values = []
    for image in images:
        color_thief = ColorThief(image)
        rgb = spectra.rgb(*color_thief.get_color())
        value = rgb.to("hsl").values[0]
        image_values.append((image, value))
    sorted_images = map(lambda x: x[0], sorted(image_values, key=lambda x: x[1]))
    canvas_size = (image_size * cols, image_size * rows * 2)
    canvas = Image.new("RGB", canvas_size, "white")
    for i, image in enumerate(sorted_images):
        x = i % cols
        y = i // cols
        img = Image.open(image)
        canvas.paste(img, (x * image_size, y * image_size * 2))
        try:
            ns_image = Path("output") / Path(image).name
            ns_img = Image.open(ns_image).resize(
                (image_size, image_size), Image.ANTIALIAS
            )
            canvas.paste(ns_img, (x * image_size, y * image_size * 2 + image_size))
        except Exception as e:
            print(e)
    canvas.save("output.png")
