# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BookStore.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x42ookStore.proto\x12\tBookStore\"\xa6\x02\n\x04\x42ook\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05title\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x06\x61uthor\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x12\n\x05price\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x16\n\tpublisher\x18\x06 \x01(\tH\x05\x88\x01\x01\x12\x1b\n\x0epublished_date\x18\x07 \x01(\tH\x06\x88\x01\x01\x12\x19\n\x0cupdated_date\x18\x08 \x01(\tH\x07\x88\x01\x01\x42\x05\n\x03_idB\x08\n\x06_titleB\t\n\x07_authorB\x0e\n\x0c_descriptionB\x08\n\x06_priceB\x0c\n\n_publisherB\x11\n\x0f_published_dateB\x0f\n\r_updated_date\"\x10\n\x0eGetBookRequest\"1\n\x0fGetBookResponse\x12\x1e\n\x05\x62ooks\x18\x01 \x03(\x0b\x32\x0f.BookStore.Book\",\n\x12GetBookByIdRequest\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x05\n\x03_id\"4\n\x13GetBookByIdResponse\x12\x1d\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x0f.BookStore.Book\"=\n\x0e\x41\x64\x64\x42ookRequest\x12\"\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x0f.BookStore.BookH\x00\x88\x01\x01\x42\x07\n\x05_book\")\n\x0f\x41\x64\x64\x42ookResponse\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x05\n\x03_id\"@\n\x11UpdateBookRequest\x12\"\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x0f.BookStore.BookH\x00\x88\x01\x01\x42\x07\n\x05_book\",\n\x12UpdateBookResponse\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x05\n\x03_id\"+\n\x11\x44\x65leteBookRequest\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x05\n\x03_id\",\n\x12\x44\x65leteBookResponse\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x05\n\x03_id2\xf9\x02\n\x05\x42ooks\x12\x42\n\x07GetBook\x12\x19.BookStore.GetBookRequest\x1a\x1a.BookStore.GetBookResponse\"\x00\x12N\n\x0bGetBookById\x12\x1d.BookStore.GetBookByIdRequest\x1a\x1e.BookStore.GetBookByIdResponse\"\x00\x12\x42\n\x07\x41\x64\x64\x42ook\x12\x19.BookStore.AddBookRequest\x1a\x1a.BookStore.AddBookResponse\"\x00\x12K\n\nUpdateBook\x12\x1c.BookStore.UpdateBookRequest\x1a\x1d.BookStore.UpdateBookResponse\"\x00\x12K\n\nDeleteBook\x12\x1c.BookStore.DeleteBookRequest\x1a\x1d.BookStore.DeleteBookResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'BookStore_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_BOOK']._serialized_start=31
  _globals['_BOOK']._serialized_end=325
  _globals['_GETBOOKREQUEST']._serialized_start=327
  _globals['_GETBOOKREQUEST']._serialized_end=343
  _globals['_GETBOOKRESPONSE']._serialized_start=345
  _globals['_GETBOOKRESPONSE']._serialized_end=394
  _globals['_GETBOOKBYIDREQUEST']._serialized_start=396
  _globals['_GETBOOKBYIDREQUEST']._serialized_end=440
  _globals['_GETBOOKBYIDRESPONSE']._serialized_start=442
  _globals['_GETBOOKBYIDRESPONSE']._serialized_end=494
  _globals['_ADDBOOKREQUEST']._serialized_start=496
  _globals['_ADDBOOKREQUEST']._serialized_end=557
  _globals['_ADDBOOKRESPONSE']._serialized_start=559
  _globals['_ADDBOOKRESPONSE']._serialized_end=600
  _globals['_UPDATEBOOKREQUEST']._serialized_start=602
  _globals['_UPDATEBOOKREQUEST']._serialized_end=666
  _globals['_UPDATEBOOKRESPONSE']._serialized_start=668
  _globals['_UPDATEBOOKRESPONSE']._serialized_end=712
  _globals['_DELETEBOOKREQUEST']._serialized_start=714
  _globals['_DELETEBOOKREQUEST']._serialized_end=757
  _globals['_DELETEBOOKRESPONSE']._serialized_start=759
  _globals['_DELETEBOOKRESPONSE']._serialized_end=803
  _globals['_BOOKS']._serialized_start=806
  _globals['_BOOKS']._serialized_end=1183
# @@protoc_insertion_point(module_scope)