from director import Director
from concretebuilder1 import ConcreteBuilder1

director = Director()
builder = ConcreteBuilder1()
director.builder = builder

print("Produkt podstawowy:")
director.built_minimal_product()
builder.product.list_parts()

print("\n______________________________")

print("Produkt pełny:")
director.built_full_product()
builder.product.list_parts()

print("\n______________________________")

print("Produkt użytkownika:")
builder.produce_part_a()
builder.produce_part_c()
builder.product.list_parts()