'use client'

import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { createClient } from '@supabase/supabase-js'
import { createClientComponentClient } from '@supabase/auth-helpers-nextjs'
import { Github, Twitter } from 'lucide-react'

export function SocialLogin() {
  const [isLoading, setIsLoading] = useState(false)
  // const supabase = createClientComponentClient()
  const supabase = createClient(
    'https://your-project-url.supabase.co',
    'your-anon-key'
  )

  const handleSocialLogin = async (provider: 'github' | 'twitter') => {
    try {
      setIsLoading(true)
      const { error } = await supabase.auth.signInWithOAuth({
        provider: provider,
        options: {
          redirectTo: `${window.location.origin}/auth/callback`,
        },
      })
      if (error) throw error
    } catch (error) {
      console.error('Error:', error)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="flex flex-col gap-4">
      <Button
        variant="outline"
        onClick={() => handleSocialLogin('github')}
        disabled={isLoading}
      >
        <Github className="mr-2 h-4 w-4" />
        Sign in with GitHub
      </Button>
      <Button
        variant="outline"
        onClick={() => handleSocialLogin('twitter')}
        disabled={isLoading}
      >
        <Twitter className="mr-2 h-4 w-4" />
        Sign in with Twitter
      </Button>
    </div>
  )
}

