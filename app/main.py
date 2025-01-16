# app/main.py
from fastapi import FastAPI, HTTPException
from app.database import get_db_connection

app = FastAPI()

# Ruta de prueba
@app.get("/")
async def root():
    return {"message": "Welcome to the Reservation Service!"}

# Ruta para obtener todas las reservas
@app.get("/read")
async def read_reservations():
    connection = await get_db_connection()
    try:
        query = "SELECT * FROM Reservations;"
        reservations = await connection.fetch(query)
        
        # Si no hay reservas
        if not reservations:
            raise HTTPException(status_code=404, detail="No reservations found")
        
        # Convertir la respuesta en formato JSON
        result = [dict(reservation) for reservation in reservations]
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
    finally:
        await connection.close()
