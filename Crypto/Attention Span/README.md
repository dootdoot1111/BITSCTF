# Attention Span

This crypto challenge presents us with another common cipher asked in CTF's called 'Mono-Alphabetic Substitution' Cipher.

We again head over to [Boxentriq](https://www.boxentriq.com/code-breaking/cryptogram). 

The question presents us with the following text :

```
WQLVGLENS YEYFSPIP XYPLM NQSAOYEYFSPIP GPLP OCL WYNO OCYO EYOGQYF FYEDGYDL IP EBO QYEMBZ IE EYOGQL YEM PIEDFL YFACYXLOIN XYPLM PGXPOIOGOIBE MBLP EBO CIML OCL POYOIPOINYF AQBALQOILP BW OCL EYOGQYF FYEDGYDL. IE OCL NYPL BW LENQSAOIBE GPIED ZBEBYFACYXLOIN PGXPOIOGOIBE, OB POYQO MLNIACLQIED OCL LENQSAOIBE IO IP GPLWGF OB DLO Y WQLVGLENS NBGEO BW YFF OCL FLOOLQP. OCL ZBPO WQLVGLEO FLOOLQ ZYS QLAQLPLEO OCL ZBPO NBZZBE FLOOLQ IE LEDFIPC, L WBFFBULM XS O, Y, B YEM I UCLQLYP OCL FLYPO WQLVGLEO YQL V, H YEM T. POYOIPOINYF AYOOLQEP IE Y FYEDGYDL NYE XL MLOLNOLM XS OQYNIED OCL QLMGEMYENS BW OCL OLTO IE OCL FYEDGYDL. IO CYP XLLE QLYFIHLM OCYO KYQIBGP GEIKLQPYF QLDGFYQIOILP NCYQYNOLQIHL OLTO WQBZ MIWWLQLEO MBZYIEP YEM FYEDGYDLP. CLQL IP SBGQ WFYD XIOPNOW{DBBM_SBG_AYIM_YOOLEOIBE}
```

We hit the auto solve on Boxentriq to get an idea of what the text should look like. It uses Frequency Analysis to decrypt the text. 
Here's what we get :
```
frequency analysis based cryptanalysis uses the fact that natural language is not random in nature and single alphabetic based substitution does not hide the statistical properties of the natural language in the case of encryption using monoalphabetic substitution to start deciphering the encryption it is useful to get a frequency count of all the letters the most frequent letter may represent the most common letter in english e followed by t a o and i whereas the least frequent are q k and j st..........
```

So now we know almost all substitutions for the letters and can decode accordingly!
