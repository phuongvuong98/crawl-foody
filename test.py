str = "https://www.google.com/maps/place/Nowzone+Fashion+Mall/@10.7642917,106.6824906,17z/data=!3m1!4b1!4m5!3m4!1s0x31752f194dae00e5:0x4b90c5d0bd96fe63!8m2!3d10.7642917!4d106.6824906"

print(str.find("https://www.google.com/maps/place/"))
print(str.find("/@"))
print(str.find("z/"))
print(str[str.find("/@"):str.find("z/")])
