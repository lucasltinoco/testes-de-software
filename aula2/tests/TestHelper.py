from agencia import Agencia


class TestHelper:
    def make_n_contas(self, n: int, agencia: Agencia):
        contas = []
        for i in range(n):
            conta = agencia.criar_conta(f"TitularTeste{i}")
            contas.append(conta)
        return contas
