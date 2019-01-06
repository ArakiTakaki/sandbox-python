import json
import os
import pickle


class Store:
    # シリアライズするストアの名前
    store_name = None

    def __init__(self, name='sample', test=1):
        self.test = test
        self.store_name = "{name}.pickle".format(name=name)

    @classmethod
    def load(self, name):
        store = "{name}.pickle".format(name=name)

        # 存在チェック
        if not os.path.exists(store):
            return None

        with open(store, mode='rb') as f:
            return pickle.load(f)

    def dump(self):
        with open(self.store_name, mode='wb') as f:
            pickle.dump(self, f)

    def loadJSON(self, json):
        pass

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
