import pickle
import numpy as np
from sklearn.model_selection import train_test_split
import tarfile
import matplotlib.pyplot as plt

# Extracting the Dataset
tar = tarfile.open(r"C:/Users/Owner/Documents/GitHub/Python_AI_Course/cifar-10-python.tar.gz")
tar.extractall()
tar.close()

# Define a function to load the batch file
def unpickle(file):
    with open(file, 'rb') as fo:
        data = pickle.load(fo, encoding='bytes')
    return data

# Load dataset batch files
data_batch_1 = unpickle('cifar-10-batches-py/data_batch_1')
data_batch_2 = unpickle('cifar-10-batches-py/data_batch_2')
data_batch_3 = unpickle('cifar-10-batches-py/data_batch_3')
data_batch_4 = unpickle('cifar-10-batches-py/data_batch_4')
data_batch_5 = unpickle('cifar-10-batches-py/data_batch_5')

# Combine the loaded batches into a single dataset
X_train = np.concatenate([
    data_batch_1[b'data'],
    data_batch_2[b'data'],
    data_batch_3[b'data'],
    data_batch_4[b'data'],
    data_batch_5[b'data'] 
])
    
y_train = np.concatenate([
    data_batch_1[b'labels'],
    data_batch_2[b'labels'],
    data_batch_3[b'labels'],
    data_batch_4[b'labels'],
    data_batch_5[b'labels']
])

# Load the test batch
test_batch = unpickle('cifar-10-batches-py/test_batch')
X_test = test_batch[b'data']
y_test = np.array (test_batch[b'labels'])

# Reshape the data
X_train = X_train.reshape(-1, 3, 32, 32).transpose(0, 2, 3, 1)
X_test = X_test.reshape(-1, 3, 32, 32).transpose(0, 2, 3, 1)

# Split the dataset into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# Verify the dataset extraction
print("Dataset extracted successfully!")

# Check the dataset shape
print("x_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)
print("x_val shape:", X_val.shape)
print("y_val shape:", y_val.shape)
print("x_test shape:", X_test.shape)
print("y_test shape:", y_test.shape)

# Complete label names dictionary for CIFAR-10
label_names = {
    0: "Airplane",
    1: "Automobile",
    2: "Bird",
    3: "Cat",
    4: "Deer",
    5: "Dog",
    6: "Frog",
    7: "Horse",
    8: "Ship",
    9: "Truck"
}

# Visualize the images
fig, axes = plt.subplots (3, 5, figsize=(15,9))
for i, ax in enumerate (axes.flat):
    ax.imshow(X_train[i])
    ax.set_title(f"Label: {y_train[i]}\n{label_names[y_train[i]]}") # Display label and category name
    ax.axis("off")
plt.tight_layout()
plt.show()

# Verify Class Labels
unique_labels = np.unique(y_train)
print("Unique class labels:", unique_labels)