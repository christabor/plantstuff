"""OCR conversion for generating data from images."""
from pprint import pprint as ppr

try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

from plantstuff.core.decorators import cached

# E.g. `which tesseract`
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'


def get_image_data(img):
    """Get image data and clean-up."""
    fpath = 'ocr_images/{}'.format(img)
    ref_name = fpath.replace('/', '__').replace('.', '___') + '.txt'

    @cached(ref_name, directory='ocr_images')
    def get():
        img = Image.open(fpath)
        res = pytesseract.image_to_string(img)
        ppr(res)
        return res
    return get()


get_image_data('threatened_taxa.jpg')
