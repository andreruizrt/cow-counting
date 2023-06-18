import os

import cv2
import json



RESOURCE_DEFAULT = "resource/"
DIRETORIO_DEFAULT_DATASET = "Dataset/"
DIRETORIO_DEFAULT_PREDICTIONS = "Predictions/"


def getAllImagesName(diretorio):
    if diretorio == "":
        diretorio = DIRETORIO_DEFAULT

    images = os.listdir(diretorio)

    return images


def encontrarNomeImagem(pathToImage):
    string = pathToImage
    parts = string.split('/')

    if len(parts) > 1:
        palavra = parts[-1]
        return palavra
    else:
        return parts


def anotarQuantidadeEncontrados(pathToImage, quantidade):
    image = cv2.imread(pathToImage)

    text = 'Bovinos: ' + str(quantidade)

    position = (10, 120)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 5
    font_color = (255, 255, 0)
    line_type = 2

    cv2.putText(image, text, position, font, font_scale, font_color, line_type)

    cv2.imwrite(pathToImage, image)


def redimensionarImagem(img):
    scale_percent = 20
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    print('redimensionarImagem >> Dimensão original : ', img.shape)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    print('redimensionarImagem >> Resized Dimensions : ', resized.shape)

    return resized


def salvarAquivoJson(caminhoArquivo, conteudo):
    with open(caminhoArquivo, "w") as arquivo:
        json.dump(conteudo, arquivo)


