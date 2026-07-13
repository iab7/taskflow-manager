from menu import exibir_menu
from crud import (
    criar_tarefa,
    listar_tarefas,
    editar_tarefa,
    excluir_tarefa,
    concluir_tarefa,
    buscar_tarefa,
)
from dashboard import mostrar_dashboard


def main():
    while True:
        opcao = exibir_menu()

        if opcao == "1":
            print("\n=== Criar Tarefa ===")
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            prioridade = input("Prioridade (Alta/Média/Baixa): ")

            criar_tarefa(titulo, descricao, prioridade)

        elif opcao == "2":
            listar_tarefas()

        elif opcao == "3":
            print("\n=== Editar Tarefa ===")
            id_tarefa = int(input("ID da tarefa: "))
            titulo = input("Novo título: ")
            descricao = input("Nova descrição: ")
            prioridade = input("Nova prioridade: ")

            editar_tarefa(id_tarefa, titulo, descricao, prioridade)

        elif opcao == "4":
            print("\n=== Excluir Tarefa ===")
            id_tarefa = int(input("ID da tarefa: "))
            excluir_tarefa(id_tarefa)

        elif opcao == "5":
            print("\n=== Concluir Tarefa ===")
            id_tarefa = int(input("ID da tarefa: "))
            concluir_tarefa(id_tarefa)

        elif opcao == "6":
            texto = input("Pesquisar: ")
            buscar_tarefa(texto)

        elif opcao == "7":
            mostrar_dashboard()

        elif opcao == "0":
            print("\nAté logo!")
            break

        else:
            print("\nOpção inválida!")


if __name__ == "__main__":
    main()
