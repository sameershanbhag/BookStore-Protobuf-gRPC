"""The Python implementation of the GRPC BookStore.Books server."""
import json
from concurrent import futures
import logging

import grpc
import BookStore_pb2
import BookStore_pb2_grpc


class BookStore(BookStore_pb2_grpc.BooksServicer):

    def AddBook(self, request, context):
        """
        Adds a book to the database
        """
        # Load the database
        data_file = open("data.json", "r")
        database = json.load(data_file)

        # Close the data file and clear contents
        data_file.close()
        open("data.json", "w").close()

        # check if the book already exists
        for current_book in database['books']:
            if current_book['id'] == request.book.id:
                return BookStore_pb2.AddBookResponse(id="Book already exists")

        # Open the data file again and write the new data
        with open("data.json", "r+") as f:
            data = {
                "id": request.book.id,
                "title": request.book.title,
                "author": request.book.author,
                "price": request.book.price,
            }
            database['books'].append(data)
            json.dump(database, f)
        f.close()
        return BookStore_pb2.AddBookResponse(id=request.book.id)

    def GetBook(self, request, context):
        """
        Returns all the books in the database
        """
        with open("data.json", "r") as f:
            database = json.load(f)
            f.close()
            return BookStore_pb2.GetBookResponse(
                books=[
                    BookStore_pb2.Book(id=current_book['id'],
                                       title=current_book['title'],
                                       author=current_book['author'],
                                       price=current_book['price'])
                    for current_book in database['books']
                ]
            )

    def GetBookById(self, request, context):
        """
        Returns a book by id
        """
        with open("data.json", "r") as f:
            database = json.load(f)
            f.close()
            for current_book in database['books']:
                if current_book['id'] == request.id:
                    return BookStore_pb2.GetBookByIdResponse(
                        book=BookStore_pb2.Book(
                            id=current_book['id'],
                            title=current_book['title'],
                            author=current_book['author'],
                            price=current_book['price']
                        )
                    )
            return BookStore_pb2.GetBookByIdResponse(book=BookStore_pb2.Book(id="Book not found"))

    def UpdateBook(self, request, context):
        """
        Updates a book by id
        """
        with open("data.json", "r") as f:
            database = json.load(f)
            f.close()
            for current_book in database['books']:
                if current_book['id'] == request.book.id:
                    current_book['title'] = request.book.title
                    current_book['author'] = request.book.author
                    current_book['price'] = request.book.price
                    with open("data.json", "w") as f:
                        json.dump(database, f)
                    f.close()
                    return BookStore_pb2.UpdateBookResponse(id=request.book.id)
            return BookStore_pb2.UpdateBookResponse(id="Book not found")

    def DeleteBook(self, request, context):
        """
        Deletes a book by id
        """
        with open("data.json", "r") as f:
            database = json.load(f)
            f.close()
            for current_book in database['books']:
                if current_book['id'] == request.id:
                    database['books'].remove(current_book)
                    with open("data.json", "w") as f:
                        json.dump(database, f)
                    f.close()
                    return BookStore_pb2.DeleteBookResponse(id=request.id)
            return BookStore_pb2.DeleteBookResponse(id="Book not found")


def serve():
    # Open a Json file to store the data
    books_store = open("data.json", "w")
    books_store.write('{"books": []}')
    books_store.close()

    # Specify the port to listen to
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    BookStore_pb2_grpc.add_BooksServicer_to_server(BookStore(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
