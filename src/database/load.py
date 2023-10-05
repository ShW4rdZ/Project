import pickle, pprint

def load_instance(save_name):
    with open(f"{save_name}.pickle", "rb") as file_:
        data = pickle.load(file_)
        return data
    return False
