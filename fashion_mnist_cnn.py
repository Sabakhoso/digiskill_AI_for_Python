# ==========================================
# TASK 1: Data Loading and Preprocessing [cite: 31]
# ==========================================
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

print("--- Task 1: Loading and Preprocessing Data ---") [cite: 31]
# 1. Load the Fashion-MNIST dataset [cite: 32]
(train_images, train_labels), (test_images, test_labels) = datasets.fashion_mnist.load_data() [cite: 33]

# Define class names for visualization
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# 2. Normalize pixel values to the range [0, 1] [cite: 34]
train_images = train_images / 255.0
test_images = test_images / 255.0

# 3. Reshape images for CNN input (28, 28, 1) [cite: 36]
train_images = train_images.reshape((train_images.shape[0], 28, 28, 1))
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1))
print(f"Train images shape: {train_images.shape}")
print(f"Test images shape: {test_images.shape}\n")

# 4. Provide sample images with labels [cite: 37]
plt.figure(figsize=(10,4))
for i in range(5):
    plt.subplot(1, 5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i].reshape(28,28), cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.suptitle("Sample Images from Fashion-MNIST Dataset")
plt.show()


# ==========================================
# TASK 2: Design/Build the CNN Model [cite: 38]
# ==========================================
print("\n--- Task 2: Building and Compiling the CNN Model ---") [cite: 38, 47]
model = models.Sequential([
    # First Convolutional Layer [cite: 41]
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)), # MaxPooling Layer [cite: 42]
    
    # Second Convolutional Layer [cite: 41]
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)), # MaxPooling Layer [cite: 42]
    
    # Flatten layer before dense layers [cite: 44]
    layers.Flatten(),
    
    # Dense layer with Dropout for regularization [cite: 43, 45]
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.3), # Dropout [cite: 43]
    
    # Output layer (10 classes for Fashion-MNIST) [cite: 45]
    layers.Dense(10, activation='softmax')
])

# Compile the model with appropriate optimizer, loss, and metric [cite: 47]
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.summary()


# ==========================================
# TASK 3: Compile and Train your Model [cite: 48]
# ==========================================
print("\n--- Task 3: Training the Model ---") [cite: 48]
# Train with a 15% validation split for 10 epochs [cite: 51, 52]
history = model.fit(train_images, train_labels, epochs=10, 
                    validation_split=0.15, batch_size=64) [cite: 51, 52]


# ==========================================
# TASK 4: Model Evaluation [cite: 54]
# ==========================================
print("\n--- Task 4: Evaluating the Model ---") [cite: 54]
# Evaluate on unseen test dataset [cite: 55]
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2) [cite: 55]
print(f"\nTest Accuracy: {test_acc:.4f}") [cite: 56]
print(f"Test Loss: {test_loss:.4f}\n") [cite: 56]

# Generate predictions for confusion matrix & classification report [cite: 58]
predictions = model.predict(test_images)
pred_labels = np.argmax(predictions, axis=1)

print("Classification Report:") [cite: 58]
print(classification_report(test_labels, pred_labels, target_names=class_names)) [cite: 58]

# Generate Confusion Matrix [cite: 58]
cm = confusion_matrix(test_labels, pred_labels)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=class_names, yticklabels=class_names)
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')
plt.show()


# ==========================================
# TASK 5: Visualization and Analysis [cite: 59]
# ==========================================
print("\n--- Task 5: Plotting Curves and Predictions ---") [cite: 59]
# 1. Plot training loss and accuracy curves [cite: 60]
plt.figure(figsize=(12, 5))

# Plot Accuracy
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

# Plot Loss
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

# 2. Plot a few test images with predicted and true labels [cite: 61]
plt.figure(figsize=(10, 4))
for i in range(5):
    plt.subplot(1, 5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(test_images[i].reshape(28,28), cmap=plt.cm.binary)
    
    predicted_label = pred_labels[i]
    true_label = test_labels[i]
    
    # Color green if correct, red if incorrect
    color = 'green' if predicted_label == true_label else 'red'
    plt.xlabel(f"Pred: {class_names[predicted_label]}\nTrue: {class_names[true_label]}", color=color)
plt.suptitle("Test Predictions vs True Labels")
plt.tight_layout()
plt.show()