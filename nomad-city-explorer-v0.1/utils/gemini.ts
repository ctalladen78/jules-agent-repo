import { GoogleGenerativeAI } from '@google/generative-ai'

export async function callGemini(messages: { role: string; content: string }[], maxTokens: number = 100, apiKey?: string) {
  const key = apiKey || process.env.NEXT_PUBLIC_GEMINI_API_KEY || 'PLACEHOLDER_GEMINI_API_KEY';
  if (!key || key === 'PLACEHOLDER_GEMINI_API_KEY') {
    console.error('Gemini API key is not set. Please check your environment variables.');
    throw new Error('Gemini API key is not set');
  }
  
  const genAI = new GoogleGenerativeAI(key);

  try {
    const model = genAI.getGenerativeModel({ model: 'gemini-pro' })

    const chat = model.startChat();

    const result = await chat.sendMessage(messages[messages.length - 1].content, {
      history: messages.slice(0, -1).map(msg => ({
        role: msg.role === 'user' ? 'user' : 'model',
        parts: msg.content,
      })),
    });
    const response = result.response
    return response.text()
  } catch (error) {
    console.error('Error calling Gemini:', error)
    throw new Error('Failed to get a response from Gemini: ' + (error instanceof Error ? error.message : String(error)))
  }
}

