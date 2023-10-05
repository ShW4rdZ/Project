import pickle
from ..inventory import Item

def save_instance(instance):
    with open("save.pickle", "wb") as file_:
        pickle.dump(instance, file_, -1)

if __name__ == "__main__":
    i = Item()

    save_instance(i)
