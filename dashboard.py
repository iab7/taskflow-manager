from storage import carregar_tarefas


def mostrar_dashboard():
    """Exibe estatísticas das tarefas."""

    tarefas = carregar_tarefas()

    total = len(tarefas)

    concluidas = sum(
        1 for tarefa in tarefas
        if tarefa["status"] == "Concluída"
    )

    pendentes = total - concluidas

    alta = sum(
        1 for tarefa in tarefas
        if tarefa["prioridade"] == "Alta"
    )

    media = sum(
        1 for tarefa in tarefas
        if tarefa["prioridade"] == "Média"
    )

    baixa = sum(
        1 for tarefa in tarefas
        if tarefa["prioridade"] == "Baixa"
    )

    if total > 0:
        porcentagem_concluidas = (concluidas / total) * 100
        porcentagem_pendentes = (pendentes / total) * 100
    else:
        porcentagem_concluidas = 0
        porcentagem_pendentes = 0

    print("\n=========== DASHBOARD ===========")

    print(f"\n📋 Total de tarefas: {total}")

    print(
        f"\n✅ Concluídas: {concluidas} ({porcentagem_concluidas:.0f}%)"
    )

    print(
        f"⏳ Pendentes : {pendentes} ({porcentagem_pendentes:.0f}%)"
    )

    print(f"\n🔥 Alta prioridade : {alta}")
    print(f"📌 Média prioridade: {media}")
    print(f"🟢 Baixa prioridade: {baixa}")

    print("\n===============================\n")