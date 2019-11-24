from PIL import Image

import os
import sys

image = 'image.png'

def Convert():
  try:
    Image.open(image).save('image.jpg')
  except IOError as e:
    print(e)


def Main():
  Convert()


Main()
