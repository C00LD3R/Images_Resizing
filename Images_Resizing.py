from PIL import Image
import os

# Entering the new image size
new_width = input("Enter new width : ")
new_height = input("Enter new height : ")
# Entering images folder path and output folder name
output_folder = input("Enter the output folder : ")
images_folder = input("Enter the images folder full path : ")


# Changing Directory to images directory
os.chdir(images_folder)

if not os.path.exists(output_folder):
    os.mkdir(output_folder)
#looping through the directory to find the images names

for filename in os.listdir('.'):
    if not filename.endswith((".png",".jpg",".jpeg")):
        pass
    else:
        image = Image.open(filename)
        
        # Getting the image real size
        width , height = image.size
        
        #checking if the new size is bigger then the old one or now
        if int(new_height) > height or int(new_width) > width:
            pass
        else:
            image = image.resize((int(new_width),int(new_height)))
            image = image.save(os.path.join(output_folder,filename))
            print(f"{filename} resized successfully")
    
print("---------------------Resizing process done---------------------")

print(f"You will find the resized images in {output_folder} folder here ---> {images_folder}")