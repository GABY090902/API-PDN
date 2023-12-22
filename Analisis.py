import requests

url = "https://dummy.restapiexample.com/api/v1/employees"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    lista_de_empleados = data.get('data', [])
    if lista_de_empleados:
        numero_empleados = len(lista_de_empleados)
        promedio_salario = sum(float(empleados.get('employee_salary', 0)) for empleados in lista_de_empleados) / numero_empleados
        edad_empleados = sum(int(empleados.get('employee_age', 0)) for empleados in lista_de_empleados) / numero_empleados
        salario = [float(empleados.get('employee_salary', 0)) for empleados in lista_de_empleados]
        min_salario = min(salario)
        max_salario = max(salario)
        edades = [int(empleados.get('employee_age', 0)) for empleados in lista_de_empleados]
        min_edad = min(edades)
        max_edad = max(edades)


        print(f"Número de empleados: {numero_empleados}")
        print(f"Promedio de salario: {promedio_salario}")
        print(f"Promedio de edad: {edad_empleados}")
        print(f"Salario mínimo: {min_salario}")
        print(f"Salario máximo: {max_salario}")
        print(f"Edad mínima: {min_edad}")
        print(f"Edad máxima: {max_edad}")
    else:
        print("No hay datos de empleados en la respuesta del API.")
else:
    print(f"Error al realizar la solicitud. Código de estado: {response.status_code}")