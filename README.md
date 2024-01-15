## Install tensorflow
pip install tensorflow

## Install tf2onnx (https://github.com/onnx/tensorflow-onnx)
pip install -U tf2onnx

## Convert tensorflow model to onnx
python -m tf2onnx.convert --saved-model tensorflow-model-path --output model.onnx

## Model output
### model_with_other
model_with_other should output an array of size 7.

- index 0 = likelihood for Time symbol
- index 1 = likelihood for Wind symbol
- index 2 = likelihood for Fire symbol
- index 3 = likelihood for Earth symbol
- index 4 = likelihood for Water symbol
- index 5 = likelihood for Lightning symbol
- index 6 = likelihood for Other symbol
