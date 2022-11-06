from flask import Flask, jsonify
from nexiona.config import DATA
import pandas as pd

app = Flask(__name__)

# API END POINT PARA VISITAS UNICAS
@app.route('/unique', methods=['GET'])
def get_unicas():
    unicas = "no data received"
    if DATA != []:
        unicas = pd.DataFrame(DATA).drop_duplicates().groupby(['PATH'])['ID'].count()
        unicas = unicas.to_json()
    return unicas    

# API END POINT PARA VISUALIZAR EL TOTAL DE LAS VISITAS ALMACENADAS
@app.route('/totals', methods=['GET'])
def get_totales():
    return jsonify(DATA)
