import os
import streamlit as st
import oci

st.set_page_config(page_title="Agente Corporativo IA", page_icon="🤖")
st.title("🤖 Agente Corporativo IA")
st.caption("Consulta información de documentos internos")

required_vars = [
    "OCI_AGENT_ENDPOINT_ID",
    "OCI_AGENT_RUNTIME_ENDPOINT",
    "OCI_USER_OCID",
    "OCI_FINGERPRINT",
    "OCI_TENANCY_OCID",
    "OCI_REGION",
    "OCI_PRIVATE_KEY"
]

missing = [var for var in required_vars if not os.environ.get(var)]
if missing:
    st.error(f"Faltan variables de entorno: {', '.join(missing)}")
    st.stop()

agent_endpoint_id = os.environ["OCI_AGENT_ENDPOINT_ID"]
service_endpoint = os.environ["OCI_AGENT_RUNTIME_ENDPOINT"]

config = {
    "user": os.environ["OCI_USER_OCID"],
    "fingerprint": os.environ["OCI_FINGERPRINT"],
    "tenancy": os.environ["OCI_TENANCY_OCID"],
    "region": os.environ["OCI_REGION"],
    "key_content": os.environ["OCI_PRIVATE_KEY"].replace("\\n", "\n")
}

try:
    oci.config.validate_config(config)
    client = oci.generative_ai_agent_runtime.GenerativeAiAgentRuntimeClient(
        config=config,
        service_endpoint=service_endpoint
    )
except Exception as e:
    st.error(f"Error al crear cliente OCI: {str(e)}")
    st.stop()

if "session_id" not in st.session_state:
    try:
        session = client.create_session(
            agent_endpoint_id=agent_endpoint_id,
            create_session_details=oci.generative_ai_agent_runtime.models.CreateSessionDetails(
                display_name="SesionWeb",
                description="Sesion creada desde Streamlit"
            )
        )
        st.session_state.session_id = session.data.id
    except Exception as e:
        st.error(f"Error al crear la sesión del agente: {str(e)}")
        st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Escribe tu pregunta...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    try:
        response = client.chat(
            agent_endpoint_id=agent_endpoint_id,
            chat_details=oci.generative_ai_agent_runtime.models.ChatDetails(
                user_message=prompt,
                session_id=st.session_state.session_id
            )
        )
        answer = response.data.message.content.text
    except Exception as e:
        answer = f"Error al consultar el agente: {str(e)}"

    st.session_state.messages.append({"role": "assistant", "content": answer})

    with st.chat_message("assistant"):
        st.write(answer)