import Link from 'next/link'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Globe, Menu } from 'lucide-react'
import { SocialLogin } from '@/components/social-login'

export function Header() {
  return (
    <header className="bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container flex h-16 items-center justify-between">
        <Link href="/" className="flex items-center gap-2">
          <Globe className="h-6 w-6" />
          <span className="text-lg font-bold">NomadHub</span>
        </Link>
        <nav className="hidden md:flex items-center gap-6">
          <Link href="/" className="text-sm font-medium hover:underline">
            Home
          </Link>
          <Link href="#" className="text-sm font-medium hover:underline">
            Destinations
          </Link>
          <Link href="#" className="text-sm font-medium hover:underline">
            Community
          </Link>
          <Link href="#" className="text-sm font-medium hover:underline">
            Resources
          </Link>
          <Link href="#" className="text-sm font-medium hover:underline">
            Jobs
          </Link>
        </nav>
        <div className="flex items-center gap-4">
          <SocialLogin />
          <Button variant="ghost" size="icon" className="md:hidden">
            <Menu className="h-6 w-6" />
            <span className="sr-only">Toggle menu</span>
          </Button>
        </div>
      </div>
    </header>
  )
}

