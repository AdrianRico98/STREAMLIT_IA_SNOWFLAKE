import streamlit as st
from snowflake.cortex import Complete
import time

st.title(":material/airwave: Respuesta en stream")

# Connect to Snowflake
try:
    # Works in Streamlit in Snowflake
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
except:
    # Works locally and on Streamlit Community Cloud
    from snowflake.snowpark import Session
    session = Session.builder.configs(st.secrets["connections"]["snowflake"]).create() 

llm_model = "claude-3-5-sonnet"
example_prompt = "What is Snowflake?"
prompt = st.text_area("prompt", example_prompt) 

# Choose streaming method
streaming_method = st.radio(
    "Streaming Method:",
    ["Direct (stream=True)", "Custom Generator"],
    help="Choose how to stream the response if there is any incompatibility with de direct stream method and the generator of the model"
)

if st.button("Generate Response"):
    # Method 1: Direct streaming with stream=True
    if streaming_method == "Direct (stream=True)":
        with st.spinner(f"Generating response with `{llm_model}`"):
            stream_generator = Complete(
                        session=session,
                        model=llm_model,
                        prompt=prompt,
                        stream=True,
                    )
                    
            st.write_stream(stream_generator)
    
    else:
        # Method 2: Custom generator 
        def custom_stream_generator():
            """
            Alternative streaming method for cases where
            the generator is not compatible with st.write_stream
            """
            output = Complete(
                session=session,
                model=llm_model,
                prompt=prompt
            )
            for chunk in output:
                yield chunks
                time.sleep(0.01)  # Small delay for smooth streaming
        
        with st.spinner(f"Generating response with `{llm_model}`"):
            st.write_stream(custom_stream_generator)

st.divider()
st.caption("Método de respuesta en stream")