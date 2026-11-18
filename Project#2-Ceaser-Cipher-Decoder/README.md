# 🔐 Caesar Cipher Decoder

A simple Python program that encrypts and decrypts messages using the Caesar cipher.

## What is the Caesar Cipher?

The Caesar cipher is one of the oldest and simplest ways to hide a message. It's named after Julius Caesar, who used it to send private messages.

It works by **shifting every letter in the alphabet by a set number of places**. This program uses a shift of **3**:

```
Plain:     A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Encrypted: D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
```

So `HELLO` becomes `KHOOR`. To decrypt, you shift each letter **back** 3 places.

When a shift goes past `Z`, it wraps around to the start of the alphabet, so `X` becomes `A`, `Y` becomes `B` and `Z` becomes `C`.



