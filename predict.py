from helper import *
import os
import csv
import scipy
from scipy import ndimage
import pickle
num_px = 64;

parameters = pickle.load( open( "weights.p", "rb" ) )
train_x_orig, train_y, test_x_orig, test_y, classes = load_data()

count = 0;
for file in os.listdir("./dataBen/TestimageRes"):
    print(file)
    if(count < 10):
        my_label_y = [0]
    else:
        my_label_y = [1]
    fname = "./dataBen/TestImageRes/" + file

    image = np.array(ndimage.imread(fname, flatten=False))
    my_image = scipy.misc.imresize(image, size=(num_px,num_px)).reshape((1, num_px*num_px*3)).T

    #my_predicted_image = predict(parameters["W2"], parameters["b2"], my_image)
    my_predicted_image = predict(my_image, my_label_y, parameters)

    plt.imshow(image)
    print("y = " + str(np.squeeze(my_predicted_image)) + ", your algorithm predicts a \"" + classes[int(np.squeeze(my_predicted_image)),].decode("utf-8") +  "\" picture.")

    count += 1
    print(count)
