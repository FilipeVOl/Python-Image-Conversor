from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

file = "./image.jpg"  # Caminho do arquivo da imagem
img = Image.open(file)  # Abre a imagem
img_data = img.getdata()  # Obtém os dados da imagem (pixels)

lst = []
for i in img_data:
    lst.append(i[0]*0.2125 + i[1]*0.7154 + i[2]*0.0721)  # Converte os pixels para escala de cinza usando a fórmula de luminância

new_img = Image.new("L", img.size)  # Cria uma nova imagem em escala de cinza
new_img.putdata(lst)  # Adiciona os dados de escala de cinza à nova imagem

threshold = 128  # Valor de limiar para converter escala de cinza para preto e branco
bw_lst = [255 if pixel > threshold else 0 for pixel in lst]  # Converte os pixels de escala de cinza para preto e branco

bw_img = Image.new("L", img.size)  # Cria uma nova imagem em preto e branco
bw_img.putdata(bw_lst)  # Adiciona os dados de preto e branco à nova imagem

# Mostrar as três imagens lado a lado
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].imshow(img)
axs[0].set_title('Original')
axs[0].axis('off')

axs[1].imshow(new_img, cmap='gray')
axs[1].set_title('Escala de Cinza')
axs[1].axis('off')

axs[2].imshow(bw_img, cmap='gray')
axs[2].set_title('Preto e Branco')
axs[2].axis('off')

plt.show()