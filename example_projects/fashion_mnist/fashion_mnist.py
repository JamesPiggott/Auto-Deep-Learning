import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from tensorflow.keras.optimizers import Adam

class FashionMnist:

    def __init__(self):

        self.train_X = ""
        self.train_Y = ""
        self.test_X = ""
        self.test_Y = ""
        self.train_Y_one_hot = ""
        self.test_Y_one_hot = ""
        self.valid_X = ""
        self.train_label = ""
        self.valid_label = ""
        self.classes = ""
        self.model = ""
        self.history = ""
        self.epochs = ""
        self.batch_size = ""

        self.load_data()
        self.convert_data()
        self.define_model(1, 64)
        self.set_optimizer()
        self.train_model()
        self.evaluate_model()
        self.store_model("example_projects/fashion_mnist/")
        self.load_model("example_projects/fashion_mnist/")
        self.perform_inference()


    def load_data(self):
        (self.train_X, self.train_Y), (self.test_X, self.test_Y) = fashion_mnist.load_data()
        self.classes = np.unique(self.train_Y)

    def convert_data(self):
        # Image preprocessing
        self.train_X = self.train_X.reshape(-1, 28, 28, 1)
        self.test_X = self.test_X.reshape(-1, 28, 28, 1)

        # Convert image format from int8 to float32
        self.train_X = self.train_X.astype('float32')
        self.test_X = self.test_X.astype('float32')

        # Normalize pixel values to between 0 and 1
        self.train_X = self.train_X / 255
        self.test_X = self.test_X / 255

        # Convert the class labels to a boolean column
        train_Y_one_hot = to_categorical(self.train_Y)
        # test_Y_one_hot = to_categorical(self.test_Y)

        print("Result after conversion: ", train_Y_one_hot[0])

        # Split the training set into two: training and validation: 80 % and 20 % ratio
        self.train_X, self.valid_X, self.train_label, self.valid_label = train_test_split(self.train_X,train_Y_one_hot, test_size=0.2, random_state=13)



    def define_model(self, epochs, batch_size):
        self.batch_size = batch_size
        self.epochs = epochs


        # The complete model
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Conv2D(32, kernel_size=(3, 3),activation='linear',padding='same',input_shape=(28,28,1)),
            tf.keras.layers.LeakyReLU(alpha=0.1),
            tf.keras.layers.MaxPooling2D((2, 2),padding='same'),
            tf.keras.layers.Dropout(0.25),
            tf.keras.layers.Conv2D(64, (3, 3), activation='linear',padding='same'),
            tf.keras.layers.LeakyReLU(alpha=0.1),
            tf.keras.layers.MaxPooling2D(pool_size=(2, 2),padding='same'),
            tf.keras.layers.Dropout(0.25),
            tf.keras.layers.Conv2D(128, (3, 3), activation='linear',padding='same'),
            tf.keras.layers.LeakyReLU(alpha=0.1),
            tf.keras.layers.MaxPooling2D(pool_size=(2, 2),padding='same'),
            tf.keras.layers.Dropout(0.4),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation='linear'),
            tf.keras.layers.LeakyReLU(alpha=0.1),
            tf.keras.layers.Dropout(0.3),
            tf.keras.layers.Dense(10, activation='softmax')
        ])

        self.model.summary()

    def set_optimizer(self):
        self.model.compile(optimizer=Adam(),
              loss='categorical_crossentropy',
              metrics = ['accuracy'])


    def train_model(self):
        self.history = self.model.fit(self.train_X, self.train_label, batch_size=self.batch_size, epochs=10, verbose=2,validation_data=(self.valid_X, self.valid_label))

    def evaluate_model(self):
        print("Evaluating the model")

        acc      = self.history.history[     'accuracy' ]
        val_acc  = self.history.history[ 'val_accuracy' ]
        loss     = self.history.history[    'loss' ]
        val_loss = self.history.history['val_loss' ]

        #-----------------------------------------------------------
        # Retrieve a list of list results on training and test data
        # sets for each training epoch
        #-----------------------------------------------------------
        epochs   = range(len(acc)) # Get number of epochs

        #------------------------------------------------
        # Plot training and validation accuracy per epoch
        #------------------------------------------------
        plt.plot  ( epochs,     acc, label='Training')
        plt.plot  ( epochs, val_acc, label='Validation')
        plt.title ('Training and validation accuracy')
        plt.legend()
        plt.figure()

        #------------------------------------------------
        # Plot training and validation loss per epoch
        #------------------------------------------------
        plt.plot  ( epochs,     loss, label='Training')
        plt.plot  ( epochs, val_loss, label='Validation')
        plt.legend()
        plt.title ('Training and validation loss')

        plt.show()

    def store_model(self, path):
        print("Store the model")
        saved_model_path = 'my_model.h5'
        self.model.save(path + saved_model_path)
        del self.model

    def load_model(self, path):
        print("Load the model")
        saved_model_path = 'test_model.h5'
        self.model = tf.keras.models.load_model(path + saved_model_path)

    def load_image(self, filename):
        img = load_img(filename, grayscale=True, target_size=(28, 28))
        img = img_to_array(img)
        img = img.reshape(1, 28, 28, 1)
        img = img.astype('float32')
        img = img / 255.0
        return img

    def perform_inference(self):
        img = self.load_image('example_projects/fashion_mnist/test.png')
        result = self.model.predict_classes(img)
        print(result[0])