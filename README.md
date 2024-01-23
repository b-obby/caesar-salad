# caesar-salad
A Caesar Cipher encryption and decryption script created with Python
 

### Before creating the script, it is imporatant to understand what a Ceasar Cipher even is.

>A **Caesar Cipher** is when the letters of the alphabet are shifted left or right by n places. 
>* For example, the default english alphabet starts with `abcd...` 
>* If we want to use the Caesar Cipher to shift our alphabet left by 1 place, our alphabet would now be `bcde...  `
>
>Imagine visually watching your alphabet shift left: B has taken A's spot, and A now has been pushed to the back of the line. 
>
>If we were to use this example key alphabet to encrypt the following phrase: "hire me" our output would look like "ijsf nf" 
>
>While this iteration was simple to manually encrypt, ceasar shifts can get with longer pieces of plaintext and with shifts larger than n = 1. 

### I have created two different scripts:
* An encryption tool
* A brute-force decryption tool

> As these scripts are very simple, the plaintext / ciphertext must be hard-coded by the user per-use.

### Optional Extra-Credit To-Do's
- [ ] Agregate both functionalities into a singular script featuring a pop up GUI of sorts so inputs do not have to be hard-coded each time. 
- [ ] Create a bash version where users could either decrypt or brute through a terminal by passing parameters in the command line such as `caesar-salad -plaintext "I LOVE BEANS" -key 2` or `caesar-salad -brute "J MPWF CFBOT"` 

