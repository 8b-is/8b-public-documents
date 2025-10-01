import numpy as np

def predict_future_state(current_state, weights):
    """
    Predicts the next state using linear function approximation.
    
    Parameters:
    - current_state: A numpy array representing the current state features.
    - weights: A numpy array of weights for the linear model.
    
    Returns:
    - predicted_state: A numpy array representing the predicted next state.
    """
    # Ensure inputs are numpy arrays
    current_state = np.array(current_state)
    weights = np.array(weights)
    
    # Linear prediction
    predicted_state = np.dot(current_state, weights)
    
    return predicted_state
