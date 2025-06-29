'use client'

const GEMINI_API_KEY = process.env.NEXT_PUBLIC_GEMINI_API_KEY || '';

import { useState, useEffect } from 'react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { ScrollArea } from '@/components/ui/scroll-area'
import { Progress } from '@/components/ui/progress'
import { callGemini } from '@/utils/gemini'
import { useTokenLimit } from '@/contexts/TokenLimitContext'

interface ChatMessage {
  role: 'user' | 'assistant' | 'system'
  content: string
}

const travelOptions = [
  'Cost of Living',
  'Best Neighborhoods',
  'Public Transportation',
  'Local Cuisine',
  'Tourist Attractions',
  'Coworking Spaces',
  'Nightlife',
  'Safety',
]

const MAX_TOKENS = 100

// Simple function to estimate token count
const estimateTokenCount = (text: string): number => {
  return text.split(/\s+/).length;
}

export function Chat({ city }: { city: string }) {
  const [messages, setMessages] = useState<ChatMessage[]>([
    { role: 'system', content: `You are a helpful assistant providing information about ${city} for digital nomads.` },
  ])
  const [input, setInput] = useState('')
  const [apiKey, setApiKey] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [clickedOptions, setClickedOptions] = useState<Set<string>>(new Set())
  const { tokenCount, setTokenCount, isLimitReached, setIsLimitReached } = useTokenLimit()
  const [isUnlimited, setIsUnlimited] = useState(false)

  const handleOptionClick = async (option: string) => {
    if (isLimitReached && !apiKey && !isUnlimited) {
      alert('Token limit reached. Please enter a new API key to continue with unlimited usage.')
      return
    }

    setClickedOptions(prev => new Set(prev).add(option))

    const userMessage: ChatMessage = { role: 'user', content: `Tell me about ${option} in ${city}` }
    setMessages((prev) => [...prev, userMessage])
    setIsLoading(true)

    try {
      const response = await callGemini([
        ...messages,
        { role: 'user', content: `Tell me about ${option} in ${city}` }
      ], 100, apiKey || GEMINI_API_KEY);
      if (response) {
        const assistantMessage: ChatMessage = { role: 'assistant', content: response }
        setMessages((prev) => [...prev, assistantMessage])
        if (!isUnlimited) {
          const newTokens = estimateTokenCount(userMessage.content) + estimateTokenCount(response)
          await updateTokenCount(newTokens)
        }
      }
    } catch (error) {
      console.error('Error:', error)
      const errorMessage = error instanceof Error ? error.message : 'An unknown error occurred'
      setMessages((prev) => [...prev, { role: 'assistant', content: `Sorry, I encountered an error: ${errorMessage}` }])
    } finally {
      setIsLoading(false)
    }
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if ((!input.trim() && !apiKey) || (isLimitReached && !apiKey && !isUnlimited)) return

    if (isLimitReached && apiKey) {
      setApiKey(apiKey)
      setIsUnlimited(true)
      setIsLimitReached(false)
      setTokenCount(0)
      return
    }

    const userMessage: ChatMessage = { role: 'user', content: input }
    setMessages((prev) => [...prev, userMessage])
    setInput('')
    setIsLoading(true)

    try {
      const response = await callGemini([
        ...messages,
        { role: 'user', content: input }
      ], 100, apiKey || GEMINI_API_KEY);
      if (response) {
        const assistantMessage: ChatMessage = { role: 'assistant', content: response }
        setMessages((prev) => [...prev, assistantMessage])
        if (!isUnlimited) {
          const newTokens = estimateTokenCount(userMessage.content) + estimateTokenCount(response)
          await updateTokenCount(newTokens)
        }
      }
    } catch (error) {
      console.error('Error:', error)
      const errorMessage = error instanceof Error ? error.message : 'An unknown error occurred'
      setMessages((prev) => [...prev, { role: 'assistant', content: `Sorry, I encountered an error: ${errorMessage}` }])
    } finally {
      setIsLoading(false)
    }
  }

  const updateTokenCount = async (newTokens: number) => {
    if (isUnlimited) return
    const response = await fetch('/api/token-limit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ tokens: newTokens }),
    })
    const data = await response.json()
    setTokenCount(data.tokenCount)
  }

  return (
    <div className="flex flex-col h-[500px] border rounded-lg overflow-hidden">
      <ScrollArea className="flex-grow p-4">
        {messages.slice(1).map((message, index) => (
          <div
            key={index}
            className={`mb-4 ${
              message.role === 'user' ? 'text-right' : 'text-left'
            }`}
          >
            <span
              className={`inline-block p-2 rounded-lg ${
                message.role === 'user'
                  ? 'bg-blue-500 text-white'
                  : 'bg-gray-200 text-gray-800'
              }`}
            >
              {message.content}
            </span>
          </div>
        ))}
      </ScrollArea>
      <div className="p-4 border-t">
        {!isUnlimited && (
          <div className="mb-2 flex justify-between items-center">
            <span className="text-sm text-gray-500">
              Tokens used: {tokenCount}/{MAX_TOKENS}
            </span>
            <Progress value={(tokenCount / MAX_TOKENS) * 100} className="w-1/2" />
          </div>
        )}
        {isUnlimited && (
          <div className="mb-2 text-center">
            <span className="text-sm text-green-500 font-semibold">Unlimited usage enabled</span>
          </div>
        )}
        <div className="flex flex-wrap gap-2 justify-center mb-4">
          {travelOptions.filter(option => !clickedOptions.has(option)).map((option) => (
            <Button
              key={option}
              variant="outline"
              size="sm"
              onClick={() => handleOptionClick(option)}
              disabled={isLoading || (isLimitReached && !apiKey && !isUnlimited)}
            >
              {option}
            </Button>
          ))}
        </div>
        <form onSubmit={handleSubmit} className="flex gap-2">
          {isLimitReached && !apiKey && !isUnlimited ? (
            <Input
              type="text"
              value={apiKey}
              onChange={(e) => setApiKey(e.target.value)}
              placeholder="Enter your Gemini API key for unlimited usage"
              className="flex-grow"
            />
          ) : (
            <Input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder={`Ask about ${city}...`}
              disabled={isLoading}
              className="flex-grow"
            />
          )}
          <Button type="submit" disabled={isLoading || (isLimitReached && !apiKey && !isUnlimited)}>
            {isLimitReached && !apiKey && !isUnlimited ? 'Set API Key' : (isLoading ? 'Sending...' : 'Send')}
          </Button>
        </form>
      </div>
    </div>
  )
}

