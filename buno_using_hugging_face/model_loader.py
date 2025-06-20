from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, pipelines
from huggingface_hub import login


def model_loader():
    # Configure 4-bit quantization
  model_id = "Qwen/Qwen3-0.6B-Base"
  bnb_config = BitsAndBytesConfig(
      load_in_4bit=True,
      bnb_4bit_use_double_quant=True,
      bnb_4bit_quant_type="nf4",     # use "fp4" for speed
      bnb_4bit_compute_dtype="float16"
  )

  model = AutoModelForCausalLM.from_pretrained(
      model_id,
      quantization_config=bnb_config,
      device_map="auto"
  )
  tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-0.6B-Base")

  return model, tokenizer

if __name__ == "__main__":
  model_loader()