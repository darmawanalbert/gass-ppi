from sklearn.metrics import roc_auc_score, average_precision_score, precision_score, recall_score, matthews_corrcoef, confusion_matrix

def evaluate_ppi(actual_interface, predicted_interface, protein_structure):
    """Evaluate PPI
    Given the actual interface and its predicted interface, calculate some performance metrics.
    Calculated using scikit-learn

    Parameters:
    actual_interface (list[Residue]): List of Residue objects which represents the experimentally proven interface
    predicted_inteface (list[Residue]): List of Residue objects which represents the predicted interface from GASS-PPI
    protein_structure (list[Residue]): List of Residue objects which represents the entire protein structure

    Returns:
    float: Precision (Positive Predictive Value) score
    float: Recall (Sensitivity/True Positive Rate) score
    float: AUC-ROC score
    float: AUC-PR score
    float: Matthew's Correlation Coefficient score
    float: Specificity (True Negative Rate) score
    float: NPV (Negative Predictive Value) score

    """
    # Additional reference: https://en.m.wikipedia.org/wiki/Evaluation_of_binary_classifiers

    # From predicted interface, convert it into 0/1 label (y_pred)
    y_pred = [1 if is_residue_in_interface(residue, predicted_interface) else 0 for residue in protein_structure]

    # From actual interface, convert it into 0/1 label (y_actual)
    y_actual = [1 if is_residue_in_interface(residue, actual_interface) else 0 for residue in protein_structure]

    # Based on the actual and predicted labels, calculate the metrics using sklearn.metrics functions
    # https://scikit-learn.org/stable/modules/model_evaluation.html
    tn, fp, fn, tp = confusion_matrix(y_actual, y_pred).ravel()

    precision = precision_score(y_actual, y_pred)
    recall = recall_score(y_actual, y_pred)
    auc_roc = roc_auc_score(y_actual, y_pred)
    auc_pr = average_precision_score(y_actual, y_pred)
    mcc = matthews_corrcoef(y_actual, y_pred)
    specificity = tn / (tn + fp)
    npv = tn / (tn + fn)

    return (precision, recall, auc_roc, auc_pr, mcc, specificity, npv)
