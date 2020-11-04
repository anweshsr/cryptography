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

## Reverse cipher

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

## Reverse cipher for byte

Extend your code so that it treats the string as a byte string and
reverses the order of bytes instead of each alphabet letter.  Test
your code with "hello world 😀". Read the
[byte](https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview)
and [memory
views](https://docs.python.org/3/library/stdtypes.html#memory-views)
section of python docs.

## Caesar cipher

Caesar cipher is a simple substitution cipher that shifts by `k` in
the alphabet, the cipher key. For example, with `k=3` and English
alphabet, "abyz" is mapped to "debc". Add a new module `CaeserCipher`
that encrypts and decrypts a given generic string, based on this
Cipher. What is the good generic alphabet that handles all type of
strings independent of encoding?

## Hacking Caesar cipher

It is very easy to find the encryption key given the ciphertext.

1.  Discuss the algorithm for hacking Caesar cipher. What is the
    complexity of the algorithm.
2.  Write a function or module that finds the key given the
    ciphertext.

    Soon we will learn more elaborate algorithms and try to hack
    them. The hacking function/module may be useful there. Discuss the
    design decisions to enable future extensions.

### English word list

These are a few options for word list:

-   https://github.com/first20hours/google-10000-english
-   Peter Norvig has big [collection](https://norvig.com/ngrams/). He
    has a tutorial for [writing spelling
    checker](http://norvig.com/spell-correct.html) that is useful to
    read.
-   On Mac an Linux, there is an alphabetical list at
    `/usr/share/dict/words`.

## Transposition cipher

The transposition cipher rearranges the symbols into an order that
makes the original message unreadable. A variant of the transposition
cipher is the Columnar transposition. In a columnar transposition, the
message is written out in rows of a fixed length, and then read out
again column by column (equivalent to matrix transpose in linear
algebra). The row width is the key for this algorithm.

Write a `TranspositionCipher` module that handles encryption and
decryption.

-  The message length is typically not divisible by the key and you
   need to pad the end of the message with a "null word". The null
   word could be specified as part of the key. In this case, the key
   is tuple, for example, `(10, stumptown)`.

-  When using lists in python, you can preallocate the memory. Find
   out what is the best way to do so and discuss its pitfalls.

### Using bytes

For the Reverse cipher, you made it work with a byte string. From
encryption and decryption purposes we can define our alphabet to be
the numbers 0 to 255 (the range of `uint8`, one byte). The benefit of
this approach is

1.  Any algorithm that we have, can work with this set
2.  we don't need to worry about interpretation of the byte and can
    encrypt any text and binary objects.

Update your code to work with bytes and can encrypt any byte
string. You already saw the `bytearray` an `memoryview`, you can also
use `ndarray.tobytes` and `numpy.frombuffer`.

Bear in mind that later on, we may switch to larger range and use two
or more bytes as our alphabets range. Your current code changes should
not hinder switching to wider alphabet set.

## Hacking the transposition cipher
## Substitution cipher
## Vigenere Cipher
## Hacking the Vigenere Cipher
## Public Key Cipher
