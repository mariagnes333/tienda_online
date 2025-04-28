from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos simulados (base de datos en memoria)
productos = [
    {"id": 1, "nombre": "Laptop", "precio": 1500},
    {"id": 2, "nombre": "Teclado", "precio": 50},
    {"id": 3, "nombre": "Mouse", "precio": 25},
    {"id": 4,"nombre": "Monitor","precio": 300}

]

# Ruta para obtener todos los productos
@app.route("/api/productos", methods=["GET"])
def obtener_productos():
    return jsonify(productos)

# Ruta para obtener un producto por ID
@app.route("/api/productos/<int:id>", methods=["GET"])
def obtener_producto(id):
    producto = next((p for p in productos if p["id"] == id), None)
    if producto:
        return jsonify(producto)
    return jsonify({"error": "Producto no encontrado"}), 404

# Ruta para agregar un producto (POST)
@app.route("/api/productos", methods=["POST"])
def agregar_producto():
    nuevo_producto = request.get_json()
    nuevo_producto["id"] = len(productos) + 1
    productos.append(nuevo_producto)
    return jsonify(nuevo_producto), 201

# Ruta para actualizar un producto (PUT)
@app.route("/api/productos/<int:id>", methods=["PUT"])
def actualizar_producto(id):
    producto = next((p for p in productos if p["id"] == id), None)
    if producto:
        datos = request.get_json()
        producto.update(datos)
        return jsonify(producto)
    return jsonify({"error": "Producto no encontrado"}), 404

# Ruta para eliminar un producto (DELETE)
@app.route("/api/productos/<int:id>", methods=["DELETE"])
def eliminar_producto(id):
    global productos
    productos = [p for p in productos if p["id"] != id]
    return jsonify({"mensaje": "Producto eliminado"}), 200

if __name__ == "__main__":
    app.run(debug=True)

