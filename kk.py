from PIL import Image

image = Image.open('secret.png')

image.show()

print(image.size)

new_image = image.resize((128,128))

new_image.save('secret2.png')

print(new_image.size)