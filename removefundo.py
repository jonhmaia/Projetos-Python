from rembg import remove
from PIL import Image

img = Image.open(
    #nome da imagem 
    #name of image
    "C:/Users/João Marcos/Downloads/game-of-thrones-house-targaryen-4k-kk-1366x768.jpg"
)
imgnotfound = remove(img)
imgnotfound.save('semfundo.png')
