import os

DIRETORIO_DEFAULT = "resource/Dataset/"


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
