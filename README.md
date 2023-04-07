## Install tensorflow
pip install tensorflow

## Install tf2onnx (https://github.com/onnx/tensorflow-onnx)
pip install -U tf2onnx

## Convert tensorflow model to onnx
python -m tf2onnx.convert --saved-model tensorflow-model-path --output model.onnx

## Model output
### model_with_other
model_with_other should output an array of size 3.

- index 0 = likelihood for Time symbol
- index 1 = likelihood for Wind symbol
- index 2 = likelihood for Other symbol

Each float represents the likelihood for each class.  
e.g. (0.8,0.2,0)  
80% likelihood for Time  
20% likelihood for Wind  
0% likelihood for Other  

### model_without_other
model_without_other should output an array of size 2.

- index 0 = likelihood for Time symbol
- index 1 = likelihood for Wind symbol

Each float represents the likelihood for each class.  
e.g. (0.8,0.2)  
80% likelihood for Time  
20% likelihood for Wind  
