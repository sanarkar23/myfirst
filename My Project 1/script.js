const facts = [
  "Honey never spoils.",
  "Bananas are berries, but strawberries aren't.",
  "Octopuses have three hearts.",
  "There are more stars in the universe than grains of sand on Earth.",
  "A group of flamingos is called a flamboyance."
];

function generateFact() {
  const randomIndex = Math.floor(Math.random() * facts.length);
  document.getElementById("fact").textContent = facts[randomIndex];
}