from flask import Flask, request, jsonify

app = Flask(__name__)
cart =[]

def check_fields(body, fields):
    required_parameters_set = set(fields)
    fields_set = set(body.keys())
    return required_parameters_set <= fields_set

@app.route('/')
def hello_world():
    return "Coucou !"

@app.route('/cart', methods=['GET'])
def list_cart():
    return jsonify(cart), 200

@app.route('/cart', methods=['POST'])
def add_to_cart():
    try:
        body = request.get_json()
        if 'id' not in body.keys() or 'quantity' not in body.keys():
            return jsonify({'error': "Missing fields."}), 400
        
        for i, item in enumerate(cart):
            if item['id'] == body['id']:
                cart[i]['quantity'] += int(body['quantity'])
                return jsonify({}), 200
        
        cart.append(body)
        return jsonify({}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/cart', methods=['PATCH'])
def edit_cart():
    try:
        body = request.get_json()
        if not chek_fields(body, {'id', 'quantity'}):
            return jsonify({'error': "Missing fields."}), 400
        
        for i, item in enumerate(cart):
            if item['id'] == body['id']:
                cart[i]['quantity'] = int(body['quantity'])
                return jsonify({}), 200
        return jsonify({'error': "Product not found."}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)