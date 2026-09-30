def pure_chai(cups):
    return cups * 10

total_chai = 0

def pour_chai(n):
    print(n)
    if n == 0:
        return "All Cups are Poured"
    return pour_chai(n - 1)

print(pour_chai(3))



chai_types = ["Light", "Kadak", "Ginger", "Kadak"]
strong_chai = list(filter(lambda chai: chai!="kadak", chai_types))
print(strong_chai)