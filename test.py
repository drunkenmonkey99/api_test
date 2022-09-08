from crypt import methods
from flask import Flask, request, jsonify

app = Flask(__name__)  # name will import all the named functions


# get means sending a data/searchquery through URL, e.g. google search
# whereas POST means sending data through the body in a way data is not visible to the user e.g. login using password we cannot see it in URL
@app.route('/xyz', methods=['GET', 'POST'])
def test(a, b):
    return a + b


print(test(1, 2))
