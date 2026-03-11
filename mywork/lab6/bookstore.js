// Task 2: use database
/*
use bookstore
*/

// Task 3: insert first author
db.authors.insertOne({
  "name": "Jane Austen",
  "nationality": "British",
  "bio": {
    "short": "English novelist known for novels about the British landed gentry.",
    "long": "Jane Austen was an English novelist whose works critique and comment upon the British landed gentry at the end of the 18th century. Her most famous novels include Pride and Prejudice, Sense and Sensibility, and Emma, celebrated for their wit, social commentary, and masterful character development."
  }
})

// Task 4: update to add birthday
db.authors.updateOne(
    { "name": "Jane Austen" },
    { $set: { "birthday": "1775-12-16" } }
    )

// Task 5: insert four more authors
db.authors.insertOne({
    "name": "Stephenie Meyer",
    "nationality": "American",
    "bio": {
    "short": "American author known for writing the Twilight series.",
    "long": "Stephenie Meyer is an American writer who is most famous for the Twilight series. The books became very popular around the world and were later turned into movies. Her stories are known for combining romance, fantasy, and drama."
    },
    "birthday": "1973-12-24"
    })
db.authors.insertOne({
    "name": "Julia Quinn",
    "nationality": "American",
    "bio": {
    "short": "American author known for historical romance books like The Duke and I.",
    "long": "Julia Quinn is an American writer who is well known for her historical romance novels. One of her most famous books is The Duke and I, which is part of the Bridgerton series. Her books became even more popular after the Netflix show was released."
    },
    "birthday": "1970-01-12"
    })

db.authors.insertOne({
    "name": "Elizabeth Acevedo",
    "nationality": "American",
    "bio": {
    "short": "American poet and author known for The Poet X.",
    "long": "Elizabeth Acevedo is an American writer and poet. She is best known for The Poet X, a novel written in verse. Her work often talks about identity, family, culture, and finding your own voice."
    },
    "birthday": "1988-02-15"
    })
db.authors.insertOne({
    "name": "Marcus Pfister",
    "nationality": "Swiss",
    "bio": {
    "short": "Swiss author and illustrator known for The Rainbow Fish.",
    "long": "Marcus Pfister is a Swiss writer and illustrator of children's books. He is best known for The Rainbow Fish, a popular picture book about sharing and kindness. The book is also known for its shiny and colorful illustrations."
    },
    "birthday": "1960-07-30"
    })


// Task 6: total count
db.authors.countDocuments()

// Task 7: British authors, sorted by name
db.authors.find({ "nationality": "British" }).sort({ "name": 1 })
