
## Image Recognition Script 🖼️🔎

This is a simple image recognition script using Python and the pre-trained MobileNetV2 model from TensorFlow. The script allows you to input an image file path and get predictions on the contents of the image.
## Prerequisites 🔄

Before you begin, ensure you have met the following requirements:
- You have installed Python 3.x
- You have installed the required libraries listed in the `requirements.txt` file

## Installation 💾

#### 1. Clone this repository or download the script directly.
#### 2. Navigate to the directory containing the script.
#### 3. Install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

## Usage 🖥️

#### 1. Run the script

```bash
python image_recognition.py
```

#### 2. When prompted, enter the path to your image file (test images provided)

```bash
Please enter the path to your image: /path/to/your/image.jpg
```

#### 3. The script will process the image and output the top 3 predicted classes along with their probabilities.

## Example Output 🖥️

```code
Predictions
================================   
>> Labrador_retriever: 60.73%      
>> golden_retriever: 15.74%        
>> Rhodesian_ridgeback: 1.61%      
================================ 
```
## Requirements 💿

The script requires the following libraries:

- tensorflow
- pillow
- numpy

These are listed in the `requirements.txt` file. Install them using:

```bash
pip install -r requirements.txt
```


## Script Details 🤖 

#### The script performs the following steps:

#### 1. Loads the pre-trained MobileNetV2 model.
#### 2. Prompts the user to input the path to an image file.
#### 3. Preprocesses the image to the required format.
#### 4. Uses the model to predict the contents of the image.
#### 5. Outputs the top 3 predicted classes along with their probabilities.
## License 📜

This project is licensed under the MIT License - see the LICENSE file for details.
## Acknowledgements 🙏

- The [TensorFlow](https://www.tensorflow.org/) team for their excellent library and pre-trained models.
- The [Keras](https://keras.io/) team for making deep learning accessible and easy to use.
- The contributors of [Pillow](https://python-pillow.org/) for their image processing library.