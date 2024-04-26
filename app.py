import gradio as gr
from cesar import cesar

demo = gr.Interface(
    fn=cesar, 
    inputs=[gr.inputs.Textbox(label="Palabra"), gr.inputs.Textbox(label="Desplazamiento")], 
    outputs="text"
)