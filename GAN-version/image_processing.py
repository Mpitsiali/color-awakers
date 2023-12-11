import os
from PIL import Image

def convert_to_grayscale_and_resize(input_folder, output_folder, size=(256, 256)):
    # Check if output folder exists, if not, create it
    if not os.path.exists(output_folder):
        print('folder not found')
        return

    # Iterate over all images in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg','.JPEG')):
            # Construct the full file path
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                # Open the image
                with Image.open(input_path) as img:
                    # grayscale_img = img.convert('L')
                    # Resize the image
                    # resized_img = img.resize(size)

                    # Convert to grayscale
                    grayscale_img = img.convert('L')
                    # Resize the image
                    resized_img = grayscale_img.resize(size)
                    # Save the image
                    resized_img.save(output_path)
                print(f"Processed {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Usage example
input_folder = 'GAN-version/Test_imagenet'
output_folder = 'GAN-version/test_image_net'
convert_to_grayscale_and_resize(input_folder, output_folder)
