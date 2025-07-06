ollama:
	export OLLAMA_API_BASE=http://127.0.0.1:11434

aider_local:
	aider --model ollama/qwen2.5-coder:1.5b35k --llm-history-file .aider.session.md 

aider_gemini:
	aider --model gemini/gemini-1.5-flash-latest --cache-prompts --no-stream