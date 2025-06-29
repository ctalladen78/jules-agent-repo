import { notFound } from 'next/navigation'
import { cities, getCitySummary } from '@/utils/cityData'
import { Chat } from '@/components/chat'
import { Header } from '@/components/header'
import { Footer } from '@/components/footer'

export function generateStaticParams() {
  return cities.map((city) => ({ name: city.toLowerCase().replace(/ /g, '-') }))
}

export default function CityPage({ params }: { params: { name: string } }) {
  const cityName = params.name.replace(/-/g, ' ').replace(/\b\w/g, (l) => l.toUpperCase())
  
  if (!cities.includes(cityName)) {
    notFound()
  }

  const summary = getCitySummary(cityName)

  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="flex-grow">
        <div className="container mx-auto px-4 py-8">
          <h1 className="text-4xl font-bold mb-6">{cityName}</h1>
          <p className="text-xl mb-8">{summary}</p>
          <h2 className="text-2xl font-semibold mb-4">Chat about {cityName}</h2>
          <Chat city={cityName} />
        </div>
      </main>
      <Footer />
    </div>
  )
}

