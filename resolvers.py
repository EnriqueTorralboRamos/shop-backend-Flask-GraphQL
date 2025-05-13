from ariadne import QueryType, MutationType
from data import products

query = QueryType()
mutation = MutationType()

@query.field("productos")
def resolve_productos(_, info):
    return products

@mutation.field("actualizarStock")
def resolve_actualizar_stock(_, info, id, cantidad):
    for prod in products:
        if prod["id"] == id:
            prod["stock"] += cantidad
            prod["stock"] = max(prod["stock"], 0)
            prod["disponible"] = prod["stock"] > 0
            return prod
    return None

resolvers = [query, mutation]
