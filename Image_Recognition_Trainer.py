# Using Python Image Library to explore how to process an image
# from PIL import Image

# input and display a cat image
# cat_image_pathname = '/Users/owl/Desktop/Images/Image Recognition Resized Images/CAT.jpeg'
# cat_image = Image.open(cat_image_pathname)
# cat_image.show()

# input and display an image by it's pathname
# display_image_pathname = input('Enter image pathname: ')
# display_image = Image.open(display_image_pathname)
# display_image.show()

# defining labels of images in CIFAR 10 dataset
labels = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

from keras.datasets import cifar10

(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# Exploring CIFAR 10 dataset
# index = int(input('Enter an image index: '))
# display_image = X_train[index]
# display_label = y_train[index][0]
#
# from matplotlib import pyplot as plt
#
# red_image = Image.fromarray(display_image)
# red, green, blue = red_image.split()
# recreating image using matplotlib
# plt.imshow(red, cmap="Reds")
# plt.show()

from keras.utils import np_utils
new_X_train = X_train.astype('float32')
new_X_test = X_test.astype('float32')
new_X_train /= 255
new_X_test /= 255
new_Y_train = np_utils.to_categorical(y_train)
new_Y_test = np_utils.to_categorical(y_test)

from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.optimizers import SGD
from keras.constraints import maxnorm

# creating keras layers to process images
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(32, 32, 3), activation='relu', padding='same', kernel_constraint=maxnorm(3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(512, activation='relu', kernel_constraint=maxnorm(3)))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

# model optimization
model.compile(loss='categorical_crossentropy', optimizer=SGD(lr=0.01), metrics=['accuracy'])
# fitting model to training dataset
model.fit(new_X_train, new_Y_train, epochs=10, batch_size=32)

#saving trained model to avoid recompilation everytime the model runs
model.save('Trained_model.h5')


