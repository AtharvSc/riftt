
import joblib
import json
import numpy as np

try:
    scaler = joblib.load('vcf_feature_extractor/models/ensemble_scaler.pkl')
    print("Scaler Mean:", list(scaler.mean_))
    print("Scaler Scale:", list(scaler.scale_))
except Exception as e:
    print(f"Error: {e}")
