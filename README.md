This is my first project uploaded to git hub, two python programs that can encipher and decipher a message stored in message.txt

Below is a general outline of the steps taken to encipher/decipher:

1. Each character that can be found on my personal keyboard has been assigned a 4 digit number which can be found in the number sheet.xlsx.
2. The encrypt.py program reads the text stored in message.txt and asks the user for a encrpyion key or "seed"
3. Each character of the message found in the message.txt file is converted to its 4 digit counterpart and stored as one long integer, the same is done for the encryption key.
4. Now that both the seed and plaintext have been converted to an integer they are multiplied together and converted to hexadecimal format.
5. The 0x found at the start of hex numbers is removed for easu of use.
6. Each character found within this new number is then converted to one of three characters, as can be found in the numbers sheet.xlsx.
7. Finally this completed message is stored within the message.txt file for future decrypting.

8. The decode.py program functions asks for the original seed used, converts it in the same way to an integer format. Then proceeds to follow the steps above backwards to decrpyt the message. Once again storing in message.txt.

