import gradio as gr

def return_image(img1):
    return img1

with gr.Blocks() as demo:
    with gr.Row():
        img1 = gr.Image(label="Image 1", type="pil")
        
    btn = gr.Button("Submit")
    out = gr.Image(label="Output Image", type="pil")

    btn.click(return_image, inputs=[img1], outputs=out, api_name="test")

demo.queue().launch(share=True, debug=True)