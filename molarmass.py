#!/bin/python3
# Tool to calculate the mass of a molecule in u (and thus to calculate that molecule's g/mol)

# Made by Thijmen Voskuilen (thijmen@thijmer.nl). You can edit, distribute or do anything other you want to do with this file, as long as you leave my credits in it. I would also like to know what you have added if you edit the file, but that isn't necessary.
# My github: https://github.com/thijmer

import sys

element_weights = {
    'H': 1.008,
    'He': 4.0026022,
    'Li': 6.94,
    'Be': 9.01218315,
    'B': 10.81,
    'C': 12.011,
    'N': 14.007,
    'O': 15.999,
    'F': 18.9984031636,
    'Ne': 20.17976,
    'Na': 22.989769282,
    'Mg': 24.305,
    'Al': 26.98153857,
    'Si': 28.085,
    'P': 30.9737619985,
    'S': 32.06,
    'Cl': 35.45,
    'Ar': 39.9481,
    'K': 39.09831,
    'Ca': 40.0784,
    'Sc': 44.9559085,
    'Ti': 47.8671,
    'V': 50.94151,
    'Cr': 51.99616,
    'Mn': 54.9380443,
    'Fe': 55.8452,
    'Co': 58.9331944,
    'Ni': 58.69344,
    'Cu': 63.5463,
    'Zn': 65.382,
    'Ga': 69.7231,
    'Ge': 72.6308,
    'As': 74.9215956,
    'Se': 78.9718,
    'Br': 79.904,
    'Kr': 83.7982,
    'Rb': 85.46783,
    'Sr': 87.621,
    'Y': 88.905842,
    'Zr': 91.2242,
    'Nb': 92.906372,
    'Mo': 95.951,
    'Tc': 98,
    'Ru': 101.072,
    'Rh': 102.905502,
    'Pd': 106.421,
    'Ag': 107.86822,
    'Cd': 112.4144,
    'In': 114.8181,
    'Sn': 118.7107,
    'Sb': 121.7601,
    'Te': 127.603,
    'I': 126.904473,
    'Xe': 131.2936,
    'Cs': 132.905451966,
    'Ba': 137.3277,
    'La': 138.905477,
    'Ce': 140.1161,
    'Pr': 140.907662,
    'Nd': 144.2423,
    'Pm': 145,
    'Sm': 150.362,
    'Eu': 151.9641,
    'Gd': 157.253,
    'Tb': 158.925352,
    'Dy': 162.5001,
    'Ho': 164.930332,
    'Er': 167.2593,
    'Tm': 168.934222,
    'Yb': 173.0451,
    'Lu': 174.96681,
    'Hf': 178.492,
    'Ta': 180.947882,
    'W': 183.841,
    'Re': 186.2071,
    'Os': 190.233,
    'Ir': 192.2173,
    'Pt': 195.0849,
    'Au': 196.9665695,
    'Hg': 200.5923,
    'Tl': 204.38,
    'Pb': 207.21,
    'Bi': 208.980401,
    'Po': 209,
    'At': 210,
    'Rn': 222,
    'Fr': 223,
    'Ra': 226,
    'Ac': 227,
    'Th': 232.03774,
    'Pa': 231.035882,
    'U': 238.028913,
    'Np': 237,
    'Pu': 244,
    'Am': 243,
    'Cm': 247,
    'Bk': 247,
    'Cf': 251,
    'Es': 252,
    'Fm': 257,
    'Md': 258,
    'No': 259,
    'Lr': 266,
    'Rf': 267,
    'Db': 268,
    'Sg': 269,
    'Bh': 270,
    'Hs': 269,
    'Mt': 278,
    'Ds': 281,
    'Rg': 282,
    'Cn': 285,
    'Nh': 286,
    'Fl': 289,
    'Mc': 289,
    'Lv': 293,
    'Ts': 294,
    'Og': 294,
    'Uue': 315
}


def separate_formula(formula):
    elements = []
    curr_element = ""
    for letter in formula:
        if letter.isupper():
            elements.append(curr_element)
            curr_element = letter
        else:
            curr_element += letter
    elements.append(curr_element)
    elements = [x for x in elements if len(x) > 0]
    return elements


def count_elements(formula):
    elements = separate_formula(formula)

    counted_elements = []

    for element in elements:
        numberstartindex = len(element)
        index = 0
        for letter in element:
            if letter.isnumeric():
                numberstartindex = index
                break
            index += 1
        element_letters = element[:numberstartindex]
        element_count = element[numberstartindex:]
        if element_count == "":
            element_count = 1
        element_count = int(element_count)
        counted_elements.append([element_letters, element_count])
    return counted_elements


def process_formula(formula):
    weight = 0
    elements = count_elements(formula)
    for element in elements:
        try:
            element_weight = element_weights[element[0]]
        except KeyError:
            return "Element '%s' does not exist (as far as I know)." % element[0]
        element_count = element[1]
        weight += element_weight * element_count
    return weight

if __name__ == "__main__":
	if len(sys.argv) != 2:
	    formula = input("Formula: ")
	else:
	    formula = sys.argv[1]
	print(process_formula(formula))
