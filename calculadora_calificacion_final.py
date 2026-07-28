>>> # Calculadora de nota final con validación de rango
... parcial = float(input("Nota parciales (0-100): "))
... proyecto = float(input("Nota proyecto (0-100): "))
... examen = float(input("Nota examen final (0-100): "))
...
... if (parcial < 0 or parcial > 100) or (proyecto < 0 or proyecto > 100) or (examen < 0 or examen > 100):
...     print("Error: las notas deben estar entre 0 y 100")
... else:
...     nota_final = (parcial * 0.4) + (proyecto * 0.3) + (examen * 0.3)
...     print("Nota final:", nota_final)
...
Nota parciales (0-100): 80
Nota proyecto (0-100): 90
Nota examen final (0-100): 85
Nota final: 84.5
>>>
>>> # Calculadora de nota final con validación de rango
... parcial = float(input("Nota parciales (0-100): "))
... proyecto = float(input("Nota proyecto (0-100): "))
... examen = float(input("Nota examen final (0-100): "))
...
... if (parcial < 0 or parcial > 100) or (proyecto < 0 or proyecto > 100) or (examen < 0 or examen > 100):
...     print("Error: las notas deben estar entre 0 y 100")
... else:
...     nota_final = (parcial * 0.4) + (proyecto * 0.3) + (examen * 0.3)
...     print("Nota final:", nota_final)
...
Nota parciales (0-100): 110
Nota proyecto (0-100): 50
Nota examen final (0-100): 60
Error: las notas deben estar entre 0 y 100
