
# Saathi

An AI powered agriculture utility platform
## Features

- Plant disease detection(Detects upto 33 classes)
- Crop recommendation based on soil quality and environmental factors
- Information about different crops



## Tech Stack

**ML/DL:** Tensorflow, Keras, Scikit

**Web:** Flask, Bootstrap

## Installation

There are 2 parts in this project

#### ML/DL

In the models directory there are two folders 'recommender-models' & 'cnn'. Recommender-models has all the models related to crop recommendation system and cnn folder contains all the notebooks and models related to plant disease classification.

#### Web

```bash
  python3 -m venv venv
  cd Saathi/webapp
  pip3 install -r requirements.txt
  python3 setup.py
```
## Results

### Crop Recommendation

| Algorithm   | Accuracy | Precision|Recall|F1-Score|
| :---        |    :----:   | :---: | :---: | :---: |
| Logistic Regression | 94.54 | 0.95   |0.95| 0.94  |
|Decision Tree|97.72|0.98|0.98|0.98|
|SVM|9.09|0.59|0.09|0.11|
|Multilayer Perceptron|95.22|0.96|0.95|0.95|
|Random Forest|99.31|0.99|0.99|0.99|

### Plant Disease Detection

| Architectures|Training Accuracy|Testing Accuracy|Validation Accuracy|
|:---|:---:|:---:|:---:|
|VGG16|92.18|91.33|91.78|
|ResNet50|96.02|95.41|95.53|
|EfficientNetV2|96.06|95.53|95.83|

