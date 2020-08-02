# thunder-detr predict_utils
# 

import numpy as np
from PIL import Image
import torchvision.transforms as tv

# use torchvision transforms for image prep...

resize_transform = tv.Resize(800)

without_resize_transform = tv.Compose([
    tv.ToTensor(),
    tv.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])  #Imagenet 
])

val_transform = tv.Compose([
    tv.Resize(800), 
    tv.ToTensor(),
    tv.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])  #Imagenet 
])

def make_cpu_array(box):
    '''move tensor from gpu to cpu and convert to array'''
    
    if not type(box) is np.ndarray:
        try:
            box = box.cpu().detach()
        except:
            print(f"failed to convert box to np.ndarray")
            return None
        
    box = np.asarray(box)
    return box



# actual predictions...

def thunder_detect(orig_img, model, min_confidence = .75):
    # orig_img is PIL image direct from drive..so first make a copy that we'll pass in as smaller image to detect
    pred_img = orig_img.copy()
    pred_img = resize_transform(pred_img) #resize to prediction size

    scores, boxes = detect(pred_img, model, transform=val_transform .. #regular detr detect goes here)

    if len(boxes):
        boxes = [upscale_boxes(box, pred_img.size, orig_img.size) for box in boxes]
        boxes = torch.Tensor(boxes)

    return scores,boxes

# plot with upscaled boxes


def upscale_box(box, pred_size, orig_size):
    '''upscale box from image used for prediction back to actual image size'''

    x_scale = orig_size[0]/pred_size[0]
    y_scale = orig_size[1]/pred_size[1]

    # needs to be moved to cpu if run on gpu...
    #box = box.cpu().detach()
    # or 
    box = make_cpu_array(box)

    x, y, w, h = np.asarray(box)

    # upscale all dimensions
    x *= x_scale
    y *= y_scale
    w *= x_scale
    h *= y_scale

    upbox = np.asarray((x, y, w, h))
    return upbox
