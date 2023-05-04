from codigo.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        entrada = "13/03/2000"
        output = 23

        funcionario_teste = Funcionario('Teste', entrada, 1500)
        resultado = funcionario_teste.idade()

        assert resultado == output

    def test_quando_sobrenome_recebe_Wellington_Oliveira_deve_retornar_Oliveira(self):
        entrada = "Wellington Carvalho "
        output = "Carvalho"

        funcionario_teste = Funcionario(entrada, "11/03/1999", 1500)
        resultado = funcionario_teste.sobrenome()

        assert resultado == output
