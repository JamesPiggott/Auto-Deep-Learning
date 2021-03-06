import sys

from example_projects.boston_housing.boston_housing import BostonHousing
from example_projects.fashion_mnist.fashion_mnist import FashionMnist
from example_projects.stock_prediction.stock_prediction import StockPrediction
from example_projects.auto_encoder.auto_encoder import AutoEncoder
from example_projects.exoplanet_detection.exoplanet_detection import ExoplanetDetection
from example_projects.rest_api_example.rest_api_model import RestAPI

from src.system import System
from src.manager import Manager
from src.project import Project
from src.model import Model
from src.train import Train
from src.evaluate import Evaluate
from src.converter import Converter
from src.inference import Inference

class App:

    def __init__(self):
        print()

    def get_user_permission(self, request_message):
        reply = input(request_message + " ")
        if reply in ['y', 'Y', 'yes', 'Yes', 'YES']:
            return True
        if reply in ['n', 'N', 'no', 'No', 'NO']:
            return False   


    def ask_user_for_training_options(self, option):
        print("")
        print("Select training options: # epochs and model save choice")

        if option == "1":
            while True:
                print("For 'Boston Housing Data' 300 epochs are typical")
                epochs = int(input("Enter number of epochs: "))
                print("Do you wish to save the model to disk? [yes/Yes||no/No]")
                save_model = input("Enter choice: ")

                if epochs > 0 and epochs < 1000:
                    if save_model in ['y', 'Y', 'yes', 'Yes', 'YES', 'n', 'N', 'no', 'No', 'NO']:
                        return [epochs, True]
                    else:
                        print("Please enter a choice that can be interpreted as 'yes' or 'no'")
                else:
                    print("Please enter a sensible value between 0 and 1000")

        if option == "2":
            while True:
                print("For 'MNIST-Fashion Zalando' 20 epochs are typical")
                epochs = int(input("Enter number of epochs: "))
                print("Do you wish to save the model to disk? [yes/Yes||no/No]")
                save_model = input("Enter choice: ")

                if epochs > 0 and epochs < 100:
                    if save_model in ['y', 'Y', 'yes', 'Yes', 'YES', 'n', 'N', 'no', 'No', 'NO']:
                        return [epochs, True]
                    else:
                        print("Please enter a choice that can be interpreted as 'yes' or 'no'")
                else:
                    print("Please enter a sensible value between 0 and 100")

        if option == "3":
            print()

        if option == "4":
            print()

        if option == "5":
            while True:
                print("For 'Exoplanet CNN' 32 epochs are typical")
                epochs = int(input("Enter number of epochs: "))
                print("Do you wish to save the model to disk? [yes/Yes||no/No]")
                save_model = input("Enter choice: ")

                if epochs > 0 and epochs < 100:
                    if save_model in ['y', 'Y', 'yes', 'Yes', 'YES', 'n', 'N', 'no', 'No', 'NO']:
                        return [epochs, True]
                    else:
                        print("Please enter a choice that can be interpreted as 'yes' or 'no'")
                else:
                    print("Please enter a sensible value between 0 and 100")

        if option == "6":
            while True:
                print("For 'MNIST-AutoEncoder' 50 epochs are typical")
                epochs = int(input("Enter number of epochs: "))
                print("Do you wish to save the model to disk? [yes/Yes||no/No]: ")
                save_model = input("Enter choice: ")

                if epochs > 0 and epochs < 100:
                    if save_model in ['y', 'Y', 'yes', 'Yes', 'YES', 'n', 'N', 'no', 'No', 'NO']:
                        return [epochs, True]
                    else:
                        print("Please enter a choice that can be interpreted as 'yes' or 'no'")
                else:
                    print("Please enter a sensible value between 0 and 100")

    def example_keras_apps(self):

        run = True
        while run:

            print("")
            print("Select application to run (you will be asked to confirm)")
            print("1. Neural Network (Boston Housing data)")
            print("2. Convolutional NN (MNIST-Fashion - Zalando")
            print("3. Recurrent NN (Stock market data)")
            print("4. MNIST Autoencoder")
            print("5. Exoplanet CNN")
            print("6. Rest API to server model")
            print("0. Exit application")
            print("")

            option = input("Choose an option: ")
            if option == "0":
                break
            if option == "1":

                boston = BostonHousing("boston_housing")

            if option == "2":

                fashion = FashionMnist()

            if option == "3":

                stock = StockPrediction()

            if option == "4":

                autoencoder = AutoEncoder()

            if option == "5":

                exoplanet = ExoplanetDetection()

            if option == "6":

                rest_api = RestAPI()

    def new_keras_project(self):

        while True:

            print("")
            print("1. Project management")
            print("2. Load data set")
            print("3. Define model")
            print("4. Train model using data set")
            print("5. Evaluate trained model")
            print("6. Model conversion")
            print("7. Model inference")
            print("8. Deployment")
            print("0. Return to main menu")
            print("")

            project_option = input("Choose an option: ")
            print("")

            if project_option == "0":
                break
            elif project_option == "1":
                self.project_management()
            elif project_option == "2":

                data_location = "../Projects/" + self.project.name[:-1] + "/data"

                if self.get_user_permission("Do you want to download a dataset?"):
                    if self.get_user_permission("Do you wish to use the url defined in project.txt?"):
                        self.project.data.download_url(self.project.download_url[:-1], data_location + "/data")
                    else:
                        data_url = input("Enter the URL for the location of the data: ") 
                        self.project.data.download_url(data_url, data_location + "/data")

                if self.get_user_permission("Do you want to unzip the dataset?"):
                    self.project.data.unzip_data_file(data_location + "/data")

                self.project.data.load_data(data_location)

                self.project.data.autodetect_data_format()
                
                self.project.data.transform_data()
            elif project_option == "3":

                self.model = Model(self.manager)

                self.model.define_model()
                
                self.model.set_optimizer()

                # self.model.load_model_from_project("./Projects/" + self.project.name[:-1] ) # + "/model"

                # set_data_augmentation()
            elif project_option == "4":

                self.train = Train(self.model, self.project.data, self.project)

                self.train.train_model(self.project)

            elif project_option == "5":

                self.evaluate = Evaluate(self.model)

                self.evaluate.evaluate_model()

            elif project_option == "6":

                self.convert = Converter()

                self.convert.create_saved_model(self.model, "../Projects/" + self.project.name[:-1] + "/my_models")

                if self.project.tf_lite_model == True:
                    self.convert.from_keras_to_tflite(self.model, "../Projects/" + self.project.name[:-1] + "/my_models", self.project.name[:-1])

            elif project_option == "7":

                self.inference = Inference()

                self.inference.perform_tflite_inference("../Projects/", self.project.name[:-1])

            elif project_option == "8":

                print("Deploy model for testing")

            else:
                print("Not a valid option")

    def project_management(self):

        self.manager = Manager()

        while True:

            print("")
            print("1. List all projects")
            print("2. Open project file")
            print("3. Create new project")
            print("4. Delete project")
            print("5. Save project")
            print("0. Return to project overview menu")
            print("")

            project_option = input("Choose an option: ")
            print("")

            if project_option == "0": 
                break
            elif project_option == "1":

                print()
                projects = self.manager.list_all_projects()
                if projects is not None:
                    print("The following project folder were detected")
                    for project in projects:
                        print(" # " + project)
                print()

            elif project_option == "2":

                directory_name = input("Enter the name of the project you want to open: ")
                message, self.project = self.manager.open_project(directory_name)
                print("Project name: " + self.project.name)

            elif project_option == "3":

                if self.get_user_permission("Do you want to create a new project folder?"):
                    directory_name = input("Enter a name for your new project: ")
                    message = self.manager.create_folder(directory_name)
                else:
                    directory_name = input("Enter the name of project where project.txt needs to be created: ")
                    message = self.manager.create_project_file(directory_name)

                print(message)

            elif project_option == "4":

                directory_name = input("Enter name of project you want to delete: ")
                message = self.manager.delete_folder(directory_name)
                print(message)

            elif project_option == "5":

                self.manager.save_project(self.project)

            else:
                print("Not a valid option")


    def run(self, run_file):
        with open(run_file, "r") as rnf:
            exec(rnf.read())


    def main(self):
        # sys.stderr.write("\x1b[2J\x1b[H")

        print(" ")
        print("#######################################################")
        print("####  Welcome to the AutoKeras Deep Learning tool   ###")
        print("#######################################################")
        print(" ")

        while True:

            print("")
            print("Input an option below")
            print("1. Select example projects")
            print("2. Open or Create Keras project")
            print("3. Detect hardware available")
            print("0. Exit application")
            print("")

            option = input("Choose an option: ")
            print("")

            if option == "0":
                break
            if option == "1":
                self.example_keras_apps()
            if option == "2":
                self.new_keras_project()
            if option == "3":
                self.system = System()
                self.system.get_available_gpus()
                self.system.check_docker_availability()
        sys.exit()


if __name__ == "__main__":
    app = App()
    app.main()
