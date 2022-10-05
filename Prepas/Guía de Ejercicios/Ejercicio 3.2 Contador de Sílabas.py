x = "Outside of that, Hu argues that the royalties can be more reliable than the entropy of Wall Street. No matter what happens to the stock market, people are always going to be listening to music."
y = "CBD, which comes from either a marijuana or hemp plant, is non-psychoactive, so it won’t get you high like THC (tetrayhydrocannabinol). It may, however, offer anti-inflammatory, antioxidant, anti-psychotic, anti-convulsant, and antidepressant properties. Because it can hemp is legal in all 50 states, hemp-derived CBD products are becoming more readily available online and in stores all over the country."
z = "According to a report published by Fast Company, apparel sales have plummeted by 50 percent. It’s a margin that will be difficult to recover from, especially for small businesses that don’t have the backing of major conglomerates. These independent companies rely on seasonal buys from retailers to stay afloat. But with the bevy of store closures and restrictions on online sales, these behemoth retailers are facing hard times of their own."
count = 0

print("x:")
print("\t Índices:")
for letter in x:
    if letter == "a" and len(x) > count+1:
        if x[count+1] == "t":
            print (f"\t\t*{count}-{count+1}")
    count += 1
print(f"\tRepeticiones: {x.count('at')}")

print("y:")
print("\t Índices:")
for letter in y:
    if letter == "o" and len(y) > count+1:
        if y[count+1] == "m":
            print (f"\t\t*{count}-{count+1}")
    count += 1
print(f"\tRepeticiones: {y.count('om')}")

print("z:")
print("\t Índices:")
for letter in z:
    if letter == "i" and len(z) > count+1:
        if z[count+1] == "n":
            print (f"\t\t*{count}-{count+1}")
    count += 1
print(f"\tRepeticiones: {z.count('in')}")