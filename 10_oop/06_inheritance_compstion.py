class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chaiii....")

class masalaChai(BaseChai):
    def add_spices(self):
        print("Adding spices to the chaiii....")


class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")


    def server(self):
        print(f"Serving {self.chai.type} the chaiii....")
        self.chai.prepare()

class fancyChaiShop(ChaiShop):
    chai_cls = masalaChai


shop = ChaiShop()
fancy = fancyChaiShop()
shop.server()
fancy.server()
fancy.chai.add_spices()