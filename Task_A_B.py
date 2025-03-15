# IMAGE CLASSIFICATION GAME using resnet18

# This is a mini image classification game built using the ResNet18 model, Gradio,Torchvision and PyTorch. The game allows users to upload an image and guess its name. The model predicts the image label, and the user’s input is compared with the actual prediction.

# Key Features:
# ResNet18 (a pre-trained deep learning model) for image classification.
# Implements real-time scoring with count_of_correct_answer and total_answers.
# Case-insensitive comparison ensures better user experience.
# Gradio-based UI for an interactive web-based experience.
# PyTorch is used for deep learning inference 
# Torchvision for loading the pre-trained ResNet18 model and image transformations to ensure proper input format.

import torch
import torchvision.transforms as T
from PIL import Image
import requests
import gradio as gr
from torchvision.models import resnet18

model = resnet18(pretrained = True)
model.eval()

transform = T.Compose([
    T.Resize(256),
    T.CenterCrop(224),
    T.ToTensor(),
    T.Normalize([0.485, 0.456, 0.406],
                [0.229,0.224,0.225])
])

labels = 'https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt'

imagenet_labels = requests.get(labels).text.split('\n')
count_of_correct_answer = 0 
total_answers = 0

def predict(img , name_of_image):
    global total_answers , count_of_correct_answer

    total_answers += 1  
    img_t = transform(img).unsqueeze(0)
    with torch.no_grad():
        pred = model(img_t).argmax().item()

    if name_of_image.lower() == imagenet_labels[pred].lower():
        count_of_correct_answer += 1  
        print(f'You have entered the correct answer')
        return f'Name of the image is {imagenet_labels[pred]}.\nYou have entered correct answer.\nTotal attempts : {total_answers}. \nYour score : {count_of_correct_answer}'

    else :
        print('You have entered the incorrect answer')
        return f'Name of the image is {imagenet_labels[pred]}.\nYou have entered incorrect answer.\nTotal attempts : {total_answers}. \nYour score : {count_of_correct_answer}'

iface = gr.Interface(
    fn = predict,
    inputs = [
        gr.Image(type = 'pil' , label = 'Upload an Image : '),
        gr.Textbox(label="Enter your Guess : ")
    ],
    outputs = gr.Textbox(label = 'Result : '),
    title = 'Welcome to ResNet18 Image Classification Game',
    description = 'In this game you can test your image recognition skills with AI-powered game.\n 1) Upload an image.\n 2) Guess its name.\n\n See if you can beat the model! \t\t You can also track your score and improve with every attempt.\t\t Lets play!',
)

iface.launch()