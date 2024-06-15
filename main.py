import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from PIL import Image
import colorama
from colorama import Fore, Style, init
from click import pause

colorama.init()

RED = Fore.LIGHTRED_EX + Style.BRIGHT
BLUE = Fore.LIGHTCYAN_EX + Style.BRIGHT
GREEN = Fore.LIGHTGREEN_EX + Style.BRIGHT
WHITE = Fore.LIGHTWHITE_EX + Style.BRIGHT
MAGENTA = Fore.LIGHTMAGENTA_EX + Style.BRIGHT
YELLOW = Fore.LIGHTYELLOW_EX + Style.BRIGHT
RESET = Style.RESET_ALL

# Load the MobileNetV2 model pre-trained on ImageNet
model = MobileNetV2(weights='imagenet')

os.system('cls')

print(f'''{WHITE}
======================================================
-----       {BLUE}Python Image Recognition Tool{WHITE}        -----
======================================================{RESET}\n''')

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))  # Load the image
    img_array = image.img_to_array(img)  # Convert the image to a numpy array
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = preprocess_input(img_array)  # Preprocess the image
    return img_array

def predict_image(img_path):
    img_array = preprocess_image(img_path)  # Preprocess the image
    predictions = model.predict(img_array)  # Make predictions
    decoded_predictions = decode_predictions(predictions, top=3)[0]  # Decode the predictions
    return decoded_predictions

if __name__ == "__main__":
    img_path = input(f"{WHITE}[{BLUE}>{WHITE}] Please enter the path to your image:{YELLOW} ")  # Ask for the image path
    print()
    if os.path.isfile(img_path):
        predictions = predict_image(img_path)  # Predict the image
        print(f'\n{RESET}{WHITE}Predictions')
        print(f'================================{RESET}')
        for pred in predictions:
            print(f"{BLUE}>> {MAGENTA}{pred[1]}{WHITE}:{RED} {pred[2]*100:.2f}%{RESET}")  # Print the predictions
        print(f'{WHITE}================================{RESET}')
        pause(f"\n{WHITE}[{BLUE}>>{WHITE}] Press any key to exit...{RESET}")

    else:
        print(f"\n{WHITE}[{RED}err{WHITE}] Invalid file path. Please try again.{RESET}")
        pause(f"\n{WHITE}[{BLUE}>>{WHITE}] Press any key to exit...{RESET}")
