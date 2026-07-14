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
            try:
                id_tarefa = int(input("ID da tarefa: "))
            except ValueError:
            print("\n❌ Digite um número válido.")
            continue
            titulo = input("Novo título: ")
            descricao = input("Nova descrição: ")
            prioridade = input("Nova prioridade: ")

            editar_tarefa(id_tarefa, titulo, descricao, prioridade)

        elif opcao == "4":
            print("\n=== Excluir Tarefa ===")
            try:
                id_tarefa = int(input("ID da tarefa: "))
            except ValueError:
            print("\n❌ Digite um número válido.")
            continue
            excluir_tarefa(id_tarefa)

        elif opcao == "5":
            print("\n=== Concluir Tarefa ===")
            try:
                id_tarefa = int(input("ID da tarefa: "))
            except ValueError:
            print("\n❌ Digite um número válido.")
            continue
            concluir_tarefa(id_tarefa)

        elif opcao == "6":
            texto = input("Pesquisar: ").strip()
            if texto:
                buscar_tarefa(texto)
            else:
                print("\n❌ Informe um texto para pesquisar.")

        elif opcao == "7":
            mostrar_dashboard()

        elif opcao == "0":
            print("\nAté logo!")
            break

        else:
            print("\nOpção inválida!")


if __name__ == "__main__":
    main()
