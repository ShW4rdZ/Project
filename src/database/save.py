import pickle

def save_instance(instance, save_name):
    with open(f"{save_name}.pickle", "wb") as file_:
        pickle.dump(instance, file_, -1)

