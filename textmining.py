# ------------------------------------ #
# Universidad del Valle de Guatemala   #
# Autores:                             #
#   Andrea Cordón, 16076               #
#   Cristopher Recinos, 16005          #
#   Pablo Lopez, 14509                 #
# textmining.py                        #
# ------------------------------------ #

import string

news_r = open("news_new.txt", "r").read()
twitter_r = open("twitter_new.txt", "r").read()
blogs_r = open("blogs_new.txt", "r").read()

# Guardar en listas
twitter = twitter_r.split(",")
news = news_r.split(",")
blogs = blogs_r.split(",")
print(len(twitter))

# ----------- #
# Frecuencias #
# ----------- #

# Twitter
print("starting")
twitt = []
for i in range(0, len(twitter)):
    if twitter[i] not in twitt:
        twitt.append(twitter[i])
        #print(twitt[i])

#print(twitt)
for j in range(0, len(twitt)):
    print("Frecuencia de", twitt[j], "is", twitter.count(twitt[j]))


# News
print("starting")
new = []
for i in range(0, len(news)):
    if news[i] not in new:
        new.append(news[i])
        #print(new[i])

#print(new)
for j in range(0, len(new)):
    print("Frecuencia de", new[j], "is", news.count(new[j]))


# Blogs
print("starting")
blog = []
for i in range(0, len(blogs)):
    if blogs[i] not in blog:
        blog.append(blogs[i])
        #print(blog[i])

#print(blog)
for j in range(0, len(blog)):
    print("Frecuencia de", blog[j], "is", blogs.count(blog[j]))




# -------- #
# N-Grams  #
# -------- #

def generate_ngrams(s, n):
    s = re.sub(',', ' ', s)
    
    tokens = [token for token in s.split(" ") if token != ""]

    ngrams = zip(*[token[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]
