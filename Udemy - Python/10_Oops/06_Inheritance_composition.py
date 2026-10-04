class Basechai():
    def __init__(self, type_):
        self.type = type

    def preparing(self):
        return f"Preparing {self.type} Chai"


class Masalachai(Basechai):
    def add_spices(self):
        print("Adding cardmom, ginger, cloves")

class ChaiShop:
    chai_cls = Basechai

    def __init__(self):
        self.chai = self.chai_cls("Masala")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

class FancyChaiShop():
    chai_cls = Masalachai

shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai_cls.add_spices()