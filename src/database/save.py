import pickle

def save_instance(instance, save_name):
    """Saves the inputed instance to a file"""
    with open(f"{save_name}.pickle", "wb") as file_:
        pickle.dump(instance, file_, -1)

