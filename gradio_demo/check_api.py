import gradio as gr

def echo(text):
    return f"Name: {text}"

iface = gr.Interface(
    fn=echo,
    inputs=gr.Textbox(label="Your Name"),
    outputs=gr.Textbox(label="Hello"),
    show_api=True,
)

iface.launch(share=True)
