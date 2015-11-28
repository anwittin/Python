text = "X-DSPAM-Confidence:    0.8475";

info = text.find('0')
num = text[info:]
num.strip()
print num