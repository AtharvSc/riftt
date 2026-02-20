
try:
    import skl2onnx
    import onnxmltools
    print("ONNX tools found.")
except ImportError as e:
    print(f"Missing: {e}")
