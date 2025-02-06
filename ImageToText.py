from huggingface_hub import InferenceClient

client = InferenceClient(
	provider="together",
	api_key="TokenPlace"
)

link = input("add your link here:")

messages = [
	{
		"role": "user",
		"content": [
			{
				"type": "text",
				"text": "Describe this image in one sentence."
			},
			{
				"type": "image_url",
				"image_url": {
					"url": link
				}
			}
		]
	}
]

completion = client.chat.completions.create(
    model="meta-llama/Llama-3.2-11B-Vision-Instruct", 
	messages=messages, 
	max_tokens=500
)

print(completion.choices[0].message.content)