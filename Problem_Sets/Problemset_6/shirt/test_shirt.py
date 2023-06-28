##### HOW TO TEST: #####
"""Here’s how to test your code manually:

Run your program with python shirt.py. Your program should exit using sys.exit 
and provide an error message: Too few command-line arguments   

Be sure to download muppets.zip and extract a collection of muppet photos using unzip muppets.zip. 
Run your program with python shirt.py before1.jpg before2.jpg before3.jpg. 
Your program should output: Too many command-line arguments

Run your program with python shirt.py before1.jpg invalid_format.bmp. Your program should exit using sys.exit 
and provide an error message: Invalid output

Run your program with python shirt.py before1.jpg after1.png. Your program should exit using sys.exit 
and provide an error message: Input and output have different extensions

Run your program with python shirt.py non_existent_image.jpg after1.jpg. Your program should exit using sys.exit 
and provide an error message: Input does not exist

Run your program with python shirt.py before1.jpg after1.jpg. 
Assuming you’ve downloaded and unzipped muppets.zip, your program should create an image like the below:


You can execute the below to check your code using check50, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

check50 cs50/problems/2022/python/shirt
Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected.
Visit the URL that check50 outputs to see the input check50 handed to your program, what output it expected, and what output your program actually gave."""
import pytest
import os
from PIL import Image
import shutil

from shirt import validate_user_input, input_image_processing


file_path_dict = {
    'overlay_filepath': r"C:\Users\emely\Documents\GitHub\Harvards-CS50P_Course\Problem_Sets\Problemset_6\shirt\shirt.png",
    
    'input_filepath1': r"C:\Users\emely\Documents\GitHub\Harvards-CS50P_Course\Problem_Sets\Problemset_6\shirt\before1.jpg",
    'output_filepath1': r"C:\Users\emely\Documents\GitHub\Harvards-CS50P_Course\Problem_Sets\Problemset_6\shirt\after1.jpg",
    
    'input_filepath2': r"C:\Users\emely\Documents\GitHub\Harvards-CS50P_Course\Problem_Sets\Problemset_6\shirt\before2.jpg",
    'output_filepath2': r"C:\Users\emely\Documents\GitHub\Harvards-CS50P_Course\Problem_Sets\Problemset_6\shirt\after2.jpg",
    
    'input_filepath3': r"C:\Users\emely\Documents\GitHub\Harvards-CS50P_Course\Problem_Sets\Problemset_6\shirt\before3.jpg",
    'output_filepath3': r"C:\Users\emely\Documents\GitHub\Harvards-CS50P_Course\Problem_Sets\Problemset_6\shirt\after3.jpg",
}

##### Test cases based on instructions for manually testing #####

def test_validate_user_input_zu_wenig_argumente_manuell():
    with pytest.raises(SystemExit) as e:
        validate_user_input(["shirt.py"])
    assert str(e.value) == "Too few command-line arguments"

def test_validate_user_input_zu_viele_argumente_manuell():
    with pytest.raises(SystemExit) as e:
        validate_user_input(["shirt.py", "before1.jpg", "before2.jpg", "before3.jpg"])
    assert str(e.value) == "Too many command-line arguments"

def test_validate_user_input_invalid_output_manuell():
    with pytest.raises(SystemExit) as e:
        validate_user_input(["shirt.py", "before1.jpg", "invalid_format.bmp"])
    assert str(e.value) == "Invalid output"

def test_validate_user_input_unterschiedliche_dateierweiterungen_manuell():
    with pytest.raises(SystemExit) as e:
        validate_user_input(["shirt.py", "before1.jpg", "after1.png"])
    assert str(e.value) == "Input and output have different extensions"

def test_input_image_processing_nicht_existierende_datei_manuell():
    with pytest.raises(SystemExit) as e:
        input_image_processing("non_existent_image.jpg", "after1.jpg")
    assert str(e.value) == "Input does not exist"

def test_input_image_processing_manuell():
    input_file = file_path_dict['input_filepath2']
    output_file = file_path_dict["output_filepath2"]

    # Führe die Bildverarbeitung aus
    input_image_processing(input_file, output_file)

    # Überprüfe, ob das Ausgabebild existiert und die richtige Größe hat
    assert os.path.isfile(output_file)
    output_img = Image.open(output_file)
    assert output_img.size == (600, 600)


##### Test cases for validate_user_input function: #####

def test_validate_user_input_too_few_args():
    with pytest.raises(SystemExit):
        validate_user_input(["shirt.py"])

def test_validate_user_input_too_many_args():
    with pytest.raises(SystemExit):
        validate_user_input(["shirt.py", "input.jpg", "output.jpg", "extra.jpg"])

def test_validate_user_input_invalid_input_file():
    with pytest.raises(SystemExit):
        validate_user_input(["shirt.py", "input.txt", "output.jpg"])

def test_validate_user_input_invalid_output_file():
    with pytest.raises(SystemExit):
        validate_user_input(["shirt.py", "input.jpg", "output.txt"])

def test_validate_user_input_diff_file_extensions():
    with pytest.raises(SystemExit):
        validate_user_input(["shirt.py", "input.jpg", "output.png"])

def test_validate_user_input_valid_input():
    assert validate_user_input(["shirt.py", "input.jpg", "output.jpg"]) == True



###### Test cases for input_image_processing function: #####

@pytest.fixture
def test_files(tmp_path):
    # Create temporary input and output files for testing
    input_file = os.path.join(tmp_path, "input.jpg")
    output_file = os.path.join(tmp_path, "output.jpg")

    # Create a dummy input image
    input_img = Image.new("RGB", (800, 600), color="red")
    input_img.save(input_file)

    return input_file, output_file

def test_input_image_processing_file_not_found():
    with pytest.raises(SystemExit):
        input_image_processing("invalid_input.jpg", "output.jpg")

def test_input_image_processing_output_file_created():
    input_file = file_path_dict["input_filepath3"]
    output_file = file_path_dict["output_filepath3"]
    input_image_processing(input_file, output_file)
    assert os.path.isfile(output_file)

def test_input_image_processing_output_image_size(test_files):
    input_file, output_file = test_files
    input_image_processing(input_file, output_file)
    output_img = Image.open(output_file)
    assert output_img.size == (600, 600)



##### INSTRUCTIONS: #####
"""In a file called shirt.py, implement a program that expects exactly two command-line arguments:

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
            wearing your virtual shirt in any of CS50’s communities!"""