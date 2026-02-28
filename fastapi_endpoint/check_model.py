import pickle
import pandas as pd
import numpy as np

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

print("Model type:", type(model))

if hasattr(model, 'feature_names_in_'):
    print("Feature names:", model.feature_names_in_)

def inspect_pipeline(pipeline):
    if hasattr(pipeline, 'steps'):
        print("\nPipeline steps:", [step[0] for step in pipeline.steps])
        for name, step in pipeline.steps:
            print(f"\nStep: {name}")
            if hasattr(step, 'transformers_'):
                for trans_name, trans, trans_cols in step.transformers_:
                    print(f"  Transformer '{trans_name}' on columns: {trans_cols}")
                    if hasattr(trans, 'categories_'):
                        for i, col in enumerate(trans_cols):
                            print(f"    Categories for {col}: {trans.categories_[i]}")
            elif hasattr(step, 'categories_'):
                 print(f"  Categories: {step.categories_}")
            
            if hasattr(step, 'feature_names_in_'):
                print(f"  Step '{name}' features:", step.feature_names_in_)

inspect_pipeline(model)
