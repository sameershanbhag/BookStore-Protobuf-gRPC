"""The Python implementation of the GRPC BookStore.Books client."""
from __future__ import print_function

import logging

import grpc
import BookStore_pb2
import BookStore_pb2_grpc


def run():
    print("Lets try to add a book ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = BookStore_pb2_grpc.BooksStub(channel)
        # Adding all the books from the CSV File
        with open("books_data.csv", "r") as f:
            for line in f.readlines()[1:]:
                book = line.strip().split(",")
                response_add = stub.AddBook(
                    BookStore_pb2.AddBookRequest(
                        book=BookStore_pb2.Book(
                            id=book[0],
                            title=book[1],
                            author=book[2],
                            price=book[3],
                        )
                    )
                )
                print(response_add.id)
        f.close()

        print("Lets try to get all books ...")
        response_get = stub.GetBook(BookStore_pb2.GetBookRequest())

        print(response_get.books)

        response_get_by_id = stub.GetBookById(BookStore_pb2.GetBookByIdRequest(id="1"))

        print(response_get_by_id.book)

        response_update = stub.UpdateBook(
            BookStore_pb2.UpdateBookRequest(book=
                                            BookStore_pb2.Book(id="1",
                                                               title="Updated Book",
                                                               author="Updated Author",
                                                               price="500$")
                                            )
        )

        print(response_update.id)

        response_delete = stub.DeleteBook(BookStore_pb2.DeleteBookRequest(id="1"))

        print(response_delete.id)


if __name__ == "__main__":
    logging.basicConfig()
    run()
