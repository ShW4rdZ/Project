import pickle, pprint

def load_instance(save_name):
    """Loads an instance of a class from a saved file"""
    with open(f"{save_name}.pickle", "rb") as file_:
        data = pickle.load(file_)
        return data
