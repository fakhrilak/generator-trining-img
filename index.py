from PIL import Image
from tqdm import tqdm
from convertyolo import convert_yolo_to_box,convert_box_to_yolo
import os
import time
# Open the file in read mode
user = "kubre2"
cut = 30
filelist = os.listdir("from/")
os.system("del to\\*")
os.system("copy from\\classes.txt to\\")
print(
   "   ▄████████    ▄████████    ▄█   ▄█▄    ▄█    █▄       ▄████████  ▄█   ▄█          ▄████████    ▄█   ▄█▄ "
   "\n  ███    ███   ███    ███   ███ ▄███▀   ███    ███     ███    ███ ███  ███         ███    ███   ███ ▄███▀ "
   "\n  ███    █▀    ███    ███   ███▐██▀     ███    ███     ███    ███ ███▌ ███         ███    ███   ███▐██▀   "
   "\n ▄███▄▄▄       ███    ███  ▄█████▀     ▄███▄▄▄▄███▄▄  ▄███▄▄▄▄██▀ ███▌ ███         ███    ███  ▄█████▀    "
   "\n▀▀███▀▀▀     ▀███████████ ▀▀█████▄    ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀▀▀   ███▌ ███       ▀███████████ ▀▀█████▄    "
   "\n  ███          ███    ███   ███▐██▄     ███    ███   ▀███████████ ███  ███         ███    ███   ███▐██▄   "
   "\n  ███          ███    ███   ███ ▀███▄   ███    ███     ███    ███ ███  ███▌    ▄   ███    ███   ███ ▀███▄ "
   "\n  ███          ███    █▀    ███   ▀█▀   ███    █▀      ███    ███ █▀   █████▄▄██   ███    █▀    ███   ▀█▀ "
   "\n                            ▀                          ███    ███      ▀                        ▀         "
)
print("   STARTING IMAGE GENERATOR")
for count,filename in tqdm(enumerate(filelist),ncols=80, total=len(filelist),bar_format='{percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]'):
    if filename[-3:] == "png":
        im = Image.open("from/"+filename)
        width_img,height_img = im.size
        file_path = "from\\"+filename[:-4]+".txt"
        coordinates = []
        clased = []
        with open(file_path, 'r') as file:
            for line in file:
                line_data = line.strip().split(" ")
                clased.append(line_data[0])
                line_data = [float(item) for item in line_data[1:]]
                coordinates.append(line_data)
        #### POTONG KIRI
        for k in range(cut):
            newCordinate=[]
            for counter_classs,classes in enumerate(coordinates):
                x,y,width,height = classes
                x1,y1,x2,y2 = convert_yolo_to_box(x, y, width, height, width_img, height_img)
                yolo_x, yolo_y, yolo_width, yolo_height = convert_box_to_yolo(x1-(k*10),y1,x2-(k*10),y2, width_img-(k*10), height_img)
                newCordinate.append([clased[counter_classs],yolo_x, yolo_y, yolo_width, yolo_height])
            name = "left-"+str(0) +str(k*10)
            file_path = "to/"+user+"-"+filename[:-4]+"-"+name+".txt"
            with open(file_path, 'w') as file:
                for line in newCordinate:
                    line_str = ' '.join(str(item) for item in line)
                    file.write(line_str + '\n')
            left = 0+(k*10)
            top = 0
            right = width_img
            bottom = height_img
            im1 = im.crop((left, top, right, bottom))
            im1.save("to/"+user+"-"+filename[:-4]+"-"+name+".png")
        ### POTONG KANAN
        for k in range(int(cut/2)):
            newCordinate=[]
            for counter_classs,classes in enumerate(coordinates):
                x,y,width,height = classes
                x1,y1,x2,y2 = convert_yolo_to_box(x, y, width, height, width_img, height_img)
                yolo_x, yolo_y, yolo_width, yolo_height = convert_box_to_yolo(x1,y1,x2,y2, width_img-(k*10), height_img)
                newCordinate.append([clased[counter_classs],yolo_x, yolo_y, yolo_width, yolo_height])
            name = "right-"+str(0) +str(k*10)
            file_path = "to/"+user+"-"+filename[:-4]+"-"+name+".txt"
            with open(file_path, 'w') as file:
                for line in newCordinate:
                    line_str = ' '.join(str(item) for item in line)
                    file.write(line_str + '\n')
            left = 0
            top = 0
            right = width_img -(k*10)
            bottom = height_img
            im1 = im.crop((left, top, right, bottom))
            im1.save("to/"+user+"-"+filename[:-4]+"-"+name+".png")
        ### POTONG ATAS
        for k in range(int(cut)):
            newCordinate=[]
            for counter_classs,classes in enumerate(coordinates):
                x,y,width,height = classes
                x1,y1,x2,y2 = convert_yolo_to_box(x, y, width, height, width_img, height_img)
                yolo_x, yolo_y, yolo_width, yolo_height = convert_box_to_yolo(x1,y1-(k*10),x2,y2-(k*10), width_img, height_img-(k*10))
                newCordinate.append([clased[counter_classs],yolo_x, yolo_y, yolo_width, yolo_height])
            name = "top-"+str(0) +str(k*10)
            file_path = "to/"+user+"-"+filename[:-4]+"-"+name+".txt"
            with open(file_path, 'w') as file:
                for line in newCordinate:
                    line_str = ' '.join(str(item) for item in line)
                    file.write(line_str + '\n')
            left = 0
            top = 0+(k*10)
            right = width_img 
            bottom = height_img
            im1 = im.crop((left, top, right, bottom))
            im1.save("to/"+user+"-"+filename[:-4]+"-"+name+".png")
        ## POTONG ATAS KIRI
        for k in range(int(cut)):
            newCordinate=[]
            for counter_classs,classes in enumerate(coordinates):
                x,y,width,height = classes
                x1,y1,x2,y2 = convert_yolo_to_box(x, y, width, height, width_img, height_img)
                yolo_x, yolo_y, yolo_width, yolo_height = convert_box_to_yolo(x1-(k*10),y1-(k*10),x2-(k*10),y2-(k*10), width_img-(k*10), height_img-(k*10))
                newCordinate.append([clased[counter_classs],yolo_x, yolo_y, yolo_width, yolo_height])
            name = "top-left-"+str(0) +str(k*10)
            file_path = "to/"+user+"-"+filename[:-4]+"-"+name+".txt"
            with open(file_path, 'w') as file:
                for line in newCordinate:
                    line_str = ' '.join(str(item) for item in line)
                    file.write(line_str + '\n')
            left = 0+(k*10)
            top = 0+(k*10)
            right = width_img 
            bottom = height_img
            im1 = im.crop((left, top, right, bottom))
            im1.save("to/"+user+"-"+filename[:-4]+"-"+name+".png")
        
        ## POTONG ATAS KANAN
        for k in range(int(cut/2)):
            newCordinate=[]
            for counter_classs,classes in enumerate(coordinates):
                x,y,width,height = classes
                x1,y1,x2,y2 = convert_yolo_to_box(x, y, width, height, width_img, height_img)
                yolo_x, yolo_y, yolo_width, yolo_height = convert_box_to_yolo(x1,y1-(k*10),x2,y2-(k*10), width_img-(k*10), height_img-(k*10))
                newCordinate.append([clased[counter_classs],yolo_x, yolo_y, yolo_width, yolo_height])
            name = "top-right-"+str(0) +str(k*10)
            file_path = "to/"+user+"-"+filename[:-4]+"-"+name+".txt"
            with open(file_path, 'w') as file:
                for line in newCordinate:
                    line_str = ' '.join(str(item) for item in line)
                    file.write(line_str + '\n')
            left = 0
            top = 0+(k*10)
            right = width_img -(k*10)
            bottom = height_img
            im1 = im.crop((left, top, right, bottom))
            im1.save("to/"+user+"-"+filename[:-4]+"-"+name+".png")