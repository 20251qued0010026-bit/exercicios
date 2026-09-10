from flask import Flask, jsonify, request

app = Flask(__name__)

filmes = [
    {
        "id": 10,
        "nome": "Matrix",
        "diretor": "Lana e Lilly Wachowski",
        "ano": 1999
    },
    {
        "id": 20,
        "nome": "Interestelar",
        "diretor": "Christopher Nolan",
        "ano": 2014
    }
]


@app.route("/filmes1", methods=["GET"])
def listar_filmes():
    return jsonify(filmes)


@app.route("/filmes/<int:id>", methods=["GET"])
def buscar_filme(id):
    for filme in filmes:
        if filme["id"] == id:
            return jsonify(filme)

    return jsonify({"erro": "Filme não encontrado"}), 404

 
@app.route("/filmes", methods=["GET"])
def pesquisar_filme():
    nome = request.args.get("nome")
    filmes_r = []
    print(nome)
    if nome:
        for filme in filmes:
            if  nome.lower() in filme["nome"].lower():
                filmes_r.append(filme)

        return jsonify(filmes_r)


        return jsonify({"erro": "Filme não encontrado"}), 404

    return jsonify(filmes)


if __name__ == "__main__":
    app.run(debug=True)