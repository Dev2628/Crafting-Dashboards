"""
    Se creo este archivo para generar mi propio excel con el que probar el framework dash
"""

import uuid
import random
import pandas as pd
from faker import Faker

fake = Faker()


def generate_customer_data():
    cliente_id = str(uuid.uuid4())
    nombre = fake.name()
    email = fake.email()
    pais = fake.country()
    direccion = fake.address()
    sueldo = round(random.uniform(20000, 80000), 2)
    carrera = fake.job()
    fecha_ingreso = fake.date_this_decade()

    return [cliente_id, nombre, email, pais, direccion, sueldo, carrera, fecha_ingreso]


def generate_customers(number_of_clients):
    customers_data = [generate_customer_data()
                      for _ in range(number_of_clients)]
    return customers_data


def save_to_excel(data, file_name):
    df = pd.DataFrame(data, columns=[
                      'ID', 'Nombre', 'Email', 'Pais', 'Direccion', 'Sueldo', 'Carrera', 'Fecha de Ingreso'],)
    df.to_excel(file_name, index=False)


if __name__ == "__main__":
    NUMBER_OF_CLIENTS = 50
    customer_data = generate_customers(NUMBER_OF_CLIENTS)
    save_to_excel(customer_data, 'clients.xlsx')
