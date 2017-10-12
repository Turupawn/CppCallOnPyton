#include <iostream>
using namespace std;

struct TestStruct
{
  int int_test;
  char* string_test;
};

extern "C"
{
  void stringParam(char* string_param)
  {
    cout<<"String param: "<<endl;
    cout<<string_param<<endl;
  }

  void vectorParam(int* vector_param, int vector_size)
  {
    cout << "Vector param: " << endl;
    for(int i=0; i<vector_size; i++)
    {
      cout<<vector_param[i]<<endl;
    }
  }

  void structParam(TestStruct test_struct)
  {
    cout << "Struct param: " << endl;
    cout<<test_struct.int_test<<endl;
    cout<<test_struct.string_test<<endl;
  }

  int callbackParam(void (*callback)(int, char*, TestStruct))
  {
    TestStruct test_struct;
    test_struct.int_test = 500;
    test_struct.string_test = (char*)"hello callback with struct param";

    callback(100, (char*)"hello callback", test_struct);
  }
}
