from PIL import Image, ImageOps
import glob, os
import sys

extensions = ['.jpg', '.jpeg', '.png']

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

else:
    split_ext = sys.argv[-1].split('.')
    new_ext = "." + split_ext[-1]
    if new_ext in extensions:
        with Image.open('shirt.png') as img:
            size = img.size
            shirt = ImageOps.fit(image = img, size = size,  bleed=0.0)

        for infile in glob.glob(sys.argv[1]):
            file, ext = os.path.splitext(infile)
        try:
            with Image.open(sys.argv[1]) as img:
                right, lower = img.size[0], img.size[1]
                (left, upper, right, lower) = (0, 0, right, lower)
                img = img.crop((left, upper, right, lower))
                muppet = ImageOps.fit(image=img, size=size, bleed=0.0)
        except FileNotFoundError:
            sys.exit('Input does not exist')

        else:
            if ext == new_ext:
                muppet.paste(shirt, shirt)
                muppet.show()
                muppet.save(sys.argv[-1])
            else:
                sys.exit('Input and output have different extensions')

    else:
        sys.exit('Invalid output')

