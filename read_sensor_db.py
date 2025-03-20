import psycopg2
from datetime import datetime
import RPi.GPIO as GPIO  # Biblioteca para controlar o GPIO
import time

# Configurar o GPIO
GPIO.setmode(GPIO.BCM)  # Usando o modo BCM para os números dos pinos
LIGHT_PIN = 17  # Substitua pelo pino que você está usando
GPIO.setup(LIGHT_PIN, GPIO.IN)  # Defina o pino como entrada

# Função para verificar o status da luz e salvar no banco de dados
def log_light_status():
    # Verifique o estado do pino (HIGH = luz ligada, LOW = luz desligada)
    light_status = GPIO.input(LIGHT_PIN) == GPIO.HIGH
    
    # Conectar ao banco de dados PostgreSQL
    conn = psycopg2.connect(
        dbname="light_database",
        user="postgres",
        password="1234",  # Substitua pela sua senha do PostgreSQL
        host="localhost"
    )
  
  # Criar um cursor
    cur = conn.cursor()
    
    # Inserir o status da luz no banco de dados
    cur.execute("INSERT INTO light_status (status) VALUES (%s)", (light_status,))
    
    # Confirmar a transação
    conn.commit()
    
    # Fechar o cursor e a conexão
    cur.close()
    conn.close()

    print(f"Light status logged: {'ON' if light_status else 'OFF'} at {datetime.now()}")

# Chamar a função para registrar o status da luz
try:
	while True:
		log_light_status()
		time.sleep(1)
except KeyboardInterrupt:
	print("Processo interrompido")

finally:
	GPIO.cleanup()

# Finalizar o uso do GPIO
GPIO.cleanup()


