from PIL import Image
import os
def convert_yolo_to_box(x, y, width, height, image_width, image_height):
    # Convert relative coordinates to absolute coordinates
    abs_x = x * image_width
    abs_y = y * image_height
    
    # Calculate the absolute width and height of the bounding box
    abs_width = width * image_width
    abs_height = height * image_height
    
    # Calculate the coordinates of the top-left and bottom-right points
    x1 = abs_x - (abs_width / 2)
    y1 = abs_y - (abs_height / 2)
    x2 = abs_x + (abs_width / 2)
    y2 = abs_y + (abs_height / 2)
    
    return x1, y1, x2, y2

def convert_box_to_yolo(x1, y1, x2, y2, image_width, image_height):
    # Calculate the center coordinates of the bounding box
    box_width = x2 - x1
    box_height = y2 - y1
    box_center_x = x1 + (box_width / 2)
    box_center_y = y1 + (box_height / 2)
    
    # Normalize the coordinates
    yolo_x = box_center_x / image_width
    yolo_y = box_center_y / image_height
    yolo_width = box_width / image_width
    yolo_height = box_height / image_height
    
    return yolo_x, yolo_y, yolo_width, yolo_height
# im = Image.open("example/kubre-0-left-00.png")
# width,height = im.size
# x,y,yolo_width,yolo_height=0.772266,0.780556,0.081250,0.112500
# x1,y1,x2,y2 = convert_yolo_to_box(x, y, yolo_width, yolo_height,width, height)
# im1 = im.crop((x1,y1,x2,y2))
# im1.show()