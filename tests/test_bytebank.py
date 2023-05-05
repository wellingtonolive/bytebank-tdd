from codigo.bytebank import Funcionario
import pytest
from pytest import mark


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

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        salario_atual = 100000
        entrada_nome = "Paulo Braganca"
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, "11/03/1999", salario_atual)

        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        salario_atual = 1000
        entrada_nome = "Paulo Braganca"
        esperado = 100

        funcionario_teste = Funcionario(entrada_nome, "11/03/1999", salario_atual)

        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            salario_atual = 1000000
            entrada_nome = "Paulo Braganca"

            funcionario_teste = Funcionario(entrada_nome, "11/03/1999", salario_atual)

            resultado = funcionario_teste.calcular_bonus()

            assert resultado

    def test_retorno_str(self):
        nome, data_nas, salario = "Well", "11/03/1999", 1500
        esperado = 'Funcionario(Well, 11/03/1999, 1500)'

        funcionario_teste = Funcionario(nome, data_nas, salario)

        resultado = funcionario_teste.__str__()

        assert resultado == esperado
