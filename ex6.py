from flask import Flask, jsonify, request

app = Flask(__name__)

carros = [
    {
        "id": 30,
        "modelo": "QQ",
        "marca": "Chery",
        "ano": 1999
    },
    {
        "id": 20,
        "modelo": "up!",
        "marca": "Volkswagen",
        "ano": 2014
    },
    {
            "id":9,
            "modelo":" Sai",
            "marca":"toyota",
            "ano":2009
    },
]


@app.route("/carros1", methods=["GET"])
def listar_carros():
    return jsonify(carros)


@app.route("/carros/<int:id>", methods=["GET"])
def buscar_carros(id):
    for carro in carros:
        if carro["id"] == id:
            return jsonify(carro)

    return jsonify({"erro": "Carro não encontrado"}), 404

 
@app.route("/carros", methods=["GET"])
def pesquisar_carros():
    marca = request.args.get("marca")
    carros_r = []
    print(marca)
    if marca:
        for carro in carros:
            if  marca.lower() in carro["marca"].lower():
                carros_r.append(carro)

        return jsonify(carros_r)


    return jsonify(carros)


if __name__ == "__main__":
    app.run(debug=True)