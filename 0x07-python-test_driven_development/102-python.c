#include <Python.h>
#include <object.h>
#include <unicodeobject.h>

void print_python_string(PyObject *p)
{
	const char *type = NULL;
	Py_ssize_t len = 0;
	wchar_t *str = NULL;

	printf("[.] string object info\n");
	if (!PyUnicode_check(p))
	{
		printf(" [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicodee_Is_COMPACT_ASCII(p))
		type = "compact ascii";
	else
		type = "compact unicode object";

	str = PyUnicode_AsWideCharString(p, &len);

	printf(" type: %s\n", type);
	pritnf(" length: %ld\n", len);
	printf(" value: %ls\n", str);
}
