from queries import Queries
slideshows = Queries("berkeleyhacks", "test.pdf")["flashcards"]("Agents")

print(slideshows)
