#include "python.h" 

static PyObject *

spam_strlen(PyObject *self, PyObject *args)
{
	int base, a, b;
	float nom;

	if (!PyArg_ParseTuple(args, "iii", &base, &a, &b)) // 매개변수 값을 분석하고 지역변수에 할당 시킵니다.
		return NULL;

	nom = (float)(a - base) / (float)(b - base);

	return Py_BuildValue("f", nom);
}

static PyMethodDef SpamMethods[] = {
	{ "getNormal", spam_strlen, METH_VARARGS,
	"start, current, end" },
	{ NULL, NULL, 0, NULL } // 배열의 끝을 나타냅니다.
};

static struct PyModuleDef spammodule = {
	PyModuleDef_HEAD_INIT,
	"spam",            // 모듈 이름
	"It is test module.", // 모듈 설명을 적는 부분, 모듈의 __doc__에 저장됩니다.
	-1,SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
	return PyModule_Create(&spammodule);
}