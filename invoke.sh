#!/usr/bin/env sh
env MONO_PATH=/home/jaseg/dev/toys/ffi/mono/mcs/class/lib/net_4_x LD_LIBRARY_PATH=/usr/lib/jvm/java-8-openjdk/jre/lib/amd64/server java -Djava.library.path=/home/jaseg/dev/toys/ffi:/usr/lib -cp ./nativelibs4java/libraries/Mono/Mono.jar:. Stage1 test
