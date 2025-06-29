import Link from 'next/link'
import { Globe } from 'lucide-react'

export function Footer() {
  return (
    <footer className="bg-gray-100 py-12">
      <div className="container mx-auto px-4">
        <div className="flex flex-col md:flex-row justify-between items-center">
          <div className="flex items-center gap-2 mb-4 md:mb-0">
            <Globe className="h-6 w-6" />
            <span className="text-lg font-bold">NomadHub</span>
          </div>
          <nav className="flex flex-wrap justify-center gap-6">
            <Link href="#" className="text-sm text-gray-600 hover:text-gray-900">
              About Us
            </Link>
            <Link href="#" className="text-sm text-gray-600 hover:text-gray-900">
              Blog
            </Link>
            <Link href="#" className="text-sm text-gray-600 hover:text-gray-900">
              Privacy Policy
            </Link>
            <Link href="#" className="text-sm text-gray-600 hover:text-gray-900">
              Terms of Service
            </Link>
            <Link href="#" className="text-sm text-gray-600 hover:text-gray-900">
              Contact
            </Link>
          </nav>
        </div>
        <div className="mt-8 text-center text-sm text-gray-600">
          © {new Date().getFullYear()} NomadHub. All rights reserved.
        </div>
      </div>
    </footer>
  )
}

