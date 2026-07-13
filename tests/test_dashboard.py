from storage import carregar_tarefas


def test_dashboard():
    tarefas = carregar_tarefas()

    assert isinstance(tarefas, list)
