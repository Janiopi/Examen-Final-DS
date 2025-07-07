# Imagen base
FROM python:3.10-slim
# Directorio de trabajo
WORKDIR /app 
# Copiando dependencias
COPY requirements.txt .
# Instalándolas
RUN pip install --no-cache-dir -r requirements.txt
# Copiando el resto de archivos
COPY . .
# Configurando el pythonpath de acuerdo a nuestro workdir
ENV PYTHONPATH="${PYTHONPATH}:/app"
# Ejecutando pytest dentro del contenedor
CMD ["pytest"]

