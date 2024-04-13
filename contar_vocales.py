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
        if letra.lower() in vocales:
            if letra.lower() not in resultado:
                resultado[letra.lower()] = 0
            resultado[letra.lower()] += 1
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
    
    def test_contar_CaSaNoVa(self):
        resultado = contar_vocales('CaSaNoVa')
        self.assertEqual(resultado, {'a': 3, 'o': 1})
    
    def test_contar_CaSaNoVa(self):
        resultado = contar_vocales('CaSaNoVa')
        self.assertEqual(resultado, {'a': 3, 'o': 1})
    
    def test_contar_INGENIERO(self):
        resultado = contar_vocales('INGENIERO')
        self.assertEqual(resultado, {'i': 2, 'o': 1, 'e' : 2})
 
    def test_contar_sin_vocales(self):
        resultado = contar_vocales('rpp')
        self.assertEqual(resultado, {})

    def test_contar_cOmPUtadORA(self):
        resultado = contar_vocales('cOmPUtadORA')
        self.assertEqual(resultado, {'o': 2, 'u': 1, 'a' : 2})

    def test_con_espacios(self):
        resultado = contar_vocales('Rocio Portal')
        self.assertEqual(resultado, {'a': 1, 'o': 3, 'i': 1})

unittest.main()

# while(True):
#     palabra = input('Ingrese palabra: ')
#     print(contar_vocales(palabra))