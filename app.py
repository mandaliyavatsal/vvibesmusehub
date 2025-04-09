import os
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import config

def download_model(model_name, model_dir):
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model.save_pretrained(model_dir)
    tokenizer.save_pretrained(model_dir)

def generate_music(model_name, prompt, length, model_dir):
    model = AutoModelForCausalLM.from_pretrained(model_dir)
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    generator = pipeline('text-generation', model=model, tokenizer=tokenizer)
    generated = generator(prompt, max_length=length, num_return_sequences=1)
    return generated[0]['generated_text']

def main():
    model_name = "gpt2"  # Example model name
    model_dir = config.MODEL_DIR

    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    download_model(model_name, model_dir)

    prompt = "Generate a music piece based on this prompt: "
    length = 100  # Example length

    music = generate_music(model_name, prompt, length, model_dir)
    print("Generated Music: ", music)

if __name__ == "__main__":
    main()
