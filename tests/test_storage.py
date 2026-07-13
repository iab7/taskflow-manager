import os
from storage import salvar_tarefas, carregar_tarefas


def test_salvar_e_carregar():
    tarefas = [
        {
            "id": 1,
            "titulo": "Teste",
            "descricao": "Descrição",
            "prioridade": "Alta",
            "status": "Pendente",
        }
    ]

    salvar_tarefas(tarefas)

    resultado = carregar_tarefas()

    assert resultado == tarefas
