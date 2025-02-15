🐶 Dog Breed Classifier
This project uses a pre-trained image classifier to identify different dog breeds. It takes an image, processes it, and predicts the breed of the dog.

📂 Project Files
pet_images/ → Folder containing dog images
check_images.py → Main script to classify images
classify_images.py → Uses a pre-trained CNN model
get_pet_labels.py → Extracts labels from image filenames
dognames.txt → List of dog breeds
print_results.py → Displays classification results
🚀 How to Run
1️⃣ Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
2️⃣ Run the Classifier
bash
Copy
Edit
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
You can replace vgg with resnet or alexnet.
3️⃣ View Results
After running, the script will display:
✅ Predicted breed
✅ Accuracy percentage
✅ Model performance

📜 License
This project is open-source and free to use.
