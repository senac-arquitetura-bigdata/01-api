from flask import Flask, jsonify
from faker import Faker
from faker_vehicle import VehicleProvider
# https://pypi.org/project/faker-vehicle/

fake = Faker()
fake.add_provider(VehicleProvider)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def cadastros():
    cadastros = []
    for _ in range(fake.randomize_nb_elements(number=1, ge=True, min=5)):
        cadastros.append(gerador_cadastro())
    return jsonify({'cadastros': cadastros})

def gerador_cadastro():
    return {
        'id': fake.numerify(text='id-%#%#'),
        'nome': fake.name(),
        'telefone': fake.numerify(text='(%%) 9%%%%-%%%%'),
        'email': fake.ascii_safe_email(),
        'endereco': fake.address(),
        'veiculo': {
            'placa': fake.license_plate(),
            'ano': fake.vehicle_year(),
            'fabricante': fake.vehicle_make(),
            'modelo': fake.vehicle_model()
        }
    }

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)