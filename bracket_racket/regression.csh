#!/bin/bash -f

g++ main.cpp

echo "123" | ./a.out
echo "(abc)" | ./a.out
echo "()abc()" | ./a.out
echo "([<{abc123abc}>])" | ./a.out


echo "(abc[123)abc]" | ./a.out
echo "(abc>" | ./a.out
