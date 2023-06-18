from decouple import config

import cv2
from roboflow import Roboflow
from datetime import datetime

import re
import filehandler


ROBO_FLOW_API_KEY = config('ROBOFLOW_API_KEY')
PROJECT = config('PROJECT')

resourcePath = 'resources/'
datasetPath = resourcePath + 'Dataset/'
predictionsPath = resourcePath + 'Predictions/'
outputImageName = predictionsPath + "output_prediction"

CONFIDENCE = 40
OVERLAP = 30

rf = Roboflow(api_key=ROBO_FLOW_API_KEY)
project = rf.workspace().project(PROJECT)
model = project.version(1).model


def main():
    imagens = filehandler.getAllImagesName(datasetPath)

    for imagem in imagens:
        imagem = datasetPath + imagem
        realizarPredicao(imagem)


def realizarPredicao(imagePath):
    outputPathTimestamp = [outputImageName, str(
        datetime.timestamp(datetime.now())).replace('.', '')]

    imageCompleteOutputPath = "_".join(["_".join(outputPathTimestamp),
                                        filehandler.encontrarNomeImagem(imagePath)])
    jsonCompleteOutPath = re.sub(
        r'.JPG', '.json', imageCompleteOutputPath, flags=re.IGNORECASE)

    prediction = model.predict(
        imagePath, confidence=CONFIDENCE, overlap=OVERLAP)

    jsonPrediction = prediction.json()

    filehandler.salvarAquivoJson(jsonCompleteOutPath, jsonPrediction)
    prediction.save(imageCompleteOutputPath)

    qtdBovinos = len(jsonPrediction['predictions'])
    print("Quantidade de bovinos encontrados: " + str(qtdBovinos))

    filehandler.anotarQuantidadeEncontrados(
        imageCompleteOutputPath, qtdBovinos)

    # print(imageCompleteOutputPath)
    # print(jsonCompleteOutPath)


main()
