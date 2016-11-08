import unittest
import socket
import json
import sys
import standards
import jsonToSqlParms

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

    def test_jsonToSqlParms_simple(self):
        json = '{"operation": "operation-here", "animals": "animal-here", "field": [{"age":{"gt":5}}]}'
        sql = jsonToSqlParms.JsonToSqlParms(json)
        self.assertEqual(sql, '(age > 5)')

    def test_jsonToSqlParms_simple_2(self):
        json = '{"operation": "operation-here", "animals": "animal-here", "field": [{ "$and": [{"length" : {"lt" : 20} }, {"$or": [{"height": {"lt": 20}}, [{"age":{"eq":10}}]]}, {"$or": [{"height": {"lt": 20}}]}]}]}';
        sql = jsonToSqlParms.JsonToSqlParms(json)
        self.assertEqual(sql, '((length < 20 and (height < 20 or (age = 10)) and (height < 20)))')

    def test_jsonToSqlParms_nested(self):
        json = '{"operation": "operation-here", "animals": "animal-here", "field": [{ "$and": [{ "age": { "eq": 5 } }, { "weight": { "lt": 20 } }, { "$or": [{ "height": { "eq": 20 } }, { "length": { "eq": 20 } } ] } ] }]}'
        sql = jsonToSqlParms.JsonToSqlParms(json)
        self.assertEqual(sql, '((age = 5 and weight < 20 and (height = 20 or length = 20)))')

    def test_jsonToSqlParms_complex(self):
        json = '{"operation": "operation-here", "animals": "animal-here", "field": [{ "$and": [{ "age": { "eq": 5 } }, { "weight": { "lt": 20 } }, { "$or": [{ "height": { "eq": 20 } }, { "length": { "eq": 20 } }] }, { "$or": [{ "height": { "eq": 20 } }, { "length": { "eq": 20 } }] }] }]}'
        sql = jsonToSqlParms.JsonToSqlParms(json)
        self.assertEqual(sql, '((age = 5 and weight < 20 and (height = 20 or length = 20) and (height = 20 or length = 20)))')

    def test_jsonToSqlParms_complex_2(self):
        json = '{"operation": "lookup", "animals": "cat", "field": [{ "$or": [{ "age": { "eq": 5 } }, { "weight": { "lt": 20 } }, { "$or": [{ "height": { "eq": 20 } }, { "length": { "eq": 20 } }] }, { "$or": [{ "height": { "eq": 20 } }, { "length": { "eq": 20 } }] }] }]}'
        sql = jsonToSqlParms.JsonToSqlParms(json)
        self.assertEqual(sql, '((age = 5 or weight < 20 or (height = 20 or length = 20) or (height = 20 or length = 20)))')

    def test_jsonToSqlParms_complex_3(self):
        json = '{"operation": "lookup", "animals": "cat", "field": [{ "$or": [{ "age": { "eq": 5 } }, { "weight": { "lt": 20 } }, { "$and": [{ "height": { "eq": 20 } }, { "length": { "eq": 20 } }] }, { "$and": [{ "height": { "eq": 20 } }, { "length": { "eq": 20 } }] }] }]}'
        sql = jsonToSqlParms.JsonToSqlParms(json)
        self.assertEqual(sql, '((age = 5 or weight < 20 or (height = 20 and length = 20) or (height = 20 and length = 20)))')

    def test_jsonToSqlParms_complex_4(self):
        json = '{"operation":"lookup","animals":"cat","field":[{"$or":[{"age":{"eq":"5"}}],"$and":[{"height":{"lt":"50"},"weight":{"gt":"500"},"age":{"eq":"100"},"$or":[{"butts":{"eq":"1"},"diabetes":{"ne":"true"},"$and":[{"dob":{"eq":"1998"},"dod":{"eq":"1999"},"$or":{"tail":{"ne":"false"},"color":{"eq":"orange"}}}]}]}]}]}'
        sql = jsonToSqlParms.JsonToSqlParm(json)
        self.assertEqual(sql, '')

if __name__ == '__main__':
    unittest.main()
