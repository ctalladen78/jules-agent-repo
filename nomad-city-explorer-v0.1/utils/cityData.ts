export const cities = [
  "New York",
  "London",
  "Tokyo",
  "Paris",
  "Sydney",
  "Berlin",
  "Rome",
  "Amsterdam",
  "Barcelona",
  "Singapore"
];

export const getCitySummary = (city: string) => {
  const summaries: { [key: string]: string } = {
    "New York": "The Big Apple, known for its iconic skyline and diverse culture.",
    "London": "A historic city blending tradition with modern innovation.",
    "Tokyo": "A bustling metropolis where cutting-edge technology meets ancient traditions.",
    "Paris": "The City of Light, famous for its art, fashion, and cuisine.",
    "Sydney": "A vibrant coastal city known for its stunning harbor and beaches.",
    "Berlin": "A city with a rich history and thriving arts scene.",
    "Rome": "The Eternal City, home to ancient ruins and world-class cuisine.",
    "Amsterdam": "Known for its picturesque canals and progressive attitude.",
    "Barcelona": "A city celebrated for its unique architecture and Mediterranean lifestyle.",
    "Singapore": "A global financial hub with a mix of cultures and futuristic gardens."
  };

  return summaries[city] || "City information not available.";
};

