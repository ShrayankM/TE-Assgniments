#include<stdio.h>
#include<jni.h>
#include "add.h"

JNIEXPORT jint JNICALL Java_add_my_1Add(JNIEnv *env, jclass object, jint a, jint b)
{
	int temp;
	temp = a + b;
	return temp;
}

JNIEXPORT jint JNICALL Java_add_my_1Sub(JNIEnv *env, jclass object, jint a, jint b)
{
	int temp;
	temp = a - b;
	return temp;
}

JNIEXPORT jint JNICALL Java_add_my_1Mul(JNIEnv *env, jclass object, jint a, jint b)
{
	int temp;
	temp = a * b;
	return temp;
}

JNIEXPORT jint JNICALL Java_add_my_1Div(JNIEnv *env, jclass object, jint a, jint b)
{
	int temp;
	temp = a / b;
	return temp;
}

