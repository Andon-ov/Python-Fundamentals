# class Catalogue:
#     def __init__(self, name: str):
#         self.name = name
#         self.products = []
#
#     def add_product(self, product_name: str):
#         self.products.append(product_name)
#
#     def get_by_letter(self, first_letter: str):
#
#         temp_list = []
#         for i in self.products:
#             if i.startswith(first_letter):
#                 temp_list.append(i)
#         return temp_list
#
#     def __repr__(self):
#         output = f"Items in the {self.name} catalogue:\n"
#         output += '\n'.join(sorted(self.products))
#         return output
#
#
# catalogue = Catalogue("Furniture")
# catalogue.add_product("Sofa")
# catalogue.add_product("Mirror")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# print(catalogue.get_by_letter("C"))
# print(catalogue)


class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):

        temp_list = []
        for i in self.products:
            if i.startswith(first_letter):
                temp_list.append(i)
        return temp_list

    def __repr__(self):
        output = f"Items in the {self.name} catalogue:\n"
        output += '\n'.join(sorted(self.products))
        return output


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
