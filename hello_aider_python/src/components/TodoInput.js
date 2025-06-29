import React, { useState } from 'react';
import { useLLM } from './llm-context';

function TodoInput() {
  const [prompt, setPrompt] = useState('');
  const { createTodoItem } = useLLM();

  const handleInputChange = (e) => {
    setPrompt(e.target.value);
  };

  const handleCreateTodo = async () => {
    try {
      const newTodo = await createTodoItem(prompt, 500);
      // Update application state with newTodo -  This depends on your state management solution
      console.log("New Todo:", newTodo);
      setPrompt(""); // Clear the input field after successful creation
    } catch (error) {
      console.error("Error creating todo:", error);
      // Display error to the user -  Implement appropriate error handling
      alert("Error creating todo. Please try again."); // Simple alert for demonstration
    }
  };

  return (
    <div>
      <input
        type="text"
        value={prompt}
        onChange={handleInputChange}
        placeholder="Enter your todo prompt..."
      />
      <button onClick={handleCreateTodo}>Create Todo</button>
    </div>
  );
}

export default TodoInput;
