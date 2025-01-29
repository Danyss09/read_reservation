from flask import Blueprint, request, jsonify
import requests
from models.reservation_model import count_reservations_by_customer, get_reservations_by_customer, get_customer_details_with_reservations, get_all_reservations

reservation_bp = Blueprint('reservation', __name__)

CUSTOMER_SERVICE_URL = "http://localhost:5000/get_customer"  # Asegúrate de que esta URL esté correctamente configurada

# Ruta para contar el número de reservas de un cliente
@reservation_bp.route('/count_reservations/<int:customer_id>', methods=['GET'])
def count_reservations_route(customer_id):
    # Validar si el cliente existe
    customer_response = requests.get(f"{CUSTOMER_SERVICE_URL}/{customer_id}")
    if customer_response.status_code != 200:
        return jsonify({"error": "Customer not found"}), 404
    
    # Si el cliente existe, contamos las reservas
    response = count_reservations_by_customer(customer_id)
    if "error" in response:
        return jsonify(response), 500
    return jsonify(response), 200

# Ruta para obtener todas las reservas de un cliente
@reservation_bp.route('/get_reservations/<int:customer_id>', methods=['GET'])
def get_reservations_route(customer_id):
    # Validar si el cliente existe
    customer_response = requests.get(f"{CUSTOMER_SERVICE_URL}/{customer_id}")
    if customer_response.status_code != 200:
        return jsonify({"error": "Customer not found"}), 404
    
    # Si el cliente existe, obtenemos las reservas
    response = get_reservations_by_customer(customer_id)
    if "error" in response:
        return jsonify(response), 500
    return jsonify(response), 200

# Ruta para obtener los detalles del cliente junto con el número de reservas
@reservation_bp.route('/get_customer_details/<int:customer_id>', methods=['GET'])
def get_customer_details_route(customer_id):
    # Validar si el cliente existe
    customer_response = requests.get(f"{CUSTOMER_SERVICE_URL}/{customer_id}")
    if customer_response.status_code != 200:
        return jsonify({"error": "Customer not found"}), 404
    
    # Si el cliente existe, obtenemos los detalles junto con las reservas
    response = get_customer_details_with_reservations(customer_id)
    if "error" in response:
        return jsonify(response), 500
    return jsonify(response), 200
@reservation_bp.route('/get_all_reservations', methods=['GET'])
def get_all_reservations_route():
    # Obtener todas las reservas
    response = get_all_reservations()
    if not response:
        return jsonify({"error": "No reservations found"}), 404
    return jsonify(response), 200