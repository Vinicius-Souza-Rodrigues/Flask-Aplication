from flask import Flask, render_template
from route.cliente import cliente

app = Flask(__name__)

# Registra o Blueprint
app.register_blueprint(cliente)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
