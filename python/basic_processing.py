from PIL import Image

image = 'image.JPG'

def Convert():
  Image.open(image).save('image.png')

def main():
  Convert()

main()
