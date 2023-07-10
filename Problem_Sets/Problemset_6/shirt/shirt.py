"""
    Title: Problemset_6 - CS50 P-Shirt

    Author: Emely Benke

    Created: 2023-06-28

    Version: 0.1

    Summary:
After finishing CS50 itself, students on campus at Harvard traditionally receive their very own
'I took CS50 t-shirt'. No need to buy one online, but like to try one on virtually?

In a file called shirt.py, implement a program that expects exactly two command-line arguments:

in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
The program should then overlay shirt.png (which has a transparent background) on the input
after resizing and cropping the input to be the same size, saving the result as its output.

Open the input with Image.open,
per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open,
resize and crop the input with ImageOps.fit,
per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit,
using default values for method, bleed, and centering, overlay the shirt with Image.paste,
per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste,
and save the result with Image.save,
per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

The program should instead exit via sys.exit:

if the user does not specify exactly two command-line arguments,
if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
if the input’s name does not have the same extension as the output’s name, or
if the specified input does not exist.
 Assume that the input will be a photo of someone posing in just the right way,
like these demos, so that, when they’re resized and cropped, the shirt appears to fit perfectly.

If you’d like to run your program on a photo of yourself,
first drag the photo over to VS Code’s file explorer,
into the same folder as shirt.py. No need to submit any photos with your code.
But, if you would like, you’re welcome (but not expected) to share a photo of yourself
wearing your virtual shirt in any of CS50’s communities!
"""

""" Hints
Note that you can determine a file’s extension with os.path.splitext, per docs.python.org/3/library/os.path.html#os.path.splitext.
Note that open can raise a FileNotFoundError, per docs.python.org/3/library/exceptions.html#FileNotFoundError.
Note that the Pillow package comes with quite a few classes and methods, per pypi.org/project/Pillow.
You might find its handbook and reference helpful to skim. You can install the package with:
pip install Pillow
You can open an image (e.g., shirt.png) with code like:

shirt = Image.open("shirt.png")
You can get the width and height, respectively, of that image as a tuple with code like:

size = shirt.size
And you can overlay that image on top of another (e.g., photo) with code like

photo.paste(shirt, shirt)
wherein the first shirt represents the image to overlay and the second shirt represents a “mask” indicating which pixels in photo to update.

Note that you can open an image (e.g., shirt.png) in VS Code by running
code shirt.png
or by double-clicking its icon in VS Code’s file explorer."""
from PIL import Image, ImageOps     # provides extensive file format support + powerful image processing capabilities.
import sys                          # for handling command-line arguments and exiting the program
import os                           # powerful interface for interaction with the operation system


##### Variables, Constants and Datacollections: #####

# Create an Container for all required Errormessages
ERROR_MESSAGES = {
    'too_few_args':         "Too few command-line arguments",
    'too_many_args':        "Too many command-line arguments",
    'input_file':           "Invalid input",
    'output_file':          "Invalid output",
    'diff_file_extensions': "Input and output have different extensions",
    'file_not_found':       "Input does not exist"
}

VALID_FILE_TYPES = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')

# Size: (600, 600) w+h as px |
SHIRT_IMG_PATH = r"C:\Users\emely\Documents\GitHub\Harvards-CS50P_Course\Problem_Sets\Problemset_6\shirt\data\shirt.png"


##### FUNCTIONS: #####

def main():
    # Validates the inputted command-line parameters
    if validate_user_input(sys.argv):
        input, output =  sys.argv[1], sys.argv[2] # ( Reference-image | Input-image | Output-image )
        # Processes the input images according to given instructions (see in header)
        input_image_processing(input, output)
        # exit the programm after finished image processing
        sys.exit()



def validate_user_input(cl_args: list):
    """Validates the command line parameters given by the user and handles not applicable requirements
    by terminating the program with a corresponding error message.

    Args:
        cl_args (list): List of command-line arguments.

    Returns:
        bool: True if the user input is valid.

    Raises:
        SystemExit: Raises a SystemExit exception for various error conditions.
    """

    # Program expects exactly two command-line arguments from the user
    if len(cl_args) < 3:
        sys.exit(ERROR_MESSAGES['too_few_args'])
    elif len(cl_args) > 3:
        sys.exit(ERROR_MESSAGES['too_many_args'])

    # Get file names|paths from inputted command line arguments
    input_file, output_file = cl_args[1:3]

    # Extract the file extensions for proper comparison
    input_path = os.path.splitext(input_file)
    output_path = os.path.splitext(output_file)

    # Exit the program if the input or output file names do not end in '.jpg', '.jpeg', or '.png', case-insensitively
    if input_path[1] not in VALID_FILE_TYPES:
        sys.exit(ERROR_MESSAGES['input_file'])
    elif output_path[1] not in VALID_FILE_TYPES:
        sys.exit(ERROR_MESSAGES['output_file'])


    # Check if the file extensions of input and output files match
    if input_path[1] != output_path[1]:
        sys.exit(ERROR_MESSAGES['diff_file_extensions'])


    # If no errors occurred so far, the given input and output files seem to be valid
    return True



def input_image_processing(input: str, output: str) -> None:
    """input_image_processing should overlay shirt.png (which has a transparent background) on the input
    after resizing and cropping the input to be the same size, saving the result as its output.

                      in pixel width | height ----
    Reference_Imagefile = Size: (600, 600) |

    Args:
        filepaths (tuple): contains filepathstring for the Reference, the Input and the Output Images.

    Returns:
        Image: returns the Imagefile of the result after saving the file
    """
    try:
        shirt = Image.open(r"C:\Users\emely\Documents\GitHub\Harvards-CS50P_Course\Problem_Sets\Problemset_6\shirt\shirt.png")
        with Image.open(input) as input_img:
            x, y = shirt.size
            input_cropped = ImageOps.fit(input_img, (x,y))
            input_cropped.paste(shirt, shirt)
            input_cropped.save(output)
    except FileNotFoundError:
        sys.exit(ERROR_MESSAGES['file_not_found'])



if __name__ == '__main__':
    main()