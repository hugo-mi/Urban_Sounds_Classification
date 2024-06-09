import torch
from device import device
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
# ----------------------------
# Inference
# ----------------------------

def inference (model, val_dl):
  correct_prediction = 0
  total_prediction = 0
  all_preds = []
  all_labels = []

  # Disable gradient updates
  with torch.no_grad():
    for data in val_dl:
      # Get the input features and target labels, and put them on the GPU
      inputs, labels = data[0].to(device), data[1].to(device)

      # Normalize the inputs
      inputs_m, inputs_s = inputs.mean(), inputs.std()
      inputs = (inputs - inputs_m) / inputs_s

      # Get predictions
      outputs = model(inputs)

      # Get the predicted class with the highest score
      _, prediction = torch.max(outputs,1)
      all_preds.extend(prediction)
      all_labels.extend(labels)
      # Count of predictions that matched the target label
      correct_prediction += (prediction == labels).sum().item()
      total_prediction += prediction.shape[0]
  
  acc = correct_prediction/total_prediction
  print(f'Accuracy: {acc:.2f}, Total items: {total_prediction}')

  print(classification_report(all_labels, all_preds))
  sns.heatmap(confusion_matrix(all_labels, all_preds))