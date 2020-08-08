import tensorflow as tf


class Converter:

    """Contains functions to create SavedModel and convert model to other formats.
       Options include:
       - SavedModel (TensorFlow Core)
       - JSON (TensorFlow.js)
       - tflite (TensorFlow Lite)
    
    
    """
    def __init__(self):
        self.model_format = ""

    def create_saved_model(self, model, export_path):
        model.model.save(export_path)

    def from_keras_to_json(self):
        # saved_model_path = "./{}.h5".format(int(time.time()))

        # model.save(saved_model_path)

        # command line argument
        # !tensorflowjs_converter --input_format=keras {saved_model_path} ./

        print("from_keras_to_json")


    def from_saved_model_to_tflite(self):
        print("from_saved_model_to_tflite")


    def from_keras_to_tflite(self):
        print("from_keras_to_tflite")


    def from_concrete_functions_to_tflite(self):
        print("from_concrete_functions_to_tflite")

    def optimization_of_model(self):
        mode = "Speed" 

        if mode == 'Storage':
            optimization = tf.lite.Optimize.OPTIMIZE_FOR_SIZE
        elif mode == 'Speed':
            optimization = tf.lite.Optimize.OPTIMIZE_FOR_LATENCY
        else:
            optimization = tf.lite.Optimize.DEFAULT





