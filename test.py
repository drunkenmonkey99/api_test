from flask import Flask, request, jsonify

app = Flask(__name__)  # name will import all the named functions


# get means sending a data/searchquery through URL, e.g. google search
# whereas POST means sending data through the body in a way data is not visible to the user e.g. login using password we cannot see it in URL
@app.route('/xyz', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        return jsonify(str(result))


if __name__ == '__main__':
    app.run()

# error 400 means an issue from client side (postman), 404 server down, and error 500 means an issue from the server side, 200 is successful
