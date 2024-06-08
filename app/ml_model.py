import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_model(data):
    df = pd.read_csv(data)
    X = df.drop('target', axis=1)
    y = df['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)

def predict(input_data):
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model.predict(input_data)
