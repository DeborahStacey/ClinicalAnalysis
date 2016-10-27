import unittest
import socket
import sys






class TestStringMethods(unittest.TestCase):

    host = '104.196.166.63'        # IP of the server
    port = 12345                   # The same port as used by the server


    # Test incorrect JSON
    def test_formatting(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TestStringMethods.host, TestStringMethods.port))
        s.sendall("hello".encode('utf-8'))
        data = s.recv(1024)
        s.close()

        self.assertEqual(data.decode('utf-8'), "Not valid json request, please check formatting")

    # Test incorrect JSON
    def test_missing_operation_key(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TestStringMethods.host, TestStringMethods.port))
        s.sendall('{"animals":"all","fields":"weight"}'.encode('utf-8'))
        data = s.recv(1024)
        s.close()

        self.assertEqual(data.decode('utf-8'), "Invalid json request, missing key: operation")

    # Test incorrect JSON
    def test_missing_animal_key(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TestStringMethods.host, TestStringMethods.port))
        s.sendall('{"operation":"lookup","fields":"weight"}'.encode('utf-8'))
        data = s.recv(1024)
        s.close()

        self.assertEqual(data.decode('utf-8'), "Invalid json request, missing key: animals")

    # Test incorrect JSON
    def test_missing_field_key(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TestStringMethods.host, TestStringMethods.port))
        s.sendall('{"operation":"lookup","animals":"all"}'.encode('utf-8'))
        data = s.recv(1024)
        s.close()

        self.assertEqual(data.decode('utf-8'), "Invalid json request, missing key: field")

    # Test incorrect JSON
    def test_correct_query(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TestStringMethods.host, TestStringMethods.port))
        s.sendall('{"operation":"lookup","animals":"all","fields":"weight"}'.encode('utf-8'))
        data = s.recv(1024)
        s.close()

        self.assertEqual(data.decode('utf-8'), "Not valid json request, please check formatting")





if __name__ == '__main__':
    unittest.main()
