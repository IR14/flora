from roboflow import Roboflow
import os
import pickle
import json

# rf = Roboflow(api_key="sAA2PirCW9POEOYvCoWV")
# project = rf.workspace("pridch-kirpich-xmkm9").project("flora-cm3ry")
# model = project.version(2).model
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
WORK_DIR = os.path.join(ROOT_DIR, 'flora')
filename = os.path.join(WORK_DIR, 'model.sav')
img = os.path.join(WORK_DIR, 'test.jpg')
# pickle.dump(model, open(filename, 'wb'))

model = pickle.load(open(filename, 'rb'))
result = model.predict(img)

print(result.json()['predictions'][0]['class'])
