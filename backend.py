import os
import cv2
import pandas as pd
from deepface import DeepFace
from retinaface import RetinaFace


def install_requirement():
    # Install requirement
    os.system("pip install -r requirement.txt")


def image_folder(img_path):
    '''This function takes the path of the image folder and returns the list of images in the folder'''
    img_list = [os.path.join(img_path, img) for img in os.listdir(img_path)]
    return img_list

def analyse_face(img_list):
    results = []
    for img_path in img_list:
        try:
            img = cv2.imread(img_path)
            faces = RetinaFace.detect_faces(img_path)
            for face_key in faces:
                face = faces[face_key]
                facial_area = img[face['facial_area'][1]:face['facial_area'][3], face['facial_area'][0]:face['facial_area'][2]]
                result = DeepFace.analyze(facial_area, actions=['gender', 'emotion', 'race'], enforce_detection=False)
                temp = {}
                temp['image_path'] = img_path #adding the file path to the result
                temp['face_key'] = face_key
                temp['dominant_emotion'] = result[0]['dominant_emotion'].lower()
                temp['dominant_gender']= result[0]['dominant_gender'].lower()
                temp['dominant_race']= result[0]['dominant_race'].lower()
                results.append(temp)
        except:
            continue
    df = pd.DataFrame(results)
    return df

if __name__ == "__main__":
    install_requirement()
    df = analyse_face(img_list=image_folder('img_Dataset'))
    print(df.head())