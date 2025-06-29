import React, { useState, useEffect } from 'react';
import { useLLM } from './llm-context';

function TodoInput() {
  const [prompt, setPrompt] = useState('');
  const [tokenCount, setTokenCount] = useState(0);
  const [maxTokens, setMaxTokens] = useState(500); // Make maxTokens configurable
  const { createTodoItem } = useLLM();

  const handleInputChange = async (e) => {
    setPrompt(e.target.value);
    const count = await countTokens(e.target.value);
    setTokenCount(count);
  };

  const handleCreateTodo = async () => {
    try {
      const newTodo = await createTodoItem(prompt, maxTokens);
      console.log("New Todo:", newTodo);
      setPrompt('');
      setTokenCount(0);
    } catch (error) {
      console.error("Error creating todo:", error);
      alert(error.message); // Display the error message from the LLM call
    }
  };

  // Placeholder - Replace with your actual token counting implementation.  This is crucial!
  const countTokens = async (text) => {
    const response = await fetch('/api/countTokens', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text }),
    });
    if (!response.ok) {
      console.error("Error fetching token count:", response.status);
      return 0; // Or handle the error appropriately
    }
    const data = await response.json();
    return data.tokenCount;
  };


  return (
    <div>
      <input
        type="text"
        value={prompt}
        onChange={handleInputChange}
        placeholder="Enter your todo prompt..."
      />
      <div>Tokens used: {tokenCount}/{maxTokens}</div>
      <button onClick={handleCreateTodo} disabled={tokenCount >= maxTokens}>
        Create Todo
      </button>
    </div>
  );
}

export default TodoInput;
