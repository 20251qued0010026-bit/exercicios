from flask import Flask, jsonify, request

app = Flask(__name__)

alunos = [
    {
        "id":5,
        "nome":"Maria B",
        "curso":"T.I",
        "idade":19
    },
    {
        "id":2,
        "nome":"jaanai",
        "curso":"culinaria",
        "idade":45
    },
    {
        "id":3,
        "nome":"gaysa",
        "curso":"aerocao",
        "idade":18
    }
]

@app.route("/alunos1", methods=["GET"])
def mostrar_alunos():
    return jsonify(alunos)


@app.route("/alunos/<int:id>", methods=["GET"])
def buscar_alunos(id):
    for aluno in alunos:
        if aluno["id"] == id:
            return jsonify(aluno)

    return jsonify({"erro": "Aluno não encontrado"}), 404

 
@app.route("/alunos", methods=["GET"])
def pesquisar_alunos():
    nome = request.args.get("nome")
    alunos_r = []
    print(nome)
    if nome:
        for aluno in alunos:
            if  nome.lower() in aluno["nome"].lower():
                alunos_r.append(aluno)

        return jsonify(alunos_r)



    return jsonify(alunos)


if __name__ == "__main__":
    app.run(debug=True)