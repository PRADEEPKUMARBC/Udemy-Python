def chai_flavour(flavour="samosa"):
    """
    Return the flavour of chai.
    """
    chai="ginger"
    return flavour


print(chai_flavour.__doc__)
print(chai_flavour.__name__)

help(len)

def generate_bill(chai=0, samosa=0):
    """
    Calculate the total bill for chai and samose
    :param chai: Number of chai cups (10 rupees for each)
    :param samose: Number of samose (15 rupees for each)
    :return: (total amount , thank you message as string)
    """

    total = chai * 10 + samosa * 15
    return total , "Tnakyou visiting chaicode.com"
