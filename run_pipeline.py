
import os
import sys

# Create necessary directories
os.makedirs('data', exist_ok=True)
os.makedirs('data/train_data', exist_ok=True)
os.makedirs('data/test_data', exist_ok=True)
os.makedirs('data/test_samples', exist_ok=True)
os.makedirs('backend/model/saved_models', exist_ok=True)

# Step 1: Generate synthetic dataset
print("Step 1: Generating synthetic WiFi CSI dataset...")
from synthetic_data_generator import SyntheticDataGenerator
generator = SyntheticDataGenerator()
generator.save_dataset(train_ratio=0.8)
print("Dataset generation completed.")

# Step 2: Generate test samples for frontend testing
print("\nStep 2: Generating individual test samples...")
from generate_test_samples import generate_test_samples
generate_test_samples()
print("Test samples generation completed.")

# Step 3: Train the LSTM model
print("\nStep 3: Training the LSTM model...")
from model.lstm_model import ModelTrainer

# Initialize and train model
input_size = 256  # Number of CSI subcarriers
trainer = ModelTrainer(input_size)
trainer.train(
    train_csv='data/train_data/wifi_csi_train.csv',
    valid_csv='data/test_data/wifi_csi_test.csv',
    num_epochs=20,  # Reduced for faster training during development
    batch_size=32
)
print("Model training completed.")

# Step 4: Test the model with test samples
print("\nStep 4: Testing the model with individual samples...")
from test_model import test_model
test_model()
print("Model testing completed.")

print("\nPipeline execution completed successfully!")
print("You can now start the Flask backend and React frontend.")
