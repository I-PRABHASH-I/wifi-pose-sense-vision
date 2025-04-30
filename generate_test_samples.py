
from synthetic_data_generator import SyntheticDataGenerator
import pandas as pd
import os

def generate_test_samples():
    """Generate one sample for each pose class for testing."""
    generator = SyntheticDataGenerator()
    test_samples = []
    
    # Generate one sample for each pose class
    for pose_class in generator.pose_classes:
        # Generate CSI data
        csi_data = generator.generate_csi_data(pose_class)
        joint_coords = generator.generate_joint_coordinates(pose_class)
        human_presence = 1 if pose_class != 'no_human' else 0
        
        sample = {
            'pose_class': pose_class,
            'human_presence': human_presence
        }
        
        # Add CSI amplitudes
        for i, amp in enumerate(csi_data):
            sample[f'csi_{i}'] = amp
        
        # Add joint coordinates
        for i in range(generator.num_joints):
            sample[f'joint_{i}_x'] = joint_coords[i*2]
            sample[f'joint_{i}_y'] = joint_coords[i*2 + 1]
        
        test_samples.append(sample)
    
    # Convert to DataFrame
    df = pd.DataFrame(test_samples)
    
    # Create test samples directory
    os.makedirs('data/test_samples', exist_ok=True)
    
    # Save individual samples
    for i, row in df.iterrows():
        filename = f"test_sample_{row['pose_class']}.csv"
        row.to_frame().T.to_csv(f'data/test_samples/{filename}', index=False)
        print(f"Generated {filename}")

if __name__ == "__main__":
    generate_test_samples()
