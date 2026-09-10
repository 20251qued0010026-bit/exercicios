from flask import Flask, jsonify, request

app = Flask(__name__)

resturantes = [
    {
        "id": 60,
        "nome": "Harumi",
        "tipo": "japonesa",
        "cidade": "quedas do guacu"
    },
    {
        "id": 50,
        "nome": "Bon apetit",
        "tipo": "Italiano",
        "cidade": "sao paulo"
    },
    {
            "id": 20,
            "nome": "Mangua",
            "tipo": "Italiano",
            "cidade": "Roma"
    }
]


@app.route("/restaurante1", methods=["GET"])
def listar_restaurantes():
    return jsonify(resturantes)


@app.route("/restaurantes/<int:id>", methods=["GET"])
def buscar_restaurantes(id):
    for restaurante in resturantes:
        if restaurante["id"] == id:
            return jsonify(resturantes)

    return jsonify({"erro": "Restaurante não encontrado"}), 404

 
@app.route("/restaurantes", methods=["GET"])
def pesquisar_restaurantes():
    tipo = request.args.get("tipo")
    resturantes_r = []
    print(tipo)
    if tipo:
        for restaurante in restaurantes:
            if  tipo.lower() in restaurante["tipo"].lower():
                resturantes_r.append(restaurante)

        return jsonify(resturantes_r)

    return jsonify(resturantes)

app.run(debug=True)