from PIL import Image
def img_resize(img,new_height,new_width):
    image = Image.open(img)
        
    # Getting the image real size
    width , height = image.size
        
    #checking if the new size is bigger then the old one or now
    if int(new_height) > height or int(new_width) > width:
        pass
    else:
        image = image.resize((int(new_width),int(new_height)))
        image = image.save(img.replace(".","_resized."))