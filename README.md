
# Anime Art Detection Dataset (v3_nisolate_padding)

## Overview
The **Anime Art Detection** dataset is a collection of 769 annotated images, designed to facilitate training models for detecting anime-style art. The dataset is annotated in YOLOv8 format, which is widely used for object detection tasks. 

The dataset was exported from **Roboflow** on December 13, 2023. The dataset was pre-processed to ensure uniformity and quality for computer vision tasks. 

## Dataset Information

- **Number of Images**: 769
- **Annotation Format**: YOLOv8
- **Image Size**: Resized to 640x640 (with black padding if aspect ratio differs)
- **Pre-processing Applied**:
  - Auto-orientation based on EXIF data (EXIF-orientation stripping)
  - Resize to 640x640 (with black padding for aspect ratio consistency)
  
- **Annotation Type**: Labels for detecting digital art in each image.

- **Export Date**: December 13, 2023

## Dataset Source

The dataset was created using **Roboflow**, an end-to-end computer vision platform that enables users to build, train, and deploy custom models efficiently. 

For more information on Roboflow, visit [https://roboflow.com](https://roboflow.com).

For state-of-the-art Computer Vision training notebooks, visit [Roboflow Notebooks](https://github.com/roboflow/notebooks).

## Usage

### Format

The dataset includes images and their corresponding annotations in **YOLOv8** format. Each image is paired with a text file containing annotations that describe the object(s) in the image.

- **Images**: Stored in their original resolution, resized to 640x640, and possibly padded with black edges.
- **Annotations**: Text files with the same name as the image (but with a `.txt` extension), containing the bounding box and label information.

The annotation format for YOLOv8 is:

```
<CLASS_ID> <CENTER_X> <CENTER_Y> <WIDTH> <HEIGHT>
```

Where:
- `CLASS_ID`: Integer representing the class of the object.
- `CENTER_X`, `CENTER_Y`: The normalized center of the bounding box (between 0 and 1).
- `WIDTH`, `HEIGHT`: The normalized width and height of the bounding box (between 0 and 1).

### How to Use the Dataset

1. **Download the Dataset**: You can download the dataset directly from [Roboflow Universe](https://universe.roboflow.com).
2. **Prepare for Training**: Use your preferred deep learning framework (such as PyTorch, TensorFlow, etc.) to load the images and annotations. The dataset can be used with pre-trained models such as YOLOv8.
3. **Training**: Train object detection models using your framework of choice. Roboflow provides seamless integration with popular frameworks, and it also supports exporting to other formats as needed.

### Example Usage with YOLOv8:
You can use the dataset with YOLOv8 for training by following the provided steps in the [YOLOv8 documentation](https://github.com/ultralytics/yolov8). Below is an example of how to load the dataset and train a model using YOLOv8:

```bash
# Clone repo

# Install dependencies
pip install -U -r requirements.txt

# Train YOLOv8 model with the Anime Art Detection dataset
python train.py --img 640 --batch 16 --epochs 50 --data your_dataset.yaml --cfg yolov8.yaml --weights yolov8.pt
```

## License

The dataset is provided for educational and research purposes. Please check the license associated with the dataset for any usage restrictions. You may need to credit the source if you use it in your work.
