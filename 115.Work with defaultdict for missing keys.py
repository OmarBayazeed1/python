#115.Work with defaultdict for missing keys
from collections import defaultdict


# three levels: customer → product → paied → count
grouped = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

orders = [
    {"customer": "Alice", "product": "Laptop",'paied':'yes'},
    {"customer": "Bob", "product": "Phone",'paied':'no'},
    {"customer": "Alice", "product": "Mouse",'paied':'yes'},
    {"customer": "Alice", "product": "Mouse",'paied':'yes'},
    {"customer": "Alice", "product": "Mouse",'paied':'yes'},
    {"customer": "Alice", "product": "Mouse",'paied':'no'},
    {"customer": "Alice", "product": "Mouse",'paied':'no'},
    {"customer": "Alice", "product": "Phone",'paied':'yes'},
    {"customer": "Bob", "product": "Laptop",'paied':'no'},
]

for order in orders:
    cust, prod = order["customer"], order["product"]
    paied = order.get("paied", "unknown")
    grouped[cust][prod][paied] += 1

# convert to normal dicts for pretty printing
import pprint

def deep_convert(d):
    if isinstance(d, defaultdict):
        d = {k: deep_convert(v) for k, v in d.items()}
    return d

pprint.pprint(deep_convert(grouped))





