"""
Auxilary functions for data preprocessing
"""


def sanitze_name(name):
    """
    >>> sanitze_name("Adipose - Visceral (Omentum)")
    Adipose_Visceral_Omentum
    """
    name = name.replace(" - ", " ").replace("(", "").replace(")", "").replace(" ", "_")
    return name