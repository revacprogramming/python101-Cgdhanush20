text= "X-DSPAM-Confidence:    0.8475"
a=text.find(":")
text=text[a:]
print(float(text))