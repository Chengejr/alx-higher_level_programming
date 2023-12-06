#include <Python.h>

void print_python_list(PyObject *p) {
    Py_ssize_t i, size;
    PyObject *item;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    size = PyList_Size(p);
    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *data;

    printf("[.] Bytes object info\n");

    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    data = PyBytes_AsString(p);

    printf("  Size: %ld\n", size);
    printf("  trying string: %s\n", data);

    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; i++) {
        printf("%02hhx", data[i]);
        if (i < size - 1 && i < 9)
            printf(" ");
    }
    printf("\n");
}
