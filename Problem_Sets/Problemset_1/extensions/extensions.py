"""
   Title: Problemset_1 - File Extensions

    Author: Emely Benke
    
    Created: 2023-05-27
    
    Version: 0.1 -> failed check50
    
    Summary: 
        Even though Windows and macOS sometimes hide them, most files have file extensions, 
        a suffix that starts with a period (.) at the end of their name. 
        For instance, file names for GIFs end with .gif, and file names for JPEGs end with .jpg or .jpeg. 
        When you double-click on a file to open it, your computer uses its file extension to determine which program to launch.

        Web browsers, by contrast, rely on media types, formerly known as MIME types, 
        to determine how to display files that live on the web. 
        When you download a file from a web server, that server sends an HTTP header, 
        along with the file itself, indicating the file’s media type. 
        For instance, the media type for a GIF is image/gif, and the media type for a JPEG is image/jpeg. 
        To determine the media type for a file, a web server typically looks at the file’s extension, mapping one to the other.

        See developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types for common types.

        In a file called extensions.py, implement a program that prompts the user for the name of a file and
        then outputs that file’s media type if the file’s name ends, 
        case-insensitively, in any of these suffixes:
            .gif
            .jpg
            .jpeg
            .png
            .pdf
            .txt
            .zip
            
        If the file’s name ends with some other suffix or has no suffix at all, 
        output application/octet-stream instead, which is a common default.
"""

def main():
      
    FILE_EXTENSIONS = {
        """Dict-Format => 'suffix': 'MIME Type', """
        'gif':     'image/gif',                    # Graphics Interchange Format (GIF)
        'jpg':     'image/jpeg',                   # JPEG images
        'jpeg':    'image/jpeg',                   # JPEG images
        'png':     'image/png',                    # Portable Network Graphics
        'pdf':     'application/pdf',              # Adobe Portable Document Format (PDF)
        'txt':     'text/plain',                   # Text, (generally ASCII or ISO 8859-n)
        'zip':     'application/zip',              # ZIP archive
    #   'other':    'application/octet-stream',    # Common default if no match is found
    }

    # prompt for a file name 
    input_file = input("What's the Name of the File?: ").lower() # set string as lowercase
    input_file = input_file.strip() # remove any whitespaces
     
    # split the given input at the '.' to receive the suffix and filename separated
    input_snippets = input_file.split('.')
    raw_file_name = input_snippets[0]
    file_suffix = input_snippets[-1]

    # get all keys of dict as list
    key_list = list(FILE_EXTENSIONS)
    # checks if the suffix of the inputted filename matches any key of the dict
    if file_suffix in key_list:
        media_type = FILE_EXTENSIONS[file_suffix]
        return print(media_type)
    else:               # default value
        return print('application/octet-stream') 
    
    

if __name__ == '__main__':
    main()



"""Here’s how to test your code manually:

Run your program with python extensions.py. Type happy.jpg and press Enter. 
Your program should output:
    image/jpeg   
    
Run your program with python extensions.py. Type document.pdf and press Enter. 
Your program should output:
    application/pdf
    
Be sure to test each of the other file formats, vary the casing of your input, 
and “accidentally” add spaces on either side of your input before pressing enter. 
Your program should behave as expected, case- and space-insensitively.
"""


"""check50 cs50/problems/2022/python/extensions"""