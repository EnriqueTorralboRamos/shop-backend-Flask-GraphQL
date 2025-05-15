from ariadne import QueryType, MutationType
from data import products

query = QueryType()
mutation = MutationType()

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
