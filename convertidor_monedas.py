>>> #Convertidor de monedas
... cantidad = float(input("Cantidad en MXN: "))
... print("Monedas: 1.USD 2.EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS")
... opcion = int(input("Elige opción: "))
... match opcion:
...     case 1:
...         resultado = cantidad / 16.5
...         moneda = "USD"
...     case 2:
...         resultado = cantidad / 18.0
...         moneda = "EUR"
...     case 3:
...         resultado = cantidad / 0.45
...         moneda = "THB"
...     case 4:
...         resultado = cantidad / 0.12
...         moneda = "JPY"
...     case 5:
...         resultado = cantidad / 0.013
...         moneda = "KRW"
...     case 6:
...         resultado = cantidad / 11.5
...         moneda = "AUD"
...     case 7:
...         resultado = cantidad / 2.8
...         moneda = "PEN"
...     case 8:
...         resultado = cantidad / 8.2
...         moneda = "CAD"
...     case 9:
...         resultado = cantidad / 0.0023
...         moneda = "VES"
...     case 10:
...         resultado = cantidad / 0.046
...         moneda = "ARS"
...     case _:
...         print("Opción no válida")
...         resultado = None
...
... if resultado is not None:
...     print(f"{cantidad} MXN son {resultado:.2f} {moneda}")
...
Cantidad en MXN: 55
Monedas: 1.USD 2.EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS
Elige opción: 1
55.0 MXN son 3.33 USD
>>>
>>> #Convertidor de monedas
... cantidad = float(input("Cantidad en MXN: "))
... print("Monedas: 1.USD 2.EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS")
... opcion = int(input("Elige opción: "))
... match opcion:
...     case 1:
...         resultado = cantidad / 16.5
...         moneda = "USD"
...     case 2:
...         resultado = cantidad / 18.0
...         moneda = "EUR"
...     case 3:
...         resultado = cantidad / 0.45
...         moneda = "THB"
...     case 4:
...         resultado = cantidad / 0.12
...         moneda = "JPY"
...     case 5:
...         resultado = cantidad / 0.013
...         moneda = "KRW"
...     case 6:
...         resultado = cantidad / 11.5
...         moneda = "AUD"
...     case 7:
...         resultado = cantidad / 2.8
...         moneda = "PEN"
...     case 8:
...         resultado = cantidad / 8.2
...         moneda = "CAD"
...     case 9:
...         resultado = cantidad / 0.0023
...         moneda = "VES"
...     case 10:
...         resultado = cantidad / 0.046
...         moneda = "ARS"
...     case _:
...         print("Opción no válida")
...         resultado = None
...
... if resultado is not None:
...     print(f"{cantidad} MXN son {resultado:.2f} {moneda}")
...
Cantidad en MXN: 55
Monedas: 1.USD 2.EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS
Elige opción: 2
55.0 MXN son 3.06 EUR
>>>
>>> #Convertidor de monedas
... cantidad = float(input("Cantidad en MXN: "))
... print("Monedas: 1.USD 2.EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS")
... opcion = int(input("Elige opción: "))
... match opcion:
...     case 1:
...         resultado = cantidad / 16.5
...         moneda = "USD"
...     case 2:
...         resultado = cantidad / 18.0
...         moneda = "EUR"
...     case 3:
...         resultado = cantidad / 0.45
...         moneda = "THB"
...     case 4:
...         resultado = cantidad / 0.12
...         moneda = "JPY"
...     case 5:
...         resultado = cantidad / 0.013
...         moneda = "KRW"
...     case 6:
...         resultado = cantidad / 11.5
...         moneda = "AUD"
...     case 7:
...         resultado = cantidad / 2.8
...         moneda = "PEN"
...     case 8:
...         resultado = cantidad / 8.2
...         moneda = "CAD"
...     case 9:
...         resultado = cantidad / 0.0023
...         moneda = "VES"
...     case 10:
...         resultado = cantidad / 0.046
...         moneda = "ARS"
...     case _:
...         print("Opción no válida")
...         resultado = None
...
... if resultado is not None:
...     print(f"{cantidad} MXN son {resultado:.2f} {moneda}")
...
Cantidad en MXN: 55
Monedas: 1.USD 2.EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS
Elige opción: 3
55.0 MXN son 122.22 THB
>>>
>>> #Convertidor de monedas
... cantidad = float(input("Cantidad en MXN: "))
... print("Monedas: 1.USD 2.EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS")
... opcion = int(input("Elige opción: "))
... match opcion:
...     case 1:
...         resultado = cantidad / 16.5
...         moneda = "USD"
...     case 2:
...         resultado = cantidad / 18.0
...         moneda = "EUR"
...     case 3:
...         resultado = cantidad / 0.45
...         moneda = "THB"
...     case 4:
...         resultado = cantidad / 0.12
...         moneda = "JPY"
...     case 5:
...         resultado = cantidad / 0.013
...         moneda = "KRW"
...     case 6:
...         resultado = cantidad / 11.5
...         moneda = "AUD"
...     case 7:
...         resultado = cantidad / 2.8
...         moneda = "PEN"
...     case 8:
...         resultado = cantidad / 8.2
...         moneda = "CAD"
...     case 9:
...         resultado = cantidad / 0.0023
...         moneda = "VES"
...     case 10:
...         resultado = cantidad / 0.046
...         moneda = "ARS"
...     case _:
...         print("Opción no válida")
...         resultado = None
...
... if resultado is not None:
...     print(f"{cantidad} MXN son {resultado:.2f} {moneda}")
...
Cantidad en MXN: 55
Monedas: 1.USD 2.EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS
Elige opción: 4
55.0 MXN son 458.33 JPY
>>>
>>> #Convertidor de monedas
... cantidad = float(input("Cantidad en MXN: "))
... print("Monedas: 1.USD 2.EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS")
... opcion = int(input("Elige opción: "))
... match opcion:
...     case 1:
...         resultado = cantidad / 16.5
...         moneda = "USD"
...     case 2:
...         resultado = cantidad / 18.0
...         moneda = "EUR"
...     case 3:
...         resultado = cantidad / 0.45
...         moneda = "THB"
...     case 4:
...         resultado = cantidad / 0.12
...         moneda = "JPY"
...     case 5:
...         resultado = cantidad / 0.013
...         moneda = "KRW"
...     case 6:
...         resultado = cantidad / 11.5
...         moneda = "AUD"
...     case 7:
...         resultado = cantidad / 2.8
...         moneda = "PEN"
...     case 8:
...         resultado = cantidad / 8.2
...         moneda = "CAD"
...     case 9:
...         resultado = cantidad / 0.0023
...         moneda = "VES"
...     case 10:
...         resultado = cantidad / 0.046
...         moneda = "ARS"
...     case _:
...         print("Opción no válida")
...         resultado = None
...
... if resultado is not None:
...     print(f"{cantidad} MXN son {resultado:.2f} {moneda}")
...
Cantidad en MXN: 55
Monedas: 1.USD 2.EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS
Elige opción: 5
55.0 MXN son 4230.77 KRW
>>>
>>> #Convertidor de monedas
... cantidad = float(input("Cantidad en MXN: "))
... print("Monedas: 1.USD 2.EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS")
... opcion = int(input("Elige opción: "))
... match opcion:
...     case 1:
...         resultado = cantidad / 16.5
...         moneda = "USD"
...     case 2:
...         resultado = cantidad / 18.0
...         moneda = "EUR"
...     case 3:
...         resultado = cantidad / 0.45
...         moneda = "THB"
...     case 4:
...         resultado = cantidad / 0.12
...         moneda = "JPY"
...     case 5:
...         resultado = cantidad / 0.013
...         moneda = "KRW"
...     case 6:
...         resultado = cantidad / 11.5
...         moneda = "AUD"
...     case 7:
...         resultado = cantidad / 2.8
...         moneda = "PEN"
...     case 8:
...         resultado = cantidad / 8.2
...         moneda = "CAD"
...     case 9:
...         resultado = cantidad / 0.0023
...         moneda = "VES"
...     case 10:
...         resultado = cantidad / 0.046
...         moneda = "ARS"
...     case _:
...         print("Opción no válida")
...         resultado = None
...
... if resultado is not None:
...     print(f"{cantidad} MXN son {resultado:.2f} {moneda}")
...
Cantidad en MXN: 55
Monedas: 1.USD 2.EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS
Elige opción: 6
55.0 MXN son 4.78 AUD
>>>
>>> #Convertidor de monedas
... cantidad = float(input("Cantidad en MXN: "))
... print("Monedas: 1.USD 2.EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS")
... opcion = int(input("Elige opción: "))
... match opcion:
...     case 1:
...         resultado = cantidad / 16.5
...         moneda = "USD"
...     case 2:
...         resultado = cantidad / 18.0
...         moneda = "EUR"
...     case 3:
...         resultado = cantidad / 0.45
...         moneda = "THB"
...     case 4:
...         resultado = cantidad / 0.12
...         moneda = "JPY"
...     case 5:
...         resultado = cantidad / 0.013
...         moneda = "KRW"
...     case 6:
...         resultado = cantidad / 11.5
...         moneda = "AUD"
...     case 7:
...         resultado = cantidad / 2.8
...         moneda = "PEN"
...     case 8:
...         resultado = cantidad / 8.2
...         moneda = "CAD"
...     case 9:
...         resultado = cantidad / 0.0023
...         moneda = "VES"
...     case 10:
...         resultado = cantidad / 0.046
...         moneda = "ARS"
...     case _:
...         print("Opción no válida")
...         resultado = None
...
... if resultado is not None:
...     print(f"{cantidad} MXN son {resultado:.2f} {moneda}")
...
Cantidad en MXN: 55
Monedas: 1.USD 2.EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS
Elige opción: 7
55.0 MXN son 19.64 PEN
>>>
>>> #Convertidor de monedas
... cantidad = float(input("Cantidad en MXN: "))
... print("Monedas: 1.USD 2.EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS")
... opcion = int(input("Elige opción: "))
... match opcion:
...     case 1:
...         resultado = cantidad / 16.5
...         moneda = "USD"
...     case 2:
...         resultado = cantidad / 18.0
...         moneda = "EUR"
...     case 3:
...         resultado = cantidad / 0.45
...         moneda = "THB"
...     case 4:
...         resultado = cantidad / 0.12
...         moneda = "JPY"
...     case 5:
...         resultado = cantidad / 0.013
...         moneda = "KRW"
...     case 6:
...         resultado = cantidad / 11.5
...         moneda = "AUD"
...     case 7:
...         resultado = cantidad / 2.8
...         moneda = "PEN"
...     case 8:
...         resultado = cantidad / 8.2
...         moneda = "CAD"
...     case 9:
...         resultado = cantidad / 0.0023
...         moneda = "VES"
...     case 10:
...         resultado = cantidad / 0.046
...         moneda = "ARS"
...     case _:
...         print("Opción no válida")
...         resultado = None
...
... if resultado is not None:
...     print(f"{cantidad} MXN son {resultado:.2f} {moneda}")
...
Cantidad en MXN: 55
Monedas: 1.USD 2.EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS
Elige opción: 8
55.0 MXN son 6.71 CAD
>>>
>>> #Convertidor de monedas
... cantidad = float(input("Cantidad en MXN: "))
... print("Monedas: 1.USD 2.EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS")
... opcion = int(input("Elige opción: "))
... match opcion:
...     case 1:
...         resultado = cantidad / 16.5
...         moneda = "USD"
...     case 2:
...         resultado = cantidad / 18.0
...         moneda = "EUR"
...     case 3:
...         resultado = cantidad / 0.45
...         moneda = "THB"
...     case 4:
...         resultado = cantidad / 0.12
...         moneda = "JPY"
...     case 5:
...         resultado = cantidad / 0.013
...         moneda = "KRW"
...     case 6:
...         resultado = cantidad / 11.5
...         moneda = "AUD"
...     case 7:
...         resultado = cantidad / 2.8
...         moneda = "PEN"
...     case 8:
...         resultado = cantidad / 8.2
...         moneda = "CAD"
...     case 9:
...         resultado = cantidad / 0.0023
...         moneda = "VES"
...     case 10:
...         resultado = cantidad / 0.046
...         moneda = "ARS"
...     case _:
...         print("Opción no válida")
...         resultado = None
...
... if resultado is not None:
...     print(f"{cantidad} MXN son {resultado:.2f} {moneda}")
...
Cantidad en MXN: 55
Monedas: 1.USD 2.EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS
Elige opción: 9
55.0 MXN son 23913.04 VES
>>>
>>> #Convertidor de monedas
... cantidad = float(input("Cantidad en MXN: "))
... print("Monedas: 1.USD 2.EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS")
... opcion = int(input("Elige opción: "))
... match opcion:
...     case 1:
...         resultado = cantidad / 16.5
...         moneda = "USD"
...     case 2:
...         resultado = cantidad / 18.0
...         moneda = "EUR"
...     case 3:
...         resultado = cantidad / 0.45
...         moneda = "THB"
...     case 4:
...         resultado = cantidad / 0.12
...         moneda = "JPY"
...     case 5:
...         resultado = cantidad / 0.013
...         moneda = "KRW"
...     case 6:
...         resultado = cantidad / 11.5
...         moneda = "AUD"
...     case 7:
...         resultado = cantidad / 2.8
...         moneda = "PEN"
...     case 8:
...         resultado = cantidad / 8.2
...         moneda = "CAD"
...     case 9:
...         resultado = cantidad / 0.0023
...         moneda = "VES"
...     case 10:
...         resultado = cantidad / 0.046
...         moneda = "ARS"
...     case _:
...         print("Opción no válida")
...         resultado = None
...
... if resultado is not None:
...     print(f"{cantidad} MXN son {resultado:.2f} {moneda}")
...
Cantidad en MXN: 55
Monedas: 1.USD 2.EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS
Elige opción: 10
55.0 MXN son 1195.65 ARS
>>>
