from crud import criar_tarefa
from storage import carregar_tarefas


def test_criar_tarefa():
    criar_tarefa(
        "Teste CRUD",
        "Descrição teste",
        "Alta"
    )

    tarefas = carregar_tarefas()

    assert len(tarefas) > 0
    assert tarefas[-1]["titulo"] == "Teste CRUD"