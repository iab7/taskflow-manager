from storage import carregar_tarefas


def mostrar_dashboard():
    tarefas = carregar_tarefas()

    total = len(tarefas)

    pendentes = sum(1 for t in tarefas if t["status"] == "Pendente")
    concluidas = sum(1 for t in tarefas if t["status"] == "Concluída")

    alta = sum(1 for t in tarefas if t["prioridade"] == "Alta")
    media = sum(1 for t in tarefas if t["prioridade"] == "Média")
    baixa = sum(1 for t in tarefas if t["prioridade"] == "Baixa")

    print("\n" + "=" * 40)
    print("         DASHBOARD")
    print("=" * 40)
    print(f"📋 Total de tarefas : {total}")
    print(f"⏳ Pendentes        : {pendentes}")
    print(f"✅ Concluídas       : {concluidas}")
    print()
    print(f"🔴 Alta             : {alta}")
    print(f"🟡 Média            : {media}")
    print(f"🟢 Baixa            : {baixa}")
    print("=" * 40)