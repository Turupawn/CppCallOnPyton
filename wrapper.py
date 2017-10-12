from ctypes import *
lib = cdll.LoadLibrary('./libfoo.so')

#Char* instead of string params

print "== String params =="

lib.stringParam("this is a test")

#Array and an int instead of vectors

print "== Vector params =="

N = 3
array = (c_int*N)()
array[0] = 10
array[1] = 20
array[2] = 30

lib.vectorParam(array, 3)

#Structs instead of class

print "== Class params =="

class TestStruct(Structure):
    _fields_ = [("int_test", c_int),("string_test", c_char_p)]

test_struct = TestStruct(100, "hello")

lib.structParam(test_struct)

# C style callbacks instead of C++ callbacks

print "== Callback params =="

def callback_function_test(int_param, string_param, test_struct):
   print int_param
   print string_param
   print test_struct.int_test
   print test_struct.string_test
   return 0

CALLBACKFUNCTION = CFUNCTYPE(c_int, c_int, c_char_p, TestStruct)
cmp_func = CALLBACKFUNCTION(callback_function_test)

lib.callbackParam(cmp_func)
