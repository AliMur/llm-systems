## What this project is
Local LLM System with Fine-Tuning + Evaluation + Serving

### Core components
1. Base model
    * Open-weight LLM (7B class)
    * Run locally using Ollama
2. Adaptation
    * LoRA fine-tune on a narrow, realistic task
    * Small but clean dataset
3. Evaluation
    * Golden dataset
    * Before vs after metrics
    * Regression checks
4. Serving
    * HTTP API
    * Concurrent requests
    * Latency measurements
5. Tradeoffs documented
    * Why this model?
    * Why this batch size?
    * Why this evaluation metric?

### Base model chosen
mistralai/Mistral-7B-Instruct - is a popular low-cost model, good for experimentation.

How to run inference locally
make sure ollama is installed and is serving
uv run ./inference/model.py

this repo uses uv for python version and dependency management
default configuration for accelerate :
    copy accelerate_config_template.yaml to ~/.cache/huggingface/accelerate/default_config.yaml and run accelerate config if needed.