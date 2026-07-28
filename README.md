# OCI Agent Streamlit Assistant

## Descripción general del proyecto

Este proyecto consiste en una aplicación web desarrollada con **Streamlit** e integrada con un agente de **OCI Generative AI Agents** mediante el **Oracle Cloud Infrastructure Python SDK**. Su objetivo es ofrecer una interfaz conversacional simple desde navegador para consultar información procesada por un agente IA desplegado en Oracle Cloud.

La solución permite que un usuario escriba preguntas en una interfaz tipo chat y reciba respuestas generadas por el agente configurado en OCI. La aplicación fue desplegada públicamente usando **Railway**, lo que facilita su acceso sin necesidad de instalar software adicional en el equipo del usuario final.

## Arquitectura de la solución implementada

La arquitectura de la solución sigue un flujo cliente-aplicación-servicio cloud:

```text
Usuario final
   ↓
Aplicación web en Streamlit
   ↓
OCI Python SDK
   ↓
OCI Generative AI Agent Runtime
   ↓
Agent Endpoint en OCI
   ↓
Agente IA configurado en Oracle Cloud
```

### Flujo de funcionamiento

1. El usuario abre la aplicación web desplegada en Railway.
2. Escribe una pregunta en la interfaz de chat.
3. La aplicación `app.py` recibe la consulta.
4. El SDK de OCI autentica la solicitud usando variables de entorno.
5. La aplicación crea o reutiliza una sesión conversacional con el agente.
6. La pregunta se envía al **OCI Generative AI Agent Runtime**.
7. El agente procesa la consulta y genera una respuesta.
8. La respuesta se muestra en pantalla al usuario.

## Tecnologías y herramientas utilizadas

### Lenguajes y framework

- **Python**
- **Streamlit**

### Servicios cloud

- **Oracle Cloud Infrastructure (OCI)**
- **OCI Generative AI Agents**
- **OCI Generative AI Agent Runtime**
- **Railway**

### Herramientas de desarrollo

- **Visual Studio Code**
- **Git**
- **GitHub**
- **OCI Cloud Shell**

### Librerías principales

- `streamlit`
- `oci`

## Estructura del proyecto

```text
OCI_AGENT/
├── app.py
├── requirements.txt
├── railway.json
├── .gitignore
└── README.md
```

## Instrucciones para ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/diegoVC99/Challenge_ALURA.git
cd OCI_AGENT
```

### 2. Crear un entorno virtual

```bash
python -m venv .venv
```

### 3. Activar el entorno virtual

#### En Windows

```bash
.\.venv\Scripts\activate
```

#### En Linux o macOS

```bash
source .venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Configurar variables de entorno

Se deben definir las siguientes variables:

- `OCI_AGENT_ENDPOINT_ID`
- `OCI_AGENT_RUNTIME_ENDPOINT`
- `OCI_USER_OCID`
- `OCI_FINGERPRINT`
- `OCI_TENANCY_OCID`
- `OCI_REGION`
- `OCI_PRIVATE_KEY`

Ejemplo:

```env
OCI_AGENT_ENDPOINT_ID=ocid1.genaiagentendpoint.oc1.sa-saopaulo-1.xxxxx
OCI_AGENT_RUNTIME_ENDPOINT=https://agent-runtime.generativeai.sa-saopaulo-1.oci.oraclecloud.com
OCI_USER_OCID=ocid1.user.oc1..xxxxx
OCI_FINGERPRINT=aa:bb:cc:dd:ee:ff:11:22:33:44:55:66:77:88:99:00
OCI_TENANCY_OCID=ocid1.tenancy.oc1..xxxxx
OCI_REGION=sa-saopaulo-1
OCI_PRIVATE_KEY=-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----
```

### 6. Ejecutar la aplicación localmente

```bash
python -m streamlit run app.py
```

### 7. Despliegue en Railway

1. Subir el proyecto a GitHub.
2. Crear un nuevo proyecto en Railway desde el repositorio.
3. Agregar las variables de entorno.
4. Configurar el dominio público desde **Networking > Public Networking**.
5. Usar el puerto correcto detectado por la aplicación, por ejemplo `8080`.

## Ejemplos de preguntas que el agente puede responder

Estas preguntas dependen del conocimiento cargado en el agente dentro de OCI. Algunos ejemplos típicos son:

- "¿Cuál es la política de vacaciones de la empresa?"
- "¿Qué dice el procedimiento de atención de incidentes?"
- "Resume el documento de onboarding para nuevos empleados."
- "¿Cuáles son las funciones del área comercial?"
- "¿Qué pasos se deben seguir para registrar una incidencia interna?"
- "Explícame el contenido del manual operativo."

## Ejemplos de respuestas generadas por el agente

Los siguientes ejemplos son ilustrativos del tipo de respuesta que puede entregar la aplicación:

### Ejemplo 1

**Pregunta:**

```text
¿Cuál es la política de vacaciones de la empresa?
```

**Respuesta esperada del agente:**

```text
La política de vacaciones indica que los colaboradores deben coordinar sus días de descanso con su jefe inmediato y registrar la solicitud con anticipación según el procedimiento interno establecido.
```

### Ejemplo 2

**Pregunta:**

```text
Resume el documento de onboarding para nuevos empleados.
```

**Respuesta esperada del agente:**

```text
El documento de onboarding describe las etapas de inducción, presentación del equipo, acceso a herramientas, revisión de políticas internas y seguimiento durante los primeros días de ingreso.
```

### Ejemplo 3

**Pregunta:**

```text
¿Qué pasos se deben seguir para registrar una incidencia interna?
```

**Respuesta esperada del agente:**

```text
Primero se debe identificar el tipo de incidencia, luego registrar el caso en el canal definido por la empresa, adjuntar la evidencia correspondiente y notificar al área responsable para su seguimiento.
```

## Archivo `requirements.txt`

Contenido mínimo sugerido:

```txt
streamlit
oci
```

## Configuración de Railway

Archivo `railway.json` sugerido:

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

## Troubleshooting

### Error: `Authorization failed or requested resource not found`

Verificar:

- que el `OCI_AGENT_ENDPOINT_ID` sea el OCID del endpoint y no del agente
- que el endpoint esté en estado **Active**
- que la región configurada coincida con la del runtime
- que el usuario tenga permisos correctos en OCI

### La URL pública no abre en Railway

Verificar:

- que el servicio esté online
- que exista un dominio en **Public Networking**
- que el dominio apunte al puerto correcto
- que la aplicación escuche en `0.0.0.0`

### Problemas con la clave privada

Verificar:

- que no tenga comillas extra
- que incluya `BEGIN PRIVATE KEY` y `END PRIVATE KEY`
- que si se coloca en una línea use `\n`

## Seguridad

- No incluir secretos en el repositorio.
- No hardcodear credenciales en `app.py`.
- Utilizar siempre variables de entorno.
- Limitar el acceso a las credenciales OCI.

## Mejoras futuras

- Historial persistente de conversaciones.
- Interfaz visual más personalizada.
- Control de autenticación para usuarios finales.
- Panel administrativo de consultas.
- Integración con una base documental más amplia.

## Autor

Proyecto desarrollado por Diego Valderrama como implementación práctica de un asistente conversacional basado en Streamlit, Railway y OCI Generative AI Agents.