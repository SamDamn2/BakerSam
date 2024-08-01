from app.models.producto import Producto

class Carrito:
    def __init__(self):
        self.carrito = []

    def agregar_producto(self, producto_id, cantidad):
        producto = Producto.query.get(producto_id)
        if producto:
            item = {'producto': producto, 'cantidad': cantidad}
            self.carrito.append(item)

    def eliminar_producto(self, idproducto):
        # Lógica para eliminar producto del carrito
        self.carrito = [item for item in self.carrito if item['producto'].idproducto != idproducto]

    def calcular_total(self):
        return sum(item['producto'].preciopdo * item['cantidad'] for item in self.carrito)
    
    def tamañoD(self):   
        return len(self.carrito)

    def getItems(self):
        return self.carrito
    
    def vaciarcarrito(self):
        self.carrito = []