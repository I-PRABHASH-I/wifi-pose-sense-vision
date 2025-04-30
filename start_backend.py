
import os
import sys

# Create necessary directories
os.makedirs('backend/model/saved_models', exist_ok=True)

# Check if model exists
model_path = os.path.join('backend', 'model', 'saved_models', 'best_model.pth')
if not os.path.exists(model_path):
    print("Warning: Trained model not found. Please run the training pipeline first.")
    print("Running: python run_pipeline.py")
    os.system('python run_pipeline.py')

# Start Flask backend
print("Starting Flask backend...")
os.chdir('backend')
os.system('python app.py')
