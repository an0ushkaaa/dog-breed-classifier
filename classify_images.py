from torchvision import models, transforms
from PIL import Image
import torch

def load_model(architecture):
    if architecture == 'resnet':
        model = models.resnet50(pretrained=True)
    elif architecture == 'alexnet':
        model = models.alexnet(pretrained=True)
    else:  
        model = models.vgg16(pretrained=True)
    
    model.eval()
    return model

def classify_images(image_dir, pet_labels, architecture):
    model = load_model(architecture)
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])

    results = {}
    for filename, label in pet_labels.items():
        image = Image.open(image_dir + filename)
        image = transform(image).unsqueeze(0)
        
        with torch.no_grad():
            output = model(image)
            _, predicted = output.max(1)

        results[filename] = label + [str(predicted.item())]
    
    return results
