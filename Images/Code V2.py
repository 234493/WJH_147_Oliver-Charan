import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw         

def frame(original_image, color, frame_width, logo_size):
    """ Put a frame around a PIL.Image
    
    original_image must be a PIL.Image
    Returns a new PIL.Image with a frame, where
    0 < frame_width < 1
    is the border as a portion of the shorter dimension of original_image
    """
    #set the radius of the rounded corners
    width, height = original_image.size
    thickness = int(frame_width * min(width, height)) # thickness in pixels
    
    ###
    #create a mask
    ###
    
    #start with transparent mask
    r, g, b = color
    frame_mask = PIL.Image.new('RGBA', (width, height), (0,0,0,0))
    drawing_layer = PIL.ImageDraw.Draw(frame_mask)
    
    drawing_layer.rectangle((0,0,width,thickness), fill=(r,g,b,255))
    drawing_layer.rectangle((0,0,thickness, height), fill=(r,g,b,255))
    drawing_layer.rectangle((0,height,width,height - thickness), fill=(r,g,b,255))
    drawing_layer.rectangle((width,height,width - thickness,0), fill=(r,g,b,255))
    
    # Make the new image, starting with all transparent
    result = original_image.copy()
    result.paste(frame_mask, (0,0), mask=frame_mask)
    
    logo = PIL.Image.open('/Users/232150/Desktop/CSP/Github/WJH_147_Oliver-Charan/WJH_147_Oliver-Charan/OrangePro.png')#Locates the logo using the directory that is provided
    #logo_size = .3 #set the logo size
    position = int(logo_size * min(width, height))
    
    rlogo = logo.resize((position, position))
    result.paste(rlogo, (thickness,thickness), rlogo)
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

def frame_all_images(directory=None, color=(255,215,0), frame_width=0.10):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have transparent rounded corners.
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'framed')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    #load all the images
    image_list, file_list = get_images(directory)  

    #go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        print n
        filename, filetype = file_list[n].split('.')
        
        # Round the corners with radius = 30% of short side
        new_image = frame(image_list[n],color,frame_width)
        #save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)    

def paste_logo(original_image, logo_size, logo):
    """ Returns a picture that the logo is pasted on
    
        We first defined the logo and then linked the directory to where
        our logo stored. After that, it opens the PIL.Image (the logo) and 
        then we decided to set the logo size to .3. And then it get's the image
        width and height to calculate where the logo will be placed on the picture.
        After that, it will paste the logo and will return the result of the picture
        with the logo on it.
    """
    logo = PIL.Image.open('/Users/232150/Desktop/CSP/Github/WJH_147_Oliver-Charan/WJH_147_Oliver-Charan/OrangePro.png')#Locates the logo using the directory that is provided
    logo_size = .3 #set the logo size
    width, height = original_image.size
    position = int(logo_size * min(width, height))
    
    rlogo = logo.resize((position, position))
    
    result = original_image.copy()
    result.paste(rlogo, (0,0), rlogo)
    return result


def paste_logoborder_for_all_images(directory=None, color =(255,215,0), frame_width=.05, logo_size=.2):
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
    new_directory = os.path.join(directory, 'modified-logoAndFrame')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    image_list, file_list = get_images(directory) #loads all the images
    logo = PIL.Image.open('/Users/232150/Desktop/CSP/Github/WJH_147_Oliver-Charan/WJH_147_Oliver-Charan/OrangePro.png') 
    #Locates the logo using the directory that is provided
    logo_size = .3 #set the logo size
    #goes through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        filename, filetype = os.path.splitext(file_list[n])
        
        new_image = frame(image_list[n], color, frame_width, logo_size )
        #Used the arguments from the paste_logo to do it all of the images at once in the list
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)