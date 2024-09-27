from pdf_creator.pdf_creator import create_pdf
from send_mail.send_mail import send_mail
from flask import Flask, request, jsonify
from waitress import serve
import os
from functools import wraps

# result = {
#     "city" : "Kalety",
#     "date" : "28-08-2024",
#     "order_No" : "0001-CZECHTRANS-CZESŁAW-2024",
#     "course_No": "59-18-3-24",
#     "route":"(1) Passat-Stal<br>(2) KIEDROWSKI",
#     "loadings":"(1) Biała k/Płocka 09-411, KORDECKIEGO 23",
#     "unloadings":"(2) BYSŁAW, PRZEMYSŁOWA 8",
#     "comments" : "",
#     "price":"1450",
#     "currency":"PLN",
#     "driver":"PAWEŁ NOWOGÓRSKI",
#     "carrier_details":"UT CZECHTRANS JANINA JARZĘBIŃSKA KIEŁPINO/ LESZNO",
#     "ordering_person_details":"Szatkowska Weronika tel.: (24) 367 68 20",
#     "route_documents":"",
#     "phone":"123456789"
# }
API_KEY = os.getenv("API_KEY")


app = Flask(__name__)

def api_key_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-KEY')
        if api_key != API_KEY:
            return jsonify({"message": "Unauthorized access"}), 403
        return f(*args, **kwargs)
    return decorated_function

@app.route('/', methods=['GET'])
@api_key_required
def home():
    return "Api"

@app.route('/send_email', methods=['POST'])
@api_key_required
def run():
    data=request.get_json()
    file = data['order_No']

    try:
        create_pdf(name=file, data=data)
        send_mail(file=file, data=data)

        return jsonify({'message':"Email sent succesfully"}), 200
    except Exception as e:
        return jsonify({"field not found":str(e)}), 500
if __name__ == '__main__':
    serve(app, host="0.0.0.0", port="5000")