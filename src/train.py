from .model import Model
from .data import Data
from .project import Project
import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator

class Train:

    model = Model
    data = Data
    project = Project
    history = ""

    def __init__(self, model, data, project):
        self.model = model
        self.data = data
        self.projecy = project
        self.history = ""

    def train_model(self, project):
        print("Train the model using the defined data set")

        # All images will be rescaled by 1./255.
        train_datagen = ImageDataGenerator( rescale = 1.0/255. )
        test_datagen  = ImageDataGenerator( rescale = 1.0/255. )

        # print(project.epochs)

        # --------------------
        # Flow training images in batches of 20 using train_datagen generator
        # --------------------
        train_generator = train_datagen.flow_from_directory("../" + self.data.train_dir,
                                                            batch_size=int(project.batch_size),
                                                            class_mode='binary',
                                                            target_size=(150, 150))     
        # --------------------
        # Flow validation images in batches of 20 using test_datagen generator
        # --------------------
        validation_generator =  test_datagen.flow_from_directory("../" + self.data.validation_dir,
                                                                batch_size=int(project.batch_size),
                                                                class_mode  = 'binary',
                                                                target_size = (150, 150))

        self.model.history = self.model.model.fit(train_generator,
                                    validation_data=validation_generator,
                                    steps_per_epoch=100,
                                    epochs=int(project.epochs),
                                    validation_steps=50,
                                    verbose=2)


    def store_model(self, path):
        print("Store the model")
        saved_model_path = "/my_model.h5"
        self.model.model.save(path + saved_model_path)