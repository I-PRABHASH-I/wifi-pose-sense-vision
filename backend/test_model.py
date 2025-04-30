
import os
import pandas as pd
from model.lstm_model import ModelTrainer

def test_model():
    print("Testing WiFi Pose Guardian LSTM Model\n")
    
    # Initialize model
    input_size = 256  # Number of CSI subcarriers
    trainer = ModelTrainer(input_size)
    
    # Load model
    model_path = os.path.join('backend','model', 'saved_models', 'best_model.pth')
    if not os.path.exists(model_path):
        print(f"Error: No trained model found at {model_path}. Please run the training script first.")
        return
    
    trainer.load_model(model_path)
    print("Model loaded successfully")
    
    # Load test samples
    test_samples_dir = os.path.join('data', 'test_samples')
    if not os.path.exists(test_samples_dir):
        print(f"Error: No test samples found at {test_samples_dir}. Please run generate_test_samples.py first.")
        return
    
    # Test each sample
    for filename in os.listdir(test_samples_dir):
        if filename.endswith('.csv'):
            print(f"\nTesting {filename}...")
            
            # Load sample
            sample_path = os.path.join(test_samples_dir, filename)
            df = pd.read_csv(sample_path)
            
            # Extract features
            csi_columns = [col for col in df.columns if col.startswith('csi_')]
            features = df[csi_columns].values
            
            # Make prediction
            presence_pred, pose_pred = trainer.predict(features)
            
            # Print results
            print(f"True pose: {df['pose_class'].iloc[0]}")
            print(f"Predicted pose: {pose_pred[0]}")
            print(f"Human presence: {'Yes' if presence_pred > 0.5 else 'No'}")

if __name__ == "__main__":
    test_model()
