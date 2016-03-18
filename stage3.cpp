
#include "stage3.hpp"
#include <cstring>
#include <jni.h>

extern "C" Stage3 *stage3_create() {
    return new Stage3();
}

extern "C" void stage3_delete(Stage3 *st) {
    delete st;
}

extern "C" const char *stage3_blep(Stage3 *st, char *foo) {
    return strdup(st->blep(foo).c_str());
}

std::string Stage3::blep(std::string foo) {
    JavaVM *jvm = NULL;
    JNIEnv *env = NULL;

    JNI_GetCreatedJavaVMs(&jvm, 1, NULL);
    jvm->AttachCurrentThread((void **)&env, NULL);


    jclass stage4 = env->FindClass("Stage4");
    jmethodID blep_id = env->GetStaticMethodID(stage4, "blep", "(Ljava/lang/String;)Ljava/lang/String;");

    jstring jfoo = env->NewStringUTF(foo.c_str());
    jstring jres = static_cast<jstring>(env->CallStaticObjectMethod(stage4, blep_id, jfoo));
    
    const char *cfoo = env->GetStringUTFChars(jres, 0);
    const char *rv = strdup(cfoo);
    env->ReleaseStringUTFChars(jfoo, cfoo);

    jvm->DetachCurrentThread();
    return rv;
}

int main(int argc, const char *argv[]) {
    if (argc < 2)
        return 1;
    Stage3 *st = new Stage3();
    printf("%s\n", st->blep(argv[1]));
    delete st;
    return 0;
}