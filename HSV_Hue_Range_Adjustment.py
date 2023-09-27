import cv2
import numpy as np
import os

###############################################################################

# Blue: Hue = 120
# Complementary: Yellow = 30

# Green: Hue = 60
# Complementary: Magenta

# Red: Hue = 0
# Complementary: Cyan = 90

# Cyan: Hue = 90 (In this code)
# Complementary: Red = 0

# Yellow: Hue = 30
# Complementary: Blue = 120

# Pink: Hue = 300
# Complementary: Hue = (300 + 180) % 180 = 120

###############################################################################

# Constants for adjustable values
INPUT_FOLDER = "Input_Images"        # Input directory
OUTPUT_FOLDER = "Output_Images"       # Output directory

INPUT_IMAGE = "Image_005.jpg"        # Input image name
HUE = 0                             # Hue value
HUE_RANGE = 10                       # Hue range width

###############################################################################

"""
    Adjusts the hue range in an image in the HSV color space.

    Args:
        img_path (str): Path to the input image.
        h (int): Central hue value to be adjusted.
        x (int): Width of the hue range to be adjusted.

    Returns:
        numpy.ndarray: Resulting image with adjusted hues.
"""
def adjust_hue_range(img_path, h, x):
    try:
        # Load the image in BGR format
        img = cv2.imread(img_path)

        # Check if the image was loaded successfully
        if img is None:
            raise FileNotFoundError("Error: Failed to load the image.")

        # Convert the image to HSV.
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Convert h to the range [0, 180]
        h = h % 180

        # Calculate the lower and upper bounds for the hue range
        lower = np.array([max(0, h - x), 0, 0])
        upper = np.array([min(180, h + x), 255, 255])

        # Create a mask for hues in the specified range
        mask = cv2.inRange(img_hsv, lower, upper)

        img_hsv[mask > 0, 0] = (img_hsv[mask > 0, 0] + 90) % 180

        # Convert the image back to the BGR color space
        img_result = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

        return img_result
    except Exception as e:
        print(e)
        return None

"""
    Generates the output file name based on the input file name.

    Args:
        input_filename (str): Input file name.

    Returns:
        str: Output file name.
"""
def generate_output_filename(input_filename):
    # Get the file name without extension
    file_name_without_extension = os.path.splitext(input_filename)[0]
    return f"{file_name_without_extension}_output.jpg"

def main():
    try:
        # Input and output directories
        current_directory = os.getcwd()
        input_path = os.path.join(current_directory, INPUT_FOLDER, INPUT_IMAGE)
        output_path = os.path.join(current_directory, OUTPUT_FOLDER, generate_output_filename(INPUT_IMAGE))

        # Hue and hue range values
        h = HUE
        x = HUE_RANGE

        input_image = cv2.imread(input_path)
        output_image = adjust_hue_range(input_path, h, x)

        # Check if the output image was generated successfully
        if output_image is not None:

            # Resize the input and output images (optional)
            input_image = cv2.resize(input_image, (1024, 1024), interpolation=cv2.INTER_LINEAR)
            output_image = cv2.resize(output_image, (1024, 1024), interpolation=cv2.INTER_LINEAR)

            # Concatenate the input and output images horizontally
            combined_image = np.hstack((input_image, output_image))

            # Check and create output directories if necessary
            os.makedirs(os.path.join(current_directory, OUTPUT_FOLDER), exist_ok=True)

            # Set the size of the output window
            cv2.namedWindow("Input and Output Images", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Input and Output Images", 800, 800)

            # Display the combined image
            cv2.imshow("Input and Output Images", combined_image)

            # Wait for a key press
            cv2.waitKey(0)

            # Close the window
            cv2.destroyAllWindows()

            # Save the output image based on the input image name
            cv2.imwrite(output_path, output_image)

        else:
            print("Failed to generate the output image.")
    except Exception as e:
        print(e)

if __name__ == "__main__" :
    main()
