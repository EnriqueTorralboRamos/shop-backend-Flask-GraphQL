# Preguntas respondidas
## ¿Qué ventajas ofrece GraphQL sobre REST en este contexto?
- GraphQL permite realizar consultas precisas, solicitando solo los campos necesarios. Esto evita la sobrecarga de datos que se produce habitualmente en REST, donde una ruta devuelve siempre el mismo conjunto fijo de campos. 
- Toda la comunicación se puede realizar a través de un único endpoint, lo que simplifica la arquitectura y reduce el número de peticiones HTTP necesarias para obtener datos diversos.
 

## ¿Cómo se definen los tipos y resolvers en una API con GraphQL?
Primero se definen los tipos en Graphql.

En este proyecto podemos ver que primero se define el tipo de archivo:
```graphql
type Product {
  id: String!
  name: String!
  price: Float!
  stock: Int!
  available: Boolean!
  descripction: String
  image: String
}
```
Y despues los tipos de query y de mutations
```graphql
type Query {
  productos: [Product!]!
  producto(id: String!): Product
}

type Mutation {
  actualizarStock(id: String!, cantidad: Int!): Product
}
```

Luego se implementa la logica de cada campo u operacion en ``resolvers.py``

```python
@query.field("productos")
def resolve_productos(_, info):
    return products

@query.field("producto")
def resolve_producto(_, info, id):
    return next((p for p in products if p["id"] == id), None)


@mutation.field("actualizarStock")
def resolve_actualizar_stock(_, info, id, cantidad):
    for prod in products:
        if prod["id"] == id:
            prod["stock"] += cantidad
            prod["stock"] = max(prod["stock"], 0)
            prod["available"] = prod["stock"] > 0
            return prod
    return None

resolvers = [query, mutation]
```


## ¿Por qué es importante que el backend también actualice disponible y no depender solo del frontend?
Porque en el frontend el usuario podria llegar a modificarlo y permitir hacer pedidos de objetos que esten agotados ya que se salta lo logica, en cambio en el back aunque se tocara el front no permitiria eso, ya que nadie mas tendria acceso a esos datos para modifcarlos, solo el back.
Otra cosa a resaltar seria qye este back seria reutilizable para otras aplicaciones web, movil...

## ¿Cómo garantizas que la lógica de actualización de stock y disponibilidad sea coherente?
A la hora de actualizar un producto se vuelve a calcular si el stock es mayor o no de 0 y en base a eso se cambia o no la disponibilidad.
```python
@mutation.field("actualizarStock")
def resolve_actualizar_stock(_, info, id, cantidad):
    for prod in products:
        if prod["id"] == id:
            prod["stock"] += cantidad
            prod["stock"] = max(prod["stock"], 0)
            prod["available"] = prod["stock"] > 0
            return prod
    return None

```