class chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength

class GingerChai(chai):
    def __init__(self, type_, strength, spice_level):
        self.type = type_
        self.strength = strength
        self.spice_level = spice_level

class GingerChai(chai):
    def __init__(self, type_, strength, ):
        chai.__init__(type_, strength)