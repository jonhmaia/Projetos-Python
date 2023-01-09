from PIL import Image

img = Image.open('image.jpg')
mirror_img = img.transpose(Image.FLIP_LEFT_RIGHT)
mirror_img.save('img_espelhada.png')