from imageai.Detection import ObjectDetection
import os

def detect(inputFile, minProbability):
    model = os.path.join(os.getcwd(), "models\\yolo.h5")
    #model = os.path.join(os.getcwd(), "models\\resnet50_coco_best_v2.1.0.h5")

    detector = ObjectDetection()
    #detector.setModelTypeAsRetinaNet()
    detector.setModelTypeAsYOLOv3()
    #detector.setModelTypeAsTinyYOLOv3()
    detector.setModelPath(model)
    detector.loadModel(detection_speed="normal")
    detections = detector.detectObjectsFromImage(input_image=inputFile, output_type="array", minimum_percentage_probability=minProbability)

    detectionDict = []
    for eachObject in detections[1]:
        detectionDict.append((eachObject["name"], eachObject["percentage_probability"]))
    return detectionDict