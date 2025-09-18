from llamafactory.extras.misc import get_device_count
from vllm import LLM, SamplingParams

if __name__ == "__main__":
    prompts = [
        "Hello, my name is",
        "The president of the United States is",
        # "The capital of France is",
        # "The future of AI is",
    ]
    sampling_params = SamplingParams(
        temperature=0.8, 
        top_p=0.95,
        logprobs=20,
        return_logits=True,
        prompt_logprobs=1,
        max_tokens=512,
        extra_args={
            "enable_conf": True,
            "window_size": 2048,
            "threshold": 17,
        }
    )

    model_name_or_path = "/data/home/Licheng/ckpts/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B"  # Example model name
    llm = LLM(
        model=model_name_or_path,
        tensor_parallel_size=get_device_count(),
        pipeline_parallel_size=1,
        enable_prefix_caching=True,
    )

    outputs = llm.generate(prompts, sampling_params)

    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")