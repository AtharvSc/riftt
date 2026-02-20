
import joblib
try:
    model = joblib.load('vcf_feature_extractor/models/ensemble_model.pkl')
    print("Model Type:", type(model))
except Exception as e:
    print(f"Error: {e}")
