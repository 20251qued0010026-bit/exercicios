from flask import Flask, jsonify, request

app = Flask(__name__)

produtos = [
    {
        "id": 20,
        "nome": "Notebook",
        "preco": 5.500,
        "categoria": "informatica"
    },
    {
        "id": 2,
        "nome":"refrigerante",
        "preco":9.50,
        "categoria":"bebidas"
    },
    {
        "id":3,
        "nome":"nutella",
        "preco":34.50,
        "categoria":"comidas"
    }
]

@app.route("/produtos1", methods=["GET"])
def mostrar_produto():
    return jsonify(produtos)


@app.route("/produtos/<int:id>", methods=["GET"])
def buscar_produtos(id):
    for produto in produtos:
        if produto["id"] == id:
            return jsonify(produto)

    return jsonify({"erro":"Produto não encontrado"}), 404

 
@app.route("/produtos", methods=["GET"])
def pesquisar_produto():
    categoria = request.args.get("categoria")
    produtos_r = []
    print(categoria)
    if categoria:
        for produto in produtos:
            if  categoria.lower() in produto["categoria"].lower():
                produtos_r.append(produto)

        return jsonify(produtos_r)



    return jsonify(produtos)


if __name__ == "__main__":
    app.run(debug=True)