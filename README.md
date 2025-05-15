# shop-backend-Flask-GraphQL
Este es un trabajo hecho para la asignatura de Programacion Web 2, en el que se hace el backend de la practica anterior donde se hizo la web con vue

`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

`.\venv\Scripts\activate`

`python app.py`

```
query {
  productos {
    id
    name
    price
    stock
    descripction
    available
  }
}
```

```
mutation {
  actualizarStock(id: "1", cantidad: -30) {
    id
    name
    stock
    available
  }
}
```

```
query ObtenerProducto {
  producto(id: "1") {
    id
    name
    price
    stock
    available
    descripction
    image
  }
}
```