import unittest
#opcion larga:
# def contar_vocales(mi_string):
#     resultado = {}
#     for letra in mi_string:
#         if letra == 'a':
#             if 'a' not in resultado:
#                 resultado['a'] = 0
#             resultado['a'] = resultado['a'] + 1
#         if letra == 'e':
#             if 'e' not in resultado:
#                 resultado['e'] = 0
#             resultado['e'] = resultado['e'] + 1
#     return resultado

def contar_vocales(mi_string):
    vocales = ('a', 'e', 'i', 'o', 'u')
    resultado = {}
    for letra in mi_string:
        # if letra in 'aeiou':
        if letra in vocales:
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] += 1
    return resultado


class TestContarVocales(unittest.TestCase):
    def test_nada(self):
        resultado = contar_vocales('zzz')
        self.assertEqual(resultado, {})

    def test_contar_a(self):
        resultado = contar_vocales('cas')
        self.assertEqual(resultado, {'a': 1})

    def test_contar_aa(self):
        resultado = contar_vocales('casa')
        self.assertEqual(resultado, {'a': 2})

    def test_contar_bese(self):
        resultado = contar_vocales('bese')
        self.assertEqual(resultado, {'e': 2})

    def test_contar_besa(self):
        resultado = contar_vocales('besa')
        self.assertEqual(resultado, {'a': 1, 'e': 1})

    def test_contar_casanova(self):
        resultado = contar_vocales('casanova')
        self.assertEqual(resultado, {'a': 3, 'o': 1})


unittest.main()

# while(True):
#     palabra = input('Ingrese palabra: ')
#     print(contar_vocales(palabra))