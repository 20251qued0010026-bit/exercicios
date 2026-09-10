from flask import Flask, jsonify, request

app = Flask(__name__)

jogos = [
    {
        "id": 10,
        "nome": "Roblox",
        "genero": "rpg",
        "ano": 2016
    },
    {
        "id": 50,
        "nome": "Minecraft",
        "genero": "aventura",
        "ano": 2000
    },
    {
            "id": 20,
            "nome": "Free-fire",
            "genero": "acao",
            "ano": 2014
    }
]


@app.route("/jogos1", methods=["GET"])
def listar_jogos():
    return jsonify(jogos)


@app.route("/jogos/<int:id>", methods=["GET"])
def buscar_jogos(id):
    for jogo in jogos:
        if jogo["id"] == id:
            return jsonify(jogos)

    return jsonify({"erro": "Jogo não encontrado"}), 404

 
@app.route("/jogos", methods=["GET"])
def pesquisar_jogo():
    genero = request.args.get("genero")
    jogos_r = []
    print(genero)
    if genero:
        for jogo in jogos:
            if  genero.lower() in jogo["genero"].lower():
                jogos_r.append(jogo)

        return jsonify(jogos_r)

    return jsonify(jogos)

app.run(debug=True)