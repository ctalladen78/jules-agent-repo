import { NextResponse } from 'next/server'

const MAX_TOKENS = 100
const RESET_INTERVAL = 10 * 60 * 1000 // 10 minutes in milliseconds

let tokenCounts: { [key: string]: { count: number; lastReset: number } } = {}

export async function GET(request: Request) {
  const ip = request.headers.get('x-forwarded-for') || 'unknown'
  const now = Date.now()

  if (!tokenCounts[ip] || now - tokenCounts[ip].lastReset > RESET_INTERVAL) {
    tokenCounts[ip] = { count: 0, lastReset: now }
  }

  return NextResponse.json({
    tokenCount: tokenCounts[ip].count,
    isLimitReached: tokenCounts[ip].count >= MAX_TOKENS,
  })
}

export async function POST(request: Request) {
  const ip = request.headers.get('x-forwarded-for') || 'unknown'
  const { tokens } = await request.json()

  if (!tokenCounts[ip]) {
    tokenCounts[ip] = { count: 0, lastReset: Date.now() }
  }

  tokenCounts[ip].count += tokens

  return NextResponse.json({
    tokenCount: tokenCounts[ip].count,
    isLimitReached: tokenCounts[ip].count >= MAX_TOKENS,
  })
}

