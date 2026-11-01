# TP-Final-Integrador-Prog2

## Intregrantes
BARBERIS Pablo Cesar
CUADRA VILCHEZ Ingrid Anneris
FERREIRA Maria Belen

## Ejecucion

Desde esta carpeta, instalar Flask e iniciar el servidor:

```powershell
pip install flask
python -m flask run
```

## Ejercicios

1. Clase `Aguila`: `aguila.py`.
2. Clase `Rinoceronte`: `rinoceronte.py`.
3. Clase `Empleado`: `empleado.py`.
4. Clase `Zoologico`: `zoologico.py`.
5. Comparacion por ID y representaciones: `animal.py`, `jirafa.py`, `aguila.py`, `rinoceronte.py`, `empleado.py` y `zoologico.py`.
6. Cuidadores principales: `servicio_empleados.py`.
7. Animales por cuidador principal: `servicio_animales.py`.

## Rutas de verificacion

- `http://localhost:5000/zoologicos/1/`
- `http://localhost:5000/zoologicos/1/cuidadores-principales/`
- `http://localhost:5000/zoologicos/1/cuidadores-principales/1/animales`