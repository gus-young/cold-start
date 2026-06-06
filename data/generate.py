import random
import csv

#generae runs.csv
count = 101
n = range(count)

data_entries = []
model_type = "xgboost", "random_forest", "logistic_regression", "svm"
dataset = "dataset_a", "dataset_b", "dataset_c"
learning_rate = (0.01, 0.1, 0.001)
estimator_options = 50, 100, 200, 500
status_qty = 6

status_list = []
for i in range (status_qty): 
    status_list.append("running")
for i in range (status_qty * 2):
    status_list.append("failed")
while len(status_list) < count:
    status_list.append("completed")
random.shuffle(status_list)

for i in n: 
    row_model = random.choice(model_type)
    row_status = status_list[i]

    if row_model == "logistic_regression":
        training_time = random.randint(1, 30)
    elif row_model == "svm":
        training_time = random.randint(10,120)
    elif row_model == "random_forest":
        training_time = random.randint(5,60)
    elif row_model == "xgboost":
        training_time = random.randint(3,45)

    entry = dict(
        run_id = f"run_{i:03d}",
        model_type = row_model,
        dataset = random.choice(dataset),
        learning_rate = None if row_model == "random_forest" or row_model == "svm" else random.choice(learning_rate),
        max_depth = None if row_model == "logistic_regression" or row_model == "svm" else random.randint(3,10),
        n_estimators = None if row_model == "logistic_regression" or row_model == "svm" else random.choice(estimator_options),
        train_accuracy = round(random.uniform(0.65, 0.95), 3),
        val_accuracy = None if row_status == "running" or row_status == "failed" else round(random.uniform(0.65, 0.95), 3),
        train_time_seconds = training_time,
        status = row_status
    )
    data_entries.append(entry)

## Create CSV ##
fieldnames = [
    "run_id",
    "model_type", 
    "dataset",
    "learning_rate",
    "max_depth",
    "n_estimators",
    "train_accuracy",
    "val_accuracy",
    "train_time_seconds",
    "status"
    ]

with open('output/runs.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    # Initialize the DictWriter
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # 1. Write the header row
    writer.writeheader()
    
    # 2. Write rows (accepts an iterable of dictionaries)
    writer.writerows(data_entries)