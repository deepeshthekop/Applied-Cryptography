# Using/ modifying the Program in Chapter-7 (Book: Hacking Secret Ciphers with Python) -
# break the following ciphertexts:

# I. R UXEN VH TRCCH,
# II. FR DBMMR EHOXL FX,
# III. CXPNCQNA FN'AN BX QJYYH,
# IV. OBR OZKOMG QOFSTFSS.
# V. PDKQCD IU DAWZ DWO OQOLEYEKJO,
# VI. FTMF U WQQB GZPQD YK TMF,
# VII. AR ITMF YUSTF TMBBQZ,
# VIII. DA D NCMVIF OJ OCZ NDUZ JA V MVO.
# IX. ZFBI. J'N QSFUUZ TVSF NZ DBU XPVME FBU NF

# Caesar Cipher Hacker

message = 'ZFBI. J\'N QSFUUZ TVSF NZ DBU XPVME FBU NF'

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# loop through every possible key
for key in range(len(LETTERS)):

    # It is important to set translated to the blank string so that the
    # previous iteration's value for translated is cleared.
    translated = ''

    # The rest of the program is the same as the original Caesar program:

    # run the encryption/decryption code on each symbol in the message
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) # get the number of the symbol
            num = num - key

            # handle the wrap-around if num is 26 or larger or less than 0
            if num < 0:
                num = num + len(LETTERS)

            # add number's symbol at the end of translated
            translated = translated + LETTERS[num]

        else:
            # just add the symbol without encrypting/decrypting
            translated = translated + symbol

            # display the current key being tested, along with its decryption
    print('Key #%s: %s' % (key, translated))