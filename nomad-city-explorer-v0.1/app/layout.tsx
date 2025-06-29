import './globals.css'
import { Inter } from 'next/font/google'
import { TokenLimitProvider } from '@/contexts/TokenLimitContext'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'NomadHub',
  description: 'Find your perfect nomad destination',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  // Check if environment variables are loaded
  if (!process.env.NEXT_PUBLIC_GEMINI_API_KEY) {
    console.error('NEXT_PUBLIC_GEMINI_API_KEY is not set. Please check your environment variables.');
  }
  if (!process.env.NEXT_PUBLIC_OPENAI_API_KEY) {
    console.error('NEXT_PUBLIC_OPENAI_API_KEY is not set. Please check your environment variables.');
  }

  return (
    <html lang="en">
      <body className={inter.className}>
        <TokenLimitProvider>
          {children}
        </TokenLimitProvider>
      </body>
    </html>
  )
}

