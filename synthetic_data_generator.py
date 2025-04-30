
import numpy as np
import pandas as pd
from sklearn.utils import shuffle
import os

class SyntheticDataGenerator:
    def __init__(self):
        self.num_subcarriers = 256  # WiFi 6 subcarriers
        self.num_joints = 17  # Number of skeleton joints
        self.pose_classes = ['stand', 'sit', 'kneel', 'sleep', 'no_human']
        self.samples_per_class = {
            'stand': 1300,
            'sit': 1300,
            'kneel': 1300,
            'sleep': 1300,
            'no_human': 800
        }

    def generate_joint_coordinates(self, pose_class):
        """Generate synthetic joint coordinates based on pose class."""
        if pose_class == 'no_human':
            return np.zeros(self.num_joints * 2)  # x,y coordinates for each joint

        # Base coordinates for different poses
        base_coords = {
            'stand': np.array([
                0.5, 0.9,   # head
                0.5, 0.8,   # neck
                0.5, 0.7,   # spine
                0.5, 0.5,   # hip
                0.4, 0.7,   # left shoulder
                0.3, 0.5,   # left elbow
                0.2, 0.4,   # left wrist
                0.6, 0.7,   # right shoulder
                0.7, 0.5,   # right elbow
                0.8, 0.4,   # right wrist
                0.4, 0.3,   # left hip
                0.3, 0.2,   # left knee
                0.3, 0.1,   # left ankle
                0.6, 0.3,   # right hip
                0.7, 0.2,   # right knee
                0.7, 0.1,   # right ankle
                0.5, 0.6    # center
            ]),
            'sit': np.array([
                0.5, 0.7,   # head
                0.5, 0.6,   # neck
                0.5, 0.5,   # spine
                0.5, 0.4,   # hip
                0.4, 0.5,   # left shoulder
                0.3, 0.4,   # left elbow
                0.2, 0.4,   # left wrist
                0.6, 0.5,   # right shoulder
                0.7, 0.4,   # right elbow
                0.8, 0.4,   # right wrist
                0.4, 0.4,   # left hip
                0.3, 0.2,   # left knee
                0.3, 0.1,   # left ankle
                0.6, 0.4,   # right hip
                0.7, 0.2,   # right knee
                0.7, 0.1,   # right ankle
                0.5, 0.5    # center
            ]),
            'kneel': np.array([
                0.5, 0.8,   # head
                0.5, 0.7,   # neck
                0.5, 0.6,   # spine
                0.5, 0.5,   # hip
                0.4, 0.6,   # left shoulder
                0.3, 0.5,   # left elbow
                0.2, 0.4,   # left wrist
                0.6, 0.6,   # right shoulder
                0.7, 0.5,   # right elbow
                0.8, 0.4,   # right wrist
                0.4, 0.3,   # left hip
                0.4, 0.2,   # left knee
                0.4, 0.1,   # left ankle
                0.6, 0.3,   # right hip
                0.6, 0.2,   # right knee
                0.6, 0.1,   # right ankle
                0.5, 0.4    # center
            ]),
            'sleep': np.array([
                0.2, 0.5,   # head
                0.3, 0.5,   # neck
                0.4, 0.5,   # spine
                0.5, 0.5,   # hip
                0.3, 0.6,   # left shoulder
                0.2, 0.6,   # left elbow
                0.1, 0.6,   # left wrist
                0.3, 0.4,   # right shoulder
                0.2, 0.4,   # right elbow
                0.1, 0.4,   # right wrist
                0.6, 0.5,   # left hip
                0.7, 0.5,   # left knee
                0.8, 0.5,   # left ankle
                0.6, 0.5,   # right hip
                0.7, 0.5,   # right knee
                0.8, 0.5,   # right ankle
                0.5, 0.5    # center
            ])
        }

        # Add random variations to make each sample unique
        coords = base_coords[pose_class].copy()
        noise = np.random.normal(0, 0.05, coords.shape)  # Random variations
        coords += noise
        coords = np.clip(coords, 0, 1)  # Ensure coordinates stay within [0,1]
        return coords

    def generate_csi_data(self, pose_class):
        """Generate synthetic CSI amplitudes based on pose class."""
        if pose_class == 'no_human':
            base_amplitude = np.random.normal(0.5, 0.1, self.num_subcarriers)
        else:
            # Generate more complex patterns for human presence
            x = np.linspace(0, 2*np.pi, self.num_subcarriers)
            base_amplitude = 0.5 + 0.3 * np.sin(x) + 0.2 * np.cos(2*x)
            
            # Add pose-specific variations
            if pose_class == 'stand':
                base_amplitude += 0.1 * np.sin(3*x)
            elif pose_class == 'sit':
                base_amplitude += 0.1 * np.cos(3*x)
            elif pose_class == 'kneel':
                base_amplitude += 0.1 * np.sin(4*x)
            elif pose_class == 'sleep':
                base_amplitude += 0.1 * np.cos(4*x)

        # Add random noise
        noise = np.random.normal(0, 0.05, self.num_subcarriers)
        amplitude = base_amplitude + noise
        return np.clip(amplitude, 0, 1)  # Normalize to [0,1]

    def generate_dataset(self):
        """Generate complete synthetic dataset."""
        data = []
        
        for pose_class in self.pose_classes:
            num_samples = self.samples_per_class[pose_class]
            for _ in range(num_samples):
                csi_data = self.generate_csi_data(pose_class)
                joint_coords = self.generate_joint_coordinates(pose_class)
                human_presence = 1 if pose_class != 'no_human' else 0
                
                sample = {
                    'pose_class': pose_class,
                    'human_presence': human_presence
                }
                
                # Add CSI amplitudes
                for i, amp in enumerate(csi_data):
                    sample[f'csi_{i}'] = amp
                
                # Add joint coordinates
                for i in range(self.num_joints):
                    sample[f'joint_{i}_x'] = joint_coords[i*2]
                    sample[f'joint_{i}_y'] = joint_coords[i*2 + 1]
                
                data.append(sample)
        
        # Convert to DataFrame and shuffle
        df = pd.DataFrame(data)
        df = shuffle(df, random_state=42)
        return df

    def save_dataset(self, train_ratio=0.8):
        """Generate and save train/test datasets."""
        print("Generating synthetic WiFi CSI dataset...")
        df = self.generate_dataset()
        
        # Split into train and test sets
        train_size = int(len(df) * train_ratio)
        train_df = df[:train_size]
        test_df = df[train_size:]
        
        # Create directories if they don't exist
        os.makedirs('data/train_data', exist_ok=True)
        os.makedirs('data/test_data', exist_ok=True)
        
        # Save datasets
        train_df.to_csv('data/train_data/wifi_csi_train.csv', index=False)
        test_df.to_csv('data/test_data/wifi_csi_test.csv', index=False)
        print(f"Generated {len(train_df)} training samples and {len(test_df)} test samples")

if __name__ == "__main__":
    generator = SyntheticDataGenerator()
    generator.save_dataset()
