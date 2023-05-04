from codigo.bytebank import Funcionario


# wellington = Funcionario('Wellington', '11/03/1999', 1500)

# print(wellington.idade())


def test_idade():
    func_test = Funcionario('Teste', '11/03/1999', 1500)
    print(f'Teste = {func_test.idade()}')

test_idade()