import gradio as gr
import numpy as np
from simpleFunc import classify
from modelFunc import modelClassify

def combined_fn(Text4SimpleSearch, Text4LLM):
    result1 = classify(Text4SimpleSearch)
    result2 = modelClassify(Text4LLM)

    return result1, result2

demo = gr.Interface(
    fn=combined_fn,
    inputs=["text", "text"],
    outputs=["text", "text"],
    title="City Themeing Machine", 
    description="Theme your Data Here."
)

demo.launch(share = True)