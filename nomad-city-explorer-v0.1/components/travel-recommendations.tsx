'use client'

import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { callGemini } from '@/utils/gemini'

export function TravelRecommendations() {
  const [query, setQuery] = useState('')
  const [recommendation, setRecommendation] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsLoading(true)
    try {
      const result = await callGemini([
        { role: 'system', content: 'You are a travel recommendation assistant.' },
        { role: 'user', content: query }
      ])
      setRecommendation(result)
    } catch (error) {
      console.error('Error:', error)
      setRecommendation('Sorry, there was an error processing your request.')
    }
    setIsLoading(false)
  }

  return (
    <section className="py-12 px-4 bg-gray-100">
      <div className="container mx-auto">
        <h2 className="text-3xl font-bold text-center mb-8">Get Travel Recommendations</h2>
        <form onSubmit={handleSubmit} className="max-w-xl mx-auto">
          <div className="flex gap-4">
            <Input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Ask for travel recommendations..."
              className="flex-grow"
            />
            <Button type="submit" disabled={isLoading}>
              {isLoading ? 'Loading...' : 'Get Recommendations'}
            </Button>
          </div>
        </form>
        {recommendation && (
          <div className="mt-8 p-4 bg-white rounded-lg shadow">
            <h3 className="text-xl font-semibold mb-2">Recommendation:</h3>
            <p>{recommendation}</p>
          </div>
        )}
      </div>
    </section>
  )
}

