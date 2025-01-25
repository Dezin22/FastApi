from fastapi import FastAPI


app = FastAPI(title="API Sorteio", description="Api para gerenciar sorteios.")

participants = []


@app.get("/info")
def info():
    return {"title": app.title, "description": app.description}


@app.get("/sorteio/participantes")
def get_all_participants(search: str | None = None):
    results = []

    if search is not None:
        for name in participants:
            if search.lower() in name.lower():
                results.append(name)
    else:
        results.extend(participants)

    return results


@app.post("/sorteio/{name}/adicionar")
def add_new_participant(name: str):
    participants.append(name)
    return {"mensage": "Participante adicionado com sucesso."}


