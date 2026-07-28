>>> # Programa para calcular salario neto
... salario_bruto = float(input("Salario bruto: "))
... porcentaje = float(input("% impuestos: "))
... deducciones = float(input("Deducciones: "))
... impuesto = salario_bruto * (porcentaje / 100)
... salario_neto = salario_bruto - impuesto - deducciones
... print("Salario neto:", salario_neto)
...
Salario bruto: 10000
% impuestos: 15
Deducciones: 500
Salario neto: 8000.0
