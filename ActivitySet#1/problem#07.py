text= "X-DSPAM-Confidence:    0.8475"
a=text.find("0")
text=text[a:]
print(float(text))