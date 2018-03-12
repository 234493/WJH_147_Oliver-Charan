import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw  

def paste_logo(original_image, logo_size, logo):
    """ Returns a picture that the logo is pasted on
    
        We first defined the logo and then linked the directory to where
        our logo stored. After that, it opens the PIL.Image (the logo) and 
        then we decided to set the logo size to .3. And then it get's the image
        width and height to calculate where the logo will be placed on the picture.
        After that, it will paste the logo and will return the result of the picture
        with the logo on it.
    """
    logo = PIL.Image.open('/Users/232150/Desktop/Python/1.4.5 Images/OrangePro.png')#Locates the logo using the directory that is provided
    logo_size = .3 #set the logo size
    width, height = original_image.size
    position = int(logo_size * min(width, height))
    
    rlogo = logo.resize((position, position))
    
    result = original_image.copy()
    result.paste(rlogo, (0,0), rlogo)
    return result
    
def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list

def paste_logo_for_all_images(directory=None):
    """ Saves a modfied version of each image in directory.
    
    It will use the current directory if no directory is specified. 
    If a directory does not exist, it will make a directory that will
    be named 'modified'. Then it will get all of the images from the 
    directory that is specified, then it gets all of the images and then
    loads them. Then it will use the same prosedures and arguments from 
    paste_logo. After that is done, it will use the file name and add '.png' 
    at the end and then puts it in the directory that the user specified
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    image_list, file_list = get_images(directory) #loads all the images
    logo = PIL.Image.open('/Users/232150/Desktop/Python/1.4.5 Images/OrangePro.png') 
    #Locates the logo using the directory that is provided
    logo_size = .3 #set the logo size
    #goes through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        filename, filetype = os.path.splitext(file_list[n])
        
        new_image = paste_logo(image_list[n], logo_size, logo)
        #Used the arguments from the paste_logo to do it all of the images at once in the list
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)