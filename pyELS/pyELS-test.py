# coding:utf-8

from mapping import MappingELS
from write import RegisterELS
from read import ReadELS

def test_mapping(index, host, port):
	ins_map = MappingELS(index=index, host=host, port=port)

def test_write(index, host, port, doc_type)
	ins_write = RegisterELS(index=index, host=host, port=port, doc_type=doc_type)

def test_read(index, host, port, doc_type):
	ins_read = ReadELS(index=index, host=host, port=port, doc_type=doc_type)

def main():
	# init
	index = "test"
	host = "localhost"
	port = "8888"
	doc_type = "test-type"
	
	# test
	test_mapping(index=index, host=host, port=port)
	test_write(index=index, host=host, port=port, doc_type=doc_type)
	test_read(index=index, host=host, port=port, doc_type=doc_type)

if __name__ == '__main__':
	main()