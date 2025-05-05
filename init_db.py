from app import create_app, db
from app.models.producto import Producto
import sys, os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

app = create_app()

with app.app_context():
    db.create_all()
    
    # Productos de ejemplo
    producto1 = Producto(nombre="Mouse Gamer", descripcion="Mouse con luces RGB", precio=120.0, stock=10)
    producto2 = Producto(nombre="Teclado Mecánico", descripcion="Teclado retroiluminado", precio=250.0, stock=5)
    producto3 = Producto(nombre="Monitor 24 pulgadas", descripcion="Full HD 1080p", precio=800.0, stock=2)


    # Guardar en la base de datos
    db.session.add_all([producto1, producto2, producto3])
    db.session.commit()

    print("✅ Tablas creadas correctamente.")
    print("✅ Productos de prueba insertados.")



