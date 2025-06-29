import { Header } from '@/components/header'
import { Hero } from '@/components/hero'
import { NomadUtilities } from '@/components/nomad-utilities'
import { Footer } from '@/components/footer'
import { cities } from '@/utils/cityData'
import { TravelRecommendations } from '@/components/travel-recommendations'
import Link from 'next/link'
import { Button } from '@/components/ui/button'

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="flex-grow">
        <Hero />
        <section className="py-12 px-4">
          <div className="container mx-auto">
            <h2 className="text-3xl font-bold text-center mb-8">Explore Popular Nomad Destinations</h2>
            <div className="flex flex-wrap justify-center gap-4">
              {cities.map((city) => (
                <Link key={city} href={`/city/${city.toLowerCase().replace(/ /g, '-')}`}>
                  <Button variant="outline" size="lg">
                    {city}
                  </Button>
                </Link>
              ))}
            </div>
          </div>
        </section>
        <NomadUtilities />
        <TravelRecommendations />
      </main>
      <Footer />
    </div>
  )
}

