---
title: Learn python and cryptography
subtitle:
topic:
date: Sep 29, 2020
category:
---

## Introduction

The tangible outcome of this project is a python module that performs
basic cryptography operations. Nevertheless, the main outcome is a
working knowledge of python, code testing, and code architecture.

A few definitions before we dive into the project:

Plaintext
~   The input information, intelligible to everyone.

Ciphertext
~   The unintelligible representation of the data.

Encryption
~   The process of converting plaintext into ciphertext.

Decryption
~   The reverse of encryption.

Cipher
~   Is a pair of algorithms that create the encryption and the decryption.

Key
~   The key is a secret, usually a short string of characters, which
    is needed to encrypt or decrypt the ciphertext.

## Reverse Cipher

One of The simplest cryptography algorithm is the reverse cipher. It
reverses the letters in the plaintext to obtain the ciphertext. For
example for "hello world" input, the ciphertext is "dlrow olleh".

Start a module `ReverseCipher` in `crypto.py` along with a unit test in
`test/crypt.py` that performs the reverse cipher for arbitrary string
input.

This is the first building block in out cryptography code and you'd
like to properly setup the framework. Before starting to write any
code, write down the functionalities that you expect from a generic
cipher class and include them in your class.

For testing, we use `pytest` framework and calling `pytest` in the
base directory should successfully run the tests.

<div class="pagebreak"> </div>

## Reverse Cipher for byte

Extend your code so that it treats the string as a byte string and
reverses the order of bytes instead of each alphabet letter.  Test
your code with "hello world 😀". Read the
[byte](https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview)
and [memory
views](https://docs.python.org/3/library/stdtypes.html#memory-views)
section of python docs.

## Caesar Cipher

Caesar cipher is a simple substitution cipher that shifts by `k` in
the alphabet, the cipher key. For example, with `k=3` and English
alphabet, "abyz" is mapped to "debc". Add a new module `CaeserCipher`
that encrypts and decrypts a given generic string, based on this
Cipher. What is the good generic alphabet that handles all type of
strings independent of encoding?

## Hacking Caesar Cipher

It is very easy to find the encryption key given the ciphertext.

1.  Discuss the algorithm for hacking Caesar cipher. What is the
    complexity of the algorithm.
2.  Write a function or module that finds the key given the
    ciphertext.

    Soon we will learn more elaborate algorithms and try to hack
    them. The hacking function/module may be useful there. Discuss the
    design decisions to enable future extensions.

