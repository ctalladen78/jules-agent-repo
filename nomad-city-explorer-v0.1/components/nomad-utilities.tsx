import Link from 'next/link'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Wifi, Umbrella, Briefcase, Users, CreditCard, Plane } from 'lucide-react'

const utilities = [
  {
    title: 'WiFi Speeds',
    description: 'Find cities with the fastest internet connections.',
    icon: Wifi,
    link: '/city/singapore',
  },
  {
    title: 'Cost of Living',
    description: 'Compare expenses in different nomad-friendly locations.',
    icon: CreditCard,
    link: '/city/berlin',
  },
  {
    title: 'Weather',
    description: 'Check climate data for your potential destinations.',
    icon: Umbrella,
    link: '/city/barcelona',
  },
  {
    title: 'Coworking Spaces',
    description: 'Discover the best places to work and network.',
    icon: Briefcase,
    link: '/city/new-york',
  },
  {
    title: 'Nomad Community',
    description: 'Connect with other digital nomads in your area.',
    icon: Users,
    link: '/city/amsterdam',
  },
  {
    title: 'Travel Deals',
    description: 'Find the best flights and accommodation offers.',
    icon: Plane,
    link: '/city/tokyo',
  },
]

export function NomadUtilities() {
  return (
    <section className="py-24 px-4">
      <h2 className="text-3xl font-bold text-center mb-12">Nomad Essentials</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto">
        {utilities.map((utility, index) => (
          <Link key={index} href={utility.link}>
            <Card className="h-full hover:shadow-lg transition-shadow">
              <CardHeader>
                <utility.icon className="h-8 w-8 mb-2 text-purple-500" />
                <CardTitle>{utility.title}</CardTitle>
              </CardHeader>
              <CardContent>
                <CardDescription>{utility.description}</CardDescription>
              </CardContent>
            </Card>
          </Link>
        ))}
      </div>
    </section>
  )
}

