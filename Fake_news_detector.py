import numpy as np
from sklearn.linear_model import LinearRegression

def predict_next_number():
    # Take input from the user as a sequence of integers
    sequence = list(map(int, input("Enter a sequence of numbers separated by spaces: ").split()))
    
    if len(sequence) < 2:
        print("Please enter at least two numbers to find a pattern.")
        return
    
    # Prepare training data (X as indices, y as values)
    X = np.array(range(1, len(sequence) + 1)).reshape(-1, 1)  # Reshape for sklearn
    y = np.array(sequence)
    
    # Train a simple linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict the next number in sequence
    next_index = np.array([[len(sequence) + 1]])
    next_number = model.predict(next_index)[0]
    
    print(f"Predicted next number: {round(next_number)}")

if __name__ == "__main__":
    predict_next_number()
