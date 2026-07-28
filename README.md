# OCI Agent Streamlit Assistant

Aplicación web desarrollada con **Streamlit** e integrada con **OCI Generative AI Agents** mediante el **Oracle Cloud Infrastructure Python SDK**. El proyecto permite publicar un asistente conversacional accesible desde navegador y desplegarlo en **Railway** usando variables de entorno para la autenticación.

## Descripción

Este proyecto conecta una interfaz web simple en Streamlit con un agente IA ya creado en Oracle Cloud Infrastructure. La aplicación crea una sesión conversacional, envía mensajes al runtime del agente y muestra las respuestas en una interfaz tipo chat.

## Arquitectura

```text
Usuario
  ↓
App web en Streamlit
  ↓
OCI Python SDK
  ↓
OCI Generative AI Agent Runtime
  ↓
OCI Agent Endpoint
```

## Tecnologías usadas

- Python
- Streamlit
- Oracle Cloud Infrastructure Python SDK (`oci`)
- Railway
- GitHub

## Estructura del proyecto

```text
OCI_AGENT/
├── app.py
├── requirements.txt
├── railway.json
├── .gitignore
└── README.md
```

## Requisitos

Antes de ejecutar o desplegar el proyecto, se necesita:

- Python 3.10 o superior
- Un agente creado en OCI
- Un Agent Endpoint activo en OCI
- Credenciales OCI válidas
- Git instalado
- Cuenta en GitHub y Railway

## Variables de entorno

La aplicación usa estas variables de entorno:

- `OCI_AGENT_ENDPOINT_ID`
- `OCI_AGENT_RUNTIME_ENDPOINT`
- `OCI_USER_OCID`
- `OCI_FINGERPRINT`
- `OCI_TENANCY_OCID`
- `OCI_REGION`
- `OCI_PRIVATE_KEY`

### Ejemplo

```env
OCI_AGENT_ENDPOINT_ID=ocid1.genaiagentendpoint.oc1.sa-saopaulo-1.xxxxx
OCI_AGENT_RUNTIME_ENDPOINT=https://agent-runtime.generativeai.sa-saopaulo-1.oci.oraclecloud.com
OCI_USER_OCID=ocid1.user.oc1..xxxxx
OCI_FINGERPRINT=aa:bb:cc:dd:ee:ff:11:22:33:44:55:66:77:88:99:00
OCI_TENANCY_OCID=ocid1.tenancy.oc1..xxxxx
OCI_REGION=sa-saopaulo-1
OCI_PRIVATE_KEY=-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----
```

> `OCI_PRIVATE_KEY` puede guardarse en una sola línea usando `\n` para representar los saltos de línea.

## Instalación local

1. Clonar el repositorio:

```bash
git clone <TU_REPO_URL>
cd OCI_AGENT
```

2. Crear entorno virtual:

```bash
python -m venv .venv
```

3. Activar entorno virtual:

### Windows

```bash
.\.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

4. Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución local

Con las variables de entorno ya configuradas, ejecutar:

```bash
python -m streamlit run app.py
```

La aplicación normalmente se abrirá en:

```text
http://localhost:8501
```

## Despliegue en Railway

### 1. Subir el proyecto a GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <TU_REPO_URL>
git push -u origin main
```

### 2. Crear proyecto en Railway

- Ir a Railway
- Seleccionar **New Project**
- Elegir **Deploy from GitHub Repo**
- Seleccionar el repositorio

### 3. Configurar variables

Agregar en Railway las mismas variables de entorno usadas localmente.

### 4. Configurar `railway.json`

```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "streamlit run app.py --server.address 0.0.0.0 --server.port $PORT --server.fileWatcherType none --browser.gatherUsageStats false"
  }
}
```

### 5. Habilitar dominio público

En Railway:

- Ir a **Settings > Networking > Public Networking**
- Elegir **Generate Domain**
- Usar el puerto donde la app esté escuchando, por ejemplo `8080`

## Archivo `requirements.txt`

Ejemplo mínimo:

```txt
streamlit
oci
```

## Funcionalidades principales

- Interfaz de chat en Streamlit
- Integración con OCI Agent Runtime
- Manejo de variables de entorno para seguridad
- Despliegue público en Railway
- Sesión conversacional persistente durante el uso de la app

## Troubleshooting

### Error: `Authorization failed or requested resource not found`

Revisar:

- Que `OCI_AGENT_ENDPOINT_ID` sea el OCID del endpoint y no del agente
- Que el endpoint esté en estado **Active**
- Que la región del endpoint y del runtime coincidan
- Que el usuario OCI tenga permisos suficientes

### La URL pública no abre en Railway

Revisar:

- Que el servicio esté realmente **online**
- Que exista **Public Networking**
- Que el dominio esté generado para el puerto correcto
- Que la app escuche en `0.0.0.0` y en `$PORT`

### Problemas con la private key

Revisar:

- Que no tenga comillas extra
- Que conserve `BEGIN PRIVATE KEY` y `END PRIVATE KEY`
- Que si está en una sola línea use `\n`

## Seguridad

- No subir credenciales al repositorio
- No hardcodear secretos en `app.py`
- Usar siempre variables de entorno
- Evitar compartir el contenido real de la private key

## Mejoras futuras

- Historial de conversaciones
- UI más personalizada
- Autenticación de usuarios finales
- Registro de logs conversacionales
- Integración con base documental empresarial

## Autor

Proyecto desarrollado por Diego Valderrama como práctica de integración entre Streamlit, Railway y OCI Generative AI Agents.
