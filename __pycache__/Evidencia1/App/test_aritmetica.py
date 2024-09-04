#pruebas unitarias - ojo!!! con test_dividir y el de promedio!!!!!

from aritmetica import sumar, restar, dividir, multiplicar, sumar_n, promedio_n

#sintaxis de assert >>> assert condición, "mensaje de error". Si la cond se cumple todo continua si no sale el mensaje de error
def test_sumar():
    assert sumar(1.5, 2.5) == 4.0, "AssertionError:Personalizar mensaje"
    assert sumar(-1.0, 1.0) == 0.0, "AssertionError:Personalizar mensaje"
    assert sumar(0.0, 0.0) == 0.0, "AssertionError:Personalizar mensaje"

def test_restar():
    assert restar(5.5, 2.5) == 3.0, "AssertionError:Personalizar mensaje"
    assert restar(2.0, 3.0) == -1.0, "AssertionError:Personalizar mensaje"
    assert restar(0.0, 0.0) == 0.0, "AssertionError:Personalizar mensaje"

def test_dividir():
    assert dividir(10.0, 2.0) == 5.0
    #assert dividir(0.0, 1.0) == 0.0
    #assert dividir(10.0, 0.0) == float('inf')
    
def test_multiplicar():
    assert multiplicar(3.0, 2.0) == 6.0
    assert multiplicar(-2.0, 3.0) == -6.0
    assert multiplicar(0.0, 5.0) == 0.0

def test_sumar_n():
    assert sumar_n(1.5, 2.5, 3.0) == 7.0
    assert sumar_n(-1.0, 1.0) == 0.0
    assert sumar_n() == 0.0

def test_promedio_n():
    assert promedio_n(1.0, 2.0, 3.0) == 2.0
    assert promedio_n(-1.0, 1.0) == 0.0, "AssertionError:Personalizar mensaje"
    assert promedio_n() == 0.0


if __name__ == "__main__":
    test_sumar()
    test_restar()
    test_dividir()
    test_multiplicar()
    test_sumar_n()
    test_promedio_n()
print("SE EJECUTO TODO OK")