from flask import Flask, jsonify, request

app = Flask(__name__)

cursos = [
    {
        "id": 60,
        "nome": "Tads",
        "instituicao": "ifpr",
        "duracao": "3 anos"
    },
    {
        "id": 50,
        "nome": "Meio-Ambiente",
        "instituicao": "ifpr",
        "duracao": "3 anos"
    },
    {
            "id": 70,
            "nome": "Informatica",
            "instituicao": "ifpr",
            "duracao": "3 anos"
    }
]


@app.route("/curso1", methods=["GET"])
def listar_cursos():
    return jsonify(cursos)


@app.route("/cursos/<int:id>", methods=["GET"])
def buscar_cursos(id):
    for curso in cursos:
        if curso["id"] == id:
            return jsonify(cursos)

    return jsonify({"erro": "Curso não encontrado"}), 404

 
@app.route("/cursos", methods=["GET"])
def pesquisar_cursos():
    instituicao = request.args.get("instituicao")
    cursos_r = []
    print(instituicao)
    if instituicao:
        for curso in cursos:
            if  instituicao.lower() in curso["instituicao"].lower():
               cursos_r.append(curso)

        return jsonify(cursos_r)

    return jsonify(cursos)

app.run(debug=True)
