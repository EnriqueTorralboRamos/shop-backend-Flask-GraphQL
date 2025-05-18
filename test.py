import unittest
import requests

BASE_URL = "http://localhost:5000/graphql"

class TestShopAPI(unittest.TestCase):

    # Test que obtiene todos los productos y comprueba que la respuesta sea correcta 
    def test_get_all_products(self):
        query = '''
        query {
            productos {
                id
                name
                price
            }
        }
        '''
        response = requests.post(BASE_URL, json={'query': query})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("data", data)
        self.assertIn("productos", data["data"])
        self.assertIsInstance(data["data"]["productos"], list)
        self.assertGreater(len(data["data"]["productos"]), 0)

    # Test que obtiene un producto por su ID y comprueba que la respuesta sea correcta
    def test_get_product_by_id(self):
        query = '''
        query {
            producto(id: "1") {
                name
                price
            }
        }
        '''
        response = requests.post(BASE_URL, json={'query': query})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("producto", data["data"])
        self.assertIsNotNone(data["data"]["producto"])
        self.assertEqual(data["data"]["producto"]["name"], "Camisa")
        self.assertIsInstance(data["data"]["producto"]["price"], (int, float))

    # Test que actualiza el stock de un producto y comprueba que la respuesta sea correcta
    def test_update_stock(self):
        # 1. Obtiene el stock actual
        query = '''
        query {
            producto(id: "1") {
                stock
            }
        }
        '''
        original_response = requests.post(BASE_URL, json={'query': query})
        original_stock = original_response.json()["data"]["producto"]["stock"]

        # 2. Actualiza el stock
        mutation = '''
        mutation {
            actualizarStock(id: "1", cantidad: 2) {
                id
                stock
            }
        }
        '''
        update_response = requests.post(BASE_URL, json={'query': mutation})
        self.assertEqual(update_response.status_code, 200)
        update_data = update_response.json()
        self.assertIn("actualizarStock", update_data["data"])
        self.assertEqual(update_data["data"]["actualizarStock"]["id"], "1")
        self.assertEqual(update_data["data"]["actualizarStock"]["stock"], original_stock + 2)

    # Test que intenta obtener el stock de un producto no existente y comprueba que la respuesta none
    def test_get_invalid_product(self):
        query = '''
        query {
            producto(id: "999") {
                name
            }
        }
        '''
        response = requests.post(BASE_URL, json={'query': query})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsNone(data["data"]["producto"])

if __name__ == "__main__":
    unittest.main()