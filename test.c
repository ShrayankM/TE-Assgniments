#include<stdio.h>
#include<jni.h>
#include "test.h"
#include<math.h>

JNIEXPORT jint JNICALL Java_test_add(JNIEnv *env, jobject object, jint a, jint b)
{
	int temp;
	temp = a + b;
	return temp;
}

JNIEXPORT jint JNICALL Java_test_sub(JNIEnv *env, jobject object, jint a, jint b)
{
	int temp;
	temp = a - b;
	return temp;
}

JNIEXPORT jint JNICALL Java_test_mul(JNIEnv *env, jobject object, jint a, jint b)
{
	int temp;
	temp = a * b;
	return temp;
}

JNIEXPORT jint JNICALL Java_test_div(JNIEnv *env, jobject object, jint a, jint b)
{
	int temp;
	temp = a / b;
	return temp;
}
JNIEXPORT jfloat JNICALL Java_test_my_1sqrt(JNIEnv *env, jobject object, jint a)
{
	float temp;
	temp = sqrt(a);
	return temp;
}

JNIEXPORT jdouble JNICALL Java_test_my_1sin(JNIEnv *env, jobject obj, jint a)
{
	double n;
	double temp;
	n = a * (3.14 / 180);
	temp = sin(n);
	return temp;
}

JNIEXPORT jdouble JNICALL Java_test_my_1cos(JNIEnv *env, jobject obj, jint a)
{
	double n;
	double temp;
	n = a * (3.14 / 180);
	temp = cos(n);
	return temp;
}

