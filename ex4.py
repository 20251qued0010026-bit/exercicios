from flask import Flask, jsonify, request

app = Flask(__name__)

musicas = [
    {
        "id":7,
        "nome":"Stay",
        "artista":"Maurice Williams & the Zodiacs",
        "ano":1960
    },
    {
        "id":2,
        "nome":"From Me to You",
        "artista":"Legiao Urbana",
        "ano":1963
    },
    {
        "id":3,
        "nome":"Old Town Road",
        "artista":"Legiao Urbana",
        "ano":2019
    }
]

@app.route("/musicas1", methods=["GET"])
def mostrar_musicas():
    return jsonify(musicas)


@app.route("/musicas/<int:id>", methods=["GET"])
def buscar_musicas(id):
    for musica in musicas:
        if musica["id"] == id:
            return jsonify(musica)

    return jsonify({"erro": "Musica não encontrado"}), 404

 
@app.route("/musicas", methods=["GET"])
def pesquisar_musicas():
    artista = request.args.get("artista")
    musicas_r = []
    print(artista)
    if artista:
        for musica in musicas:
            if  artista.lower() in musica["artista"].lower():
                musicas_r.append(musica)

        return jsonify(musicas_r)

    return jsonify(musicas)


if __name__ == "__main__":
    app.run(debug=True)