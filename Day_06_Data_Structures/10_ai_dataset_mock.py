# 10_ai_dataset_mock.py
# Concept: List of Dictionaries - Common Data Science structure

# Mock dataset representing rows from a Kaggle CSV file
dataset = [
    {"id": 1, "label": "Cat", "confidence": 0.98, "processed": True},
    {"id": 2, "label": "Dog", "confidence": 0.45, "processed": False},
    {"id": 3, "label": "Bird", "confidence": 0.88, "processed": True},
    {"id": 4, "label": "Cat", "confidence": 0.72, "processed": True},
    {"id": 5, "label": "Dog", "confidence": 0.91, "processed": True}
]

print(f"Dataset contains {len(dataset)} items.")

# 1. Filtering: Keep only processed items with confidence > 0.8
filtered_data = [
    row for row in dataset 
    if row['processed'] and row['confidence'] > 0.8
]

print("\n--- High Confidence Processed Data ---")
for row in filtered_data:
    print(row)

# 2. Aggregation: Count occurrences of each label
label_counts = {}
for row in dataset:
    label = row['label']
    label_counts[label] = label_counts.get(label, 0) + 1

print("\n--- Label Distribution ---")
for label, count in label_counts.items():
    print(f"{label}: {count}")

# 3. Data Transformation: List of labels from high confidence data
high_conf_labels = [row['label'] for row in filtered_data]
print(f"\nHigh Confidence Labels: {high_conf_labels}")
