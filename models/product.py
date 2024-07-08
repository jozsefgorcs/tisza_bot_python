from dataclasses import dataclass


@dataclass
class Product:
    url: str
    name: str
    price: str
    currency: str
    size: str

    def __repr__(self):
        return f"<Product {self.name} {self.price} {self.currency} {self.size}>"

    def print_to_message(self):
        return f"Name: {self.name} - size: {self.size}, {self.price} {self.currency} {self.url}"
