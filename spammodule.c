#include "python.h" 

static PyObject *

spam_strlen(PyObject *self, PyObject *args)
{
	int base, a, b;
	float nom;

	if (!PyArg_ParseTuple(args, "iii", &base, &a, &b)) // �Ű����� ���� �м��ϰ� ���������� �Ҵ� ��ŵ�ϴ�.
		return NULL;

	nom = (float)(a - base) / (float)(b - base);

	return Py_BuildValue("f", nom);
}

static PyMethodDef SpamMethods[] = {
	{ "getNormal", spam_strlen, METH_VARARGS,
	"start, current, end" },
	{ NULL, NULL, 0, NULL } // �迭�� ���� ��Ÿ���ϴ�.
};

static struct PyModuleDef spammodule = {
	PyModuleDef_HEAD_INIT,
	"spam",            // ��� �̸�
	"It is test module.", // ��� ������ ���� �κ�, ����� __doc__�� ����˴ϴ�.
	-1,SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
	return PyModule_Create(&spammodule);
}