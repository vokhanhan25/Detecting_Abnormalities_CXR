import os

# path_model = 'weights/best.pt'
# path_image = '../img/image.png'
# path_result = '../img/result.png'
 
path_model = 'public/model/best.pt'
path_image = 'public/img/image.png'
path_result = 'yolov5/runs/detect/exp/image.png'

def predict(path_image, path_model):
    """
    Function to infer image

    Args:
    path_image -- path of input image
    path_model -- path of model to use

    Returns:
    path_result -- path of output image
    """
    os.system(f'python yolov5/detect.py   --weights {path_model} \
                                    --img 256 \
                                    --conf 0.01 \
                                    --iou 0.4 \
                                    --source {path_image} \
                                    --save-txt --save-conf --exist-ok > output.txt')
    # os.system(f'mv ../yolov5/ ../public/img/result.png')

predict(path_image, path_model)