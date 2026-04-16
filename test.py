from gradio_client import Client, handle_file

client = Client("gokaygokay/Florence-2")

result = client.predict(
    image=handle_file("IMG_0007.jpeg"),
    task_prompt="Caption",
    text_input="", # Changed from None to ""
    model_id="microsoft/Florence-2-large",
    api_name="/process_image"
)
print(result)
