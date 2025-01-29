from services.db_config import get_connection

def count_reservations_by_customer(customer_id):
    connection = get_connection()
    try:
        with connection.cursor(dictionary=True) as cursor:
            query = """
                SELECT COUNT(*) AS reservation_count
                FROM ReservationDB.Reservation r
                JOIN CustomerCreateDb.Customers c ON r.CustomerID = c.CustomerID
                WHERE r.CustomerID = %s
            """
            cursor.execute(query, (customer_id,))
            result = cursor.fetchone()
            return result
    except Exception as e:
        return {"error": str(e)}
    finally:
        connection.close()

def get_reservations_by_customer(customer_id):
    connection = get_connection()
    try:
        with connection.cursor(dictionary=True) as cursor:
            query = """
                SELECT * 
                FROM ReservationDB.Reservation r
                JOIN CustomerCreateDb.Customers c ON r.CustomerID = c.CustomerID
                WHERE r.CustomerID = %s
            """
            cursor.execute(query, (customer_id,))
            result = cursor.fetchall()
            return result
    except Exception as e:
        return {"error": str(e)}
    finally:
        connection.close()

def get_customer_details_with_reservations(customer_id):
    connection = get_connection()
    try:
        with connection.cursor(dictionary=True) as cursor:
            query = """
                SELECT c.CustomerID, c.FirstName, c.LastName, COUNT(r.ReservationID) AS reservation_count
                FROM ReservationDB.Reservation r
                JOIN CustomerCreateDb.Customers c ON r.CustomerID = c.CustomerID
                WHERE r.CustomerID = %s
                GROUP BY c.CustomerID
            """
            cursor.execute(query, (customer_id,))
            result = cursor.fetchone()
            return result
    except Exception as e:
        return {"error": str(e)}
    finally:
        connection.close()
def get_all_reservations():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    
    query = """
    SELECT * 
    FROM ReservationDB.Reservation
    """
    
    cursor.execute(query)
    reservations = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return reservations
