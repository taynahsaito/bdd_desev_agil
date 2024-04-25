from behave import given, when, then

@given('eu tenho dois números inteiros: {n1:d} e {n2:d}')
def step_given(contexto, n1, n2):
    contexto.n1 = n1
    contexto.n2 = n2

@when('eu realizo a média de dois números inteiros')
def step_when(contexto):    
    contexto.resultado =  (contexto.n1 + contexto.n2)/2

@then('o resultado deve ser {resultado:d}')
def step_then(contexto, resultado):
    assert contexto.resultado == resultado, f"resultado incorreto. esperado: {resultado}. obtido: {contexto.resultado}"