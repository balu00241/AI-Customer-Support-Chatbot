import json

def load_dataset():
    with open("dataset.json", "r") as file:
        return json.load(file)

def get_response(user_input, dataset):
    for keyword in dataset:
        if keyword in user_input.lower():
            return dataset[keyword]
    return "Let's try that again."
