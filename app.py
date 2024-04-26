import gradio as gr
from cesar import cesar

demo = gr.Interface(fn=cesar, inputs="text", outputs="text")
demo.launch()