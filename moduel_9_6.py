def all_variants(text):
    for a in range(1, len(text) + 1):
        for b in range(len(text) - a + 1):
            yield text[b:b+a]

a = all_variants("abc")
for i in a:
    print(i)