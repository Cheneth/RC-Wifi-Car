import numpy as np
import cv2 as cv


'''
Want to load data here from .npz file and parse through itself.
'''
class NeuralNetwork(self):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.network = None
        self.layerSize = np.int32([100,70,4])

    def make(self):
        self.network = cv.ml.ANN_MLP_create()
        self.network.setLayerSizes(self.layerSize)
        self.network.setActivation(cv.ml.ANN_MLP_SIGMOID_SYM, 2, 1)
        self.network.setTrainMethod(cv.ml.ANN_MLP_BACKPROP)
        self.network.setTermCriteria(cv.TERM_CRITERIA_COUNT, 250, 0.001)

    def train(self): #data loaded from .npz
