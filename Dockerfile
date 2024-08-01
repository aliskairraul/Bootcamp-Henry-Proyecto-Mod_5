# Usar una imagen base de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requerimientos y la aplicación
COPY requirements.txt requirements.txt
COPY main.py main.py

# Instalar las dependencias
RUN pip install -r requirements.txt

# Exponer el puerto que usará la aplicación
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:server"]
