import unittest
import socket
import json
import sys
import QueryBuilder

class TestStringMethods(unittest.TestCase):

    host = '104.196.166.63'        # IP of the server
    port = 12345                   # The same port as used by the server


    # Test incorrect JSON
    def test_formatting(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TestStringMethods.host, TestStringMethods.port))
        s.sendall("hello".encode('utf-8'))
        data = json.loads(s.recv(1024).decode('utf-8'))
        s.close()

        self.assertEqual(data['code'], 1)

    # Test missing operation key
    def test_missing_operation_key(self):

      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((TestStringMethods.host, TestStringMethods.port))
      s.sendall('{"animals":"all","fields":"weight"}'.encode('utf-8'))
      data = json.loads(s.recv(1024).decode('utf-8'))
      s.close()

      self.assertEqual(data['code'], 10)

    # Test missing animal key
    def test_missing_animal_key(self):

      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((TestStringMethods.host, TestStringMethods.port))
      s.sendall('{"operation":"lookup","fields":"weight"}'.encode('utf-8'))
      data = json.loads(s.recv(1024).decode('utf-8'))
      s.close()

      self.assertEqual(data['code'], 11)

    # Test missing field key
    def test_missing_field_key(self):

      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((TestStringMethods.host, TestStringMethods.port))
      s.sendall('{"operation":"lookup","animals":"all"}'.encode('utf-8'))
      data = json.loads(s.recv(1024).decode('utf-8'))
      s.close()

      self.assertEqual(data['code'], 12)

    def test_query_builder_simple(self):
      queryList = []
      queryList.append(["$and","age","eq",5])
      queryList.append(["$and","weight","lt",20])
      query = QueryBuilder.build_query(queryList)
      self.assertEqual(query,'(age=5 AND weight<20)')

    def test_query_builder_complex(self):
      queryList = []
      queryList.append(["$and","age","eq",5])
      queryList.append(["$and","weight","lt",20])
      queryList.append(["$or","name","eq",'bob'])
      queryList.append(["$and","region","eq",'Ontario'])
      query = QueryBuilder.build_query(queryList)
      self.assertEqual(query,'((age=5 AND weight<20) OR (name="bob" AND region="Ontario"))')

    def test_query_builder_complex_2(self):
      queryList = []
      queryList.append(["$or","age","eq",5])
      queryList.append(["$or","weight","lt",20])
      query = QueryBuilder.build_query(queryList)
      self.assertEqual(query,'(age=5 OR weight<20)')





if __name__ == '__main__':
    unittest.main()
