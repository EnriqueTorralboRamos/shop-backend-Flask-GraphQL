# 🛒 Shop Backend - Flask + GraphQL API

Este proyecto es una API de ejemplo desarrollada con **Flask** y **GraphQL** para gestionar productos de una tienda.

[***Enlace a Preguntas***](./Respuestas.md)

[***Enlace a Frontend Vue***](https://github.com/EnriqueTorralboRamos/Shop-Vue.git)

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clona este repositorio.

```bash
git clone https://github.com/EnriqueTorralboRamos/shop-backend-Flask-GraphQL.git
cd shop-backend-Flask-GraphQL
```

2. Crea un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias necesarias:

```bash
pip install Flask ariadne
```

## 🚀 Cómo ejecutar la API

1. Activa el enrotno virtual creado con `python -m venv venv`:

``` bash
.\venv\Scripts\activate
```
--> Nota: a veces es necesairo ejecutar la siguiente linea para ejecutar scripts bloqueados en powershell, si el anterior comando fallo prueba a ejecutar esto y re intentar

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

2. Ejecutar el Servidor


```bash
python app.py
```

3. Accede a la interfaz de prueba GraphQL en tu navegador:

```bash
http://localhost:5000/graphql
```

Desde ahí puedes lanzar queries y mutations definidas en `schema.graphql`.

## 🚀 Cómo ejecutar el test
Dependiendo de como quieras hacerlo, si usas visual studio al colocarte en el archivo te permite ejecutarlo o por consola de la misma manera que el proyecto

**Tienes que tener lanzado el back**

1. Activa el enrotno virtual creado con `python -m venv venv`:

``` bash
.\venv\Scripts\activate
```
--> Nota: a veces es necesairo ejecutar la siguiente linea para ejecutar scripts bloqueados en powershell, si el anterior comando fallo prueba a ejecutar esto y re intentar

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

2. Ejecutar el test


```bash
python test.py
```

Si todo es correcto te mostrara algo asi:

``` bash
....
----------------------------------------------------------------------
Ran 4 tests in 10.246s

OK
```

## 🧪 Ejemplos de uso

### Obtener todos los productos

```graphql
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

### Obtener un producto por ID

```graphql
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

### Actualizar stock de un producto

```graphql
mutation {
  actualizarStock(id: "1", cantidad: -30) {
    id
    name
    stock
    available
  }
}
```

## 📂 Estructura del proyecto

```
.
├── app.py              # Punto de entrada de la aplicación Flask
├── schema.graphql      # Definición del esquema GraphQL
├── resolvers.py        # Resolvers para queries y mutations
├── data.py             # Datos estáticos o fuente de datos
├── README.md
```

## 🛠️ Notas adicionales

- Puedes modificar `data.py` para cambiar los productos cargados en memoria.
- El endpoint `/graphql` ofrece una interfaz interactiva si estás en desarrollo.
- Este es un trabajo hecho para la asignatura de Programacion Web 2, en el que se hace el backend de la practica anterior donde se hizo la web con vue


