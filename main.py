from img_proc import img_resize
import os

def main():
    # Entering the new image size
    new_width = input("Enter new width : ")
    new_height = input("Enter new height : ")
    # Entering images folder path and output folder name
    images_folder = input("Enter the images folder full path : ")


    # Changing Directory to images directory
    os.chdir(images_folder)

    for filename in os.listdir('.'):
        if not filename.endswith((".png",".jpg",".jpeg")):
            pass
        else:
            img_resize(filename,new_height,new_width)        
    print("---------------------Resizing process done---------------------")

    print(f"You will find the resized images here ---> {images_folder}")
        

if __name__ == "__main__":
    main()