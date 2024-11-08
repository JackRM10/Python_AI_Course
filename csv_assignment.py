# Import neccessary libraries
import os
import pandas as pd

# Set the root directory
dataset_root = "C:\\Users\\Owner\\Documents\\GitHub\\Python_AI_Course\\images"

#Initialize an empty DataFrame with columns for image_path and label
image_data = pd.DataFrame(columns=["image_path", "label"])

# Traverse the dataset directory
for root, dirs, files in os.walk(dataset_root):
    #Use the directory name as the label
    label = os.path.basename(root)

    # Iterate over each file in the current directory
    for file in files:
        #Combine the root directory and file name to get the complete image path
        image_path = os.path.join(root, file)

        # Create a new DataFrame with the image path and label as values
        row = pd.DataFrame({"image_path": [image_path], "label": [label]})

        #Concatenate the new row with the existing image_data DataFrame
        image_data = pd.concat([image_data, row], ignore_index=True)

        # Save the DataFrame as a csv file named "image_dataset.csv"
        image_data.to_csv("image_dataset.csv", index=False)

        file_path = "image_dataset.csv"
        os.startfile(file_path)
        