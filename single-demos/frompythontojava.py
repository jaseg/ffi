#!/usr/bin/env python3

import sys
from ctypes import *

jni = CDLL('/usr/lib/jvm/java-8-openjdk/jre/lib/amd64/server/libjvm.so')

if __name__ == '__main__':
    _,foo = sys.argv
    print('Python running:', foo)

    class JavaVMInitArgs(Structure):
        _fields_ = [('version', c_int),
                    ('nOptions', c_int),
                    ('options', c_void_p),
                    ('ignoreUnrecognized', c_int)]

    class JNINativeInterface(Structure):
        _fields_ = [
            ('reserved0', c_int64),
            ('reserved1', c_int64),
            ('reserved2', c_int64),
            ('reserved3', c_int64),
            ('GetVersion', c_int64),
            ('DefineClass', c_int64),
            ('FindClass', c_int64),
            ('FromReflectedMethod', c_int64),
            ('FromReflectedField', c_int64),
            ('ToReflectedMethod', c_int64),
            ('GetSuperclass', c_int64),
            ('IsAssignableFrom', c_int64),
            ('ToReflectedField', c_int64),
            ('Throw', c_int64),
            ('ThrowNew', c_int64),
            ('ExceptionOccurred', c_int64),
            ('ExceptionDescribe', c_int64),
            ('ExceptionClear', c_int64),
            ('FatalError', c_int64),
            ('PushLocalFrame', c_int64),
            ('PopLocalFrame', c_int64),
            ('NewGlobalRef', c_int64),
            ('DeleteGlobalRef', c_int64),
            ('DeleteLocalRef', c_int64),
            ('IsSameObject', c_int64),
            ('NewLocalRef', c_int64),
            ('EnsureLocalCapacity', c_int64),
            ('AllocObject', c_int64),
            ('NewObject', c_int64),
            ('NewObjectV', c_int64),
            ('NewObjectA', c_int64),
            ('GetObjectClass', c_int64),
            ('IsInstanceOf', c_int64),
            ('GetMethodID', c_int64),
            ('CallObjectMethod', c_int64),
            ('CallObjectMethodV', c_int64),
            ('CallObjectMethodA', c_int64),
            ('CallBooleanMethod', c_int64),
            ('CallBooleanMethodV', c_int64),
            ('CallBooleanMethodA', c_int64),
            ('CallByteMethod', c_int64),
            ('CallByteMethodV', c_int64),
            ('CallByteMethodA', c_int64),
            ('CallCharMethod', c_int64),
            ('CallCharMethodV', c_int64),
            ('CallCharMethodA', c_int64),
            ('CallShortMethod', c_int64),
            ('CallShortMethodV', c_int64),
            ('CallShortMethodA', c_int64),
            ('CallIntMethod', c_int64),
            ('CallIntMethodV', c_int64),
            ('CallIntMethodA', c_int64),
            ('CallLongMethod', c_int64),
            ('CallLongMethodV', c_int64),
            ('CallLongMethodA', c_int64),
            ('CallFloatMethod', c_int64),
            ('CallFloatMethodV', c_int64),
            ('CallFloatMethodA', c_int64),
            ('CallDoubleMethod', c_int64),
            ('CallDoubleMethodV', c_int64),
            ('CallDoubleMethodA', c_int64),
            ('CallVoidMethod', c_int64),
            ('CallVoidMethodV', c_int64),
            ('CallVoidMethodA', c_int64),
            ('CallNonvirtualObjectMethod', c_int64),
            ('CallNonvirtualObjectMethodV', c_int64),
            ('CallNonvirtualObjectMethodA', c_int64),
            ('CallNonvirtualBooleanMethod', c_int64),
            ('CallNonvirtualBooleanMethodV', c_int64),
            ('CallNonvirtualBooleanMethodA', c_int64),
            ('CallNonvirtualByteMethod', c_int64),
            ('CallNonvirtualByteMethodV', c_int64),
            ('CallNonvirtualByteMethodA', c_int64),
            ('CallNonvirtualCharMethod', c_int64),
            ('CallNonvirtualCharMethodV', c_int64),
            ('CallNonvirtualCharMethodA', c_int64),
            ('CallNonvirtualShortMethod', c_int64),
            ('CallNonvirtualShortMethodV', c_int64),
            ('CallNonvirtualShortMethodA', c_int64),
            ('CallNonvirtualIntMethod', c_int64),
            ('CallNonvirtualIntMethodV', c_int64),
            ('CallNonvirtualIntMethodA', c_int64),
            ('CallNonvirtualLongMethod', c_int64),
            ('CallNonvirtualLongMethodV', c_int64),
            ('CallNonvirtualLongMethodA', c_int64),
            ('CallNonvirtualFloatMethod', c_int64),
            ('CallNonvirtualFloatMethodV', c_int64),
            ('CallNonvirtualFloatMethodA', c_int64),
            ('CallNonvirtualDoubleMethod', c_int64),
            ('CallNonvirtualDoubleMethodV', c_int64),
            ('CallNonvirtualDoubleMethodA', c_int64),
            ('CallNonvirtualVoidMethod', c_int64),
            ('CallNonvirtualVoidMethodV', c_int64),
            ('CallNonvirtualVoidMethodA', c_int64),
            ('GetFieldID', c_int64),
            ('GetObjectField', c_int64),
            ('GetBooleanField', c_int64),
            ('GetByteField', c_int64),
            ('GetCharField', c_int64),
            ('GetShortField', c_int64),
            ('GetIntField', c_int64),
            ('GetLongField', c_int64),
            ('GetFloatField', c_int64),
            ('GetDoubleField', c_int64),
            ('SetObjectField', c_int64),
            ('SetBooleanField', c_int64),
            ('SetByteField', c_int64),
            ('SetCharField', c_int64),
            ('SetShortField', c_int64),
            ('SetIntField', c_int64),
            ('SetLongField', c_int64),
            ('SetFloatField', c_int64),
            ('SetDoubleField', c_int64),
            ('GetStaticMethodID', c_int64),
            ('CallStaticObjectMethod', c_int64),
            ('CallStaticObjectMethodV', c_int64),
            ('CallStaticObjectMethodA', c_int64),
            ('CallStaticBooleanMethod', c_int64),
            ('CallStaticBooleanMethodV', c_int64),
            ('CallStaticBooleanMethodA', c_int64),
            ('CallStaticByteMethod', c_int64),
            ('CallStaticByteMethodV', c_int64),
            ('CallStaticByteMethodA', c_int64),
            ('CallStaticCharMethod', c_int64),
            ('CallStaticCharMethodV', c_int64),
            ('CallStaticCharMethodA', c_int64),
            ('CallStaticShortMethod', c_int64),
            ('CallStaticShortMethodV', c_int64),
            ('CallStaticShortMethodA', c_int64),
            ('CallStaticIntMethod', c_int64),
            ('CallStaticIntMethodV', c_int64),
            ('CallStaticIntMethodA', c_int64),
            ('CallStaticLongMethod', c_int64),
            ('CallStaticLongMethodV', c_int64),
            ('CallStaticLongMethodA', c_int64),
            ('CallStaticFloatMethod', c_int64),
            ('CallStaticFloatMethodV', c_int64),
            ('CallStaticFloatMethodA', c_int64),
            ('CallStaticDoubleMethod', c_int64),
            ('CallStaticDoubleMethodV', c_int64),
            ('CallStaticDoubleMethodA', c_int64),
            ('CallStaticVoidMethod', c_int64),
            ('CallStaticVoidMethodV', c_int64),
            ('CallStaticVoidMethodA', c_int64),
            ('GetStaticFieldID', c_int64),
            ('GetStaticObjectField', c_int64),
            ('GetStaticBooleanField', c_int64),
            ('GetStaticByteField', c_int64),
            ('GetStaticCharField', c_int64),
            ('GetStaticShortField', c_int64),
            ('GetStaticIntField', c_int64),
            ('GetStaticLongField', c_int64),
            ('GetStaticFloatField', c_int64),
            ('GetStaticDoubleField', c_int64),
            ('SetStaticObjectField', c_int64),
            ('SetStaticBooleanField', c_int64),
            ('SetStaticByteField', c_int64),
            ('SetStaticCharField', c_int64),
            ('SetStaticShortField', c_int64),
            ('SetStaticIntField', c_int64),
            ('SetStaticLongField', c_int64),
            ('SetStaticFloatField', c_int64),
            ('SetStaticDoubleField', c_int64),
            ('NewString', c_int64),
            ('GetStringLength', c_int64),
            ('GetStringChars', c_int64),
            ('ReleaseStringChars', c_int64),
            ('NewStringUTF', c_int64),
            ('GetStringUTFLength', c_int64),
            ('GetStringUTFChars', c_int64),
            ('ReleaseStringUTFChars', c_int64),
            ('GetArrayLength', c_int64),
            ('NewObjectArray', c_int64),
            ('GetObjectArrayElement', c_int64),
            ('SetObjectArrayElement', c_int64),
            ('NewBooleanArray', c_int64),
            ('NewByteArray', c_int64),
            ('NewCharArray', c_int64),
            ('NewShortArray', c_int64),
            ('NewIntArray', c_int64),
            ('NewLongArray', c_int64),
            ('NewFloatArray', c_int64),
            ('NewDoubleArray', c_int64),
            ('GetBooleanArrayElements', c_int64),
            ('GetByteArrayElements', c_int64),
            ('GetCharArrayElements', c_int64),
            ('GetShortArrayElements', c_int64),
            ('GetIntArrayElements', c_int64),
            ('GetLongArrayElements', c_int64),
            ('GetFloatArrayElements', c_int64),
            ('GetDoubleArrayElements', c_int64),
            ('ReleaseBooleanArrayElements', c_int64),
            ('ReleaseByteArrayElements', c_int64),
            ('ReleaseCharArrayElements', c_int64),
            ('ReleaseShortArrayElements', c_int64),
            ('ReleaseIntArrayElements', c_int64),
            ('ReleaseLongArrayElements', c_int64),
            ('ReleaseFloatArrayElements', c_int64),
            ('ReleaseDoubleArrayElements', c_int64),
            ('GetBooleanArrayRegion', c_int64),
            ('GetByteArrayRegion', c_int64),
            ('GetCharArrayRegion', c_int64),
            ('GetShortArrayRegion', c_int64),
            ('GetIntArrayRegion', c_int64),
            ('GetLongArrayRegion', c_int64),
            ('GetFloatArrayRegion', c_int64),
            ('GetDoubleArrayRegion', c_int64),
            ('SetBooleanArrayRegion', c_int64),
            ('SetByteArrayRegion', c_int64),
            ('SetCharArrayRegion', c_int64),
            ('SetShortArrayRegion', c_int64),
            ('SetIntArrayRegion', c_int64),
            ('SetLongArrayRegion', c_int64),
            ('SetFloatArrayRegion', c_int64),
            ('SetDoubleArrayRegion', c_int64),
            ('RegisterNatives', c_int64),
            ('UnregisterNatives', c_int64),
            ('MonitorEnter', c_int64),
            ('MonitorExit', c_int64),
            ('GetJavaVM', c_int64),
            ('GetStringRegion', c_int64),
            ('GetStringUTFRegion', c_int64),
            ('GetPrimitiveArrayCritical', c_int64),
            ('ReleasePrimitiveArrayCritical', c_int64),
            ('GetStringCritical', c_int64),
            ('ReleaseStringCritical', c_int64),
            ('NewWeakGlobalRef', c_int64),
            ('DeleteWeakGlobalRef', c_int64),
            ('ExceptionCheck', c_int64),
            ('NewDirectByteBuffer', c_int64),
            ('GetDirectBufferAddress', c_int64),
            ('GetDirectBufferCapacity', c_int64),
            ('GetObjectRefType', c_int64)]

        def cFindClass(self, a, b):
            return CFUNCTYPE(c_void_p, c_void_p, c_char_p)(int(self.FindClass))(a, b)

        def cGetStaticMethodID(self, a, b, c, d):
            return CFUNCTYPE(c_void_p, c_void_p, c_void_p, c_char_p, c_char_p)(int(self.GetStaticMethodID))(a, b, c, d)

        def cCallStaticObjectMethod(self, a, b, c, d):
            return CFUNCTYPE(c_void_p, c_void_p, c_void_p, c_void_p, c_void_p)(int(self.CallStaticObjectMethod))(a, b, c, d)

        def cNewStringUTF(self, a, b):
            return CFUNCTYPE(c_void_p, c_void_p, c_char_p)(int(self.NewStringUTF))(a, b)

        def cGetStringUTFChars(self, a, b, c):
            return CFUNCTYPE(c_char_p, c_void_p, c_void_p, c_void_p)(int(self.GetStringUTFChars))(a, b, c)

        def cReleaseStringUTFChars(self, a, b, c):
            return CFUNCTYPE(c_void_p, c_void_p, c_void_p, c_char_p)(int(self.ReleaseStringUTFChars))(a, b, c)


    jvm, env = pointer(create_string_buffer(8)), pointer(create_string_buffer(8))
    args = JavaVMInitArgs(0x00010008, 0, None, 0)
    jni.JNI_CreateJavaVM(jvm, env, pointer(args))

    e = cast(env, POINTER(POINTER(POINTER(JNINativeInterface)))).contents.contents.contents
    env = cast(env, POINTER(c_void_p)).contents
    
    fptj = e.cFindClass(env, b"FromPythonToJava")
    blep_id = e.cGetStaticMethodID(env, fptj, b"blep", b"(Ljava/lang/String;)Ljava/lang/String;")

    jfoo = c_void_p(e.cNewStringUTF(env, foo.encode()))
    jres = c_void_p(e.cCallStaticObjectMethod(env, fptj, blep_id, jfoo))
    
    cfoo = c_char_p(e.cGetStringUTFChars(env, jres, 0))
    bar = cfoo.value.decode()
    print('Java responded with "{}".'.format(bar))
