'use client'

import React, { createContext, useContext, useState, useEffect } from 'react'

interface TokenLimitContextType {
  tokenCount: number
  setTokenCount: React.Dispatch<React.SetStateAction<number>>
  isLimitReached: boolean
  setIsLimitReached: React.Dispatch<React.SetStateAction<boolean>>
}

const TokenLimitContext = createContext<TokenLimitContextType | undefined>(undefined)

export const useTokenLimit = () => {
  const context = useContext(TokenLimitContext)
  if (!context) {
    throw new Error('useTokenLimit must be used within a TokenLimitProvider')
  }
  return context
}

export const TokenLimitProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [tokenCount, setTokenCount] = useState(0)
  const [isLimitReached, setIsLimitReached] = useState(false)

  useEffect(() => {
    const checkTokenLimit = async () => {
      const response = await fetch('/api/token-limit')
      const data = await response.json()
      setTokenCount(data.tokenCount)
      setIsLimitReached(data.isLimitReached)
    }

    checkTokenLimit()
    const interval = setInterval(checkTokenLimit, 60000) // Check every minute

    return () => clearInterval(interval)
  }, [])

  return (
    <TokenLimitContext.Provider value={{ tokenCount, setTokenCount, isLimitReached, setIsLimitReached }}>
      {children}
    </TokenLimitContext.Provider>
  )
}

