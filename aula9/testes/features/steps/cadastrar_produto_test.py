from behave import *
from mercado_leilao import MercadoLeilao

@given('o cadastro do usuario Ernani Cesar foi realizado')
def step_impl(context):
    context.mercado = MercadoLeilao()

    context.mercado.cadastra_usuario(
        "Ernani Cesar",
        "UFSC",
        "ernani@posgrad.ufsc.br",
        "055.761.919-00"
    )

@given('o nome do produto {nome_produto}')
def step_impl(context, nome_produto):
    context.nome_produto = nome_produto

@given('a descricao do produto {descricao_produto}')
def step_impl(context, descricao_produto):
    context.descricao_produto = descricao_produto

@given('e o lance {valor_lance}')
def step_impl(context, valor_lance):
    context.valor_lance = float(valor_lance)

@given('e o cpf do leiloador {cpf}')
def step_impl(context, cpf):
    context.cpf_leiloador = cpf

@given('sofa amarelo ja foi cadastrado')
def step_impl(context):
    context.mercado.cadastra_produto(
        "sofa",
        "amarelo",
        100,
        "055.761.919-00",
        12345
    )

@when('cadastrar o produto')
def step_impl(context):
    try:
        context.mercado.cadastra_produto(
            context.nome_produto,
            context.descricao_produto,
            context.valor_lance,
            context.cpf_leiloador,
            12345
        )

        context.msg = "SUCESSO"

    except Exception as e:
        context.msg = str(e)

@then('o sistema cadastra com sucesso')
def step_impl(context):
    assert context.msg == "SUCESSO"

@then('o sistema mostra a mensagem O produto ja existe ou o leiloador nao esta cadastrado.')
def step_impl(context):
    assert context.msg == "O produto ja existe ou o leiloador nao esta cadastrado."