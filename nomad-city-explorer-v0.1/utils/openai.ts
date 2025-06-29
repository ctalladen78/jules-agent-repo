import { Configuration, OpenAIApi } from 'openai'

const configuration = new Configuration({
  apiKey: process.env.NEXT_PUBLIC_OPENAI_API_KEY,
})

const openai = new OpenAIApi(configuration)

export async function getOpenAIResponse(messages: { role: string; content: string }[], maxTokens: number = 100) {
  try {
    const response = await openai.createChatCompletion({
      model: "gpt-3.5-turbo",
      messages: messages,
      max_tokens: maxTokens,
    })

    return response.data.choices[0].message?.content
  } catch (error) {
    console.error('Error calling OpenAI:', error)
    throw new Error('Failed to get a response from OpenAI')
  }
}

