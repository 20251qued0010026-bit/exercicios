from flask import Flask, jsonify, request

app = Flask(__name__)

funcionarios = [
    {
        "id":15,
        "nome":"maria b",
        "cargo":"medica",
        "asalario": 60.000
    },
    {
            "id":4,
            "nome":"jaanai",
            "cargo":"cozinheira",
            "asalario": 0.2
    },
    {
        "id":3,
        "nome":"gaysa",
        "cargo":"programador",
        "asalario": 1.000
    }
]

@app.route("/funcionarios1", methods=["GET"])
def mostrar_funcionarios():
    return jsonify(funcionarios)


@app.route("/funcionarios/<int:id>", methods=["GET"])
def buscar_funcionarios(id):
    for funcionario in funcionarios:
        if funcionario["id"] == id:
            return jsonify(funcionario)

    return jsonify({"erro": "funcionario não encontrado"}), 404

 
@app.route("/funcionarios", methods=["GET"])
def pesquisar_funcionarios():
    cargo = request.args.get("cargo")
    funcionarios_r = []
    print(cargo)
    if cargo:
        for funcionario in funcionarios:
            if  cargo.lower() in funcionario["cargo"].lower():
                funcionarios_r.append(funcionarios)


        return jsonify(funcionarios_r)

    return jsonify(funcionarios)


if __name__ == "__main__":
    app.run(debug=True)