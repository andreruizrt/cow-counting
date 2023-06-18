from decouple import config

import cv2
from roboflow import Roboflow
import argparse
import numpy as np

import filehandler

ROBO_FLOW_API_KEY = config('ROBOFLOW_API_KEY')
PROJECT = config('PROJECT')

resourcePath = 'resources/'
datasetPath = resourcePath + 'Dataset/'
predictionsPath = resourcePath + 'Predictions/'
outputImageName = predictionsPath + "output_prediction"

rf = Roboflow(api_key=ROBO_FLOW_API_KEY)
project = rf.workspace().project("bovino-pwwpq")
model = project.version(1).model


def main():
    imagens = filehandler.getAllImagesName(datasetPath)

    for imagem in imagens:
        imagem = datasetPath + imagem
        realizarPredicao(imagem)

    # img = cv2.imread(outputImageName, cv2.IMREAD_UNCHANGED)
    # resized = redimensionarImagem(img)

    # cv2.imshow(filehandler.encontrarNomeImagem(outputImageName), resized)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


def realizarPredicao(imagePath):
    model.predict(imagePath, confidence=40, overlap=30).json()
    model.predict(imagePath, confidence=40,
                  overlap=30).save(outputImageName + "_" + filehandler.encontrarNomeImagem(imagePath))
    # print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())


def redimensionarImagem(img):
    scale_percent = 20
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    print('redimensionarImagem >> Dimensão original : ', img.shape)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    print('redimensionarImagem >> Resized Dimensions : ', resized.shape)

    return resized


main()
