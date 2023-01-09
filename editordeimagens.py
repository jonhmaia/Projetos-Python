from PIL import Image
from rembg import remove
from PIL import Image

x = int(input("Digite a opção: "))

img = Image.open('nameofimage.jpg')
#espelhar a imagem
if x == 1:
    mirror_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    mirror_img.save('img_espelhada.png')
#remover o fundo
elif x == 2:
    imgnotfound = remove(img)
    imgnotfound.save('semfundo.png')
#comprimir imagem
elif x == 3:
    img.save(
        #nome que você quer dar pra imagem dps de salvar
        'img_compressed.jpg',
        'JPEG',
        optimize=True,
        quality=10)
