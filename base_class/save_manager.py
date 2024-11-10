import pickle
import os


class SaveManager:

    def __init__(self, engine):
        self.engine = engine

    def save(self):
        # with open(f"{os.path.dirname(os.getcwd())}\\saves\\save_file.txt", "bw") as file:
        with open("D:\\pythonProjects\\TtH\\saves\\save_file.txt", "bw") as file:
            file.write(pickle.dumps(self.engine))

    @staticmethod
    def load():
        # with open(f"{os.path.dirname(os.getcwd())}\\saves\\save_file.txt", "br") as file:
        with open("D:\\pythonProjects\\TtH\\saves\\save_file.txt", "br") as file:
            return pickle.loads(file.read())


