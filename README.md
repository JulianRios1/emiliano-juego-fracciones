# Carrera de Fracciones 🍕

Juego para aprender fracciones en el salón. Se proyecta en una pantalla y las filas del salón compiten como equipos (de 2 a 8 filas, con nombre, cantidad de alumnos e ícono configurables).

## Niveles
1. Partes de un todo (pizzas y chocolates)
2. ¿Cuál es mayor? (comparar)
3. Equivalentes y fracción de un grupo
4. Sumar y restar con mismo denominador
5. Fracciones heterogéneas (distinto denominador y denominador común)
- Mezcla de todo

## Modos
- **Por turnos**: responde una fila (10 pts). Si falla, rebota a la siguiente (5 pts).
- **Todas a la vez**: cada fila levanta su tarjeta A, B, C o D y el docente marca quién acertó.

## Fin de la partida
- **Por preguntas**: número fijo de preguntas por fila.
- **Por puntos**: se juega hasta que una fila llega a la meta (30 a 150 puntos). Si dos filas la pasan empatadas, sigue una pregunta de desempate.

Teclado: `A–D` o `1–4` para responder, `Enter` para seguir.

## Correr con Docker

```bash
docker compose up -d --build
```

Abrir http://localhost:8000

Sin compose:

```bash
docker build -t emiliano-juego-fracciones .
docker run -d -p 8000:8000 --name juego emiliano-juego-fracciones
```

Otro puerto: `docker run -e PORT=8080 -p 8080:8080 emiliano-juego-fracciones`

## Correr sin Docker

```bash
pip install -r requirements.txt
python main.py
```

## Estructura
```
main.py            # servidor FastAPI (/ y /health)
static/index.html  # el juego completo (HTML + CSS + JS)
Dockerfile
docker-compose.yml
```
