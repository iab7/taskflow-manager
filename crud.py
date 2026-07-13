from models import Tarefa
from storage import carregar_tarefas, salvar_tarefas


def criar_tarefa(titulo, descricao, prioridade):
    tarefas = carregar_tarefas()

    novo_id = 1
    if tarefas:
        novo_id = max(t["id"] for t in tarefas) + 1

    tarefa = Tarefa(
        id=novo_id, titulo=titulo, descricao=descricao, prioridade=prioridade
    )

    tarefas.append(tarefa.to_dict())
    salvar_tarefas(tarefas)

    print("\n✅ Tarefa criada com sucesso!")


def listar_tarefas():
    tarefas = carregar_tarefas()

    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    print("\n========== TAREFAS ==========\n")

    for tarefa in tarefas:
        print(f"ID: {tarefa['id']}")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Status: {tarefa['status']}")
        print("-" * 30)


def editar_tarefa(id_tarefa, titulo, descricao, prioridade):
    tarefas = carregar_tarefas()

    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa["titulo"] = titulo
            tarefa["descricao"] = descricao
            tarefa["prioridade"] = prioridade

            salvar_tarefas(tarefas)

            print("\n✅ Tarefa atualizada!")
            return

    print("\n❌ Tarefa não encontrada.")


def excluir_tarefa(id_tarefa):
    tarefas = carregar_tarefas()

    novas = [t for t in tarefas if t["id"] != id_tarefa]

    salvar_tarefas(novas)

    print("\n🗑️ Tarefa excluída.")


def concluir_tarefa(id_tarefa):
    tarefas = carregar_tarefas()

    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa["status"] = "Concluída"

            salvar_tarefas(tarefas)

            print("\n✅ Tarefa concluída!")
            return

    print("\n❌ Tarefa não encontrada.")


def buscar_tarefa(texto):
    tarefas = carregar_tarefas()

    resultado = [t for t in tarefas if texto.lower() in t["titulo"].lower()]

    if not resultado:
        print("\nNenhuma tarefa encontrada.")
        return

    print("\n======= RESULTADO =======\n")

    for tarefa in resultado:
        print(f"{tarefa['id']} - {tarefa['titulo']} ({tarefa['status']})")
