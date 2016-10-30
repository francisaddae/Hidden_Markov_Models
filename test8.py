# cis 391 homework 8 test program
from homework8 import *
import datetime
import string

print '=========== Homework 8 =========='

print 'load_corpus()'

corpus = load_corpus("brown_corpus.txt")
print len(corpus)
print corpus[1402]
print corpus[1799]


print 'Tagger() initialization'

print 'Tagger Corpus'
time = datetime.datetime.now().time()
time1 = time.isoformat()
t1 = Tagger(corpus)
time = datetime.datetime.now().time()
print 'Tagger init start:', time1
print 'Tagger init end:', time.isoformat()

print 'most_probable_tags()'
print t1.most_probable_tags(['The', 'man', 'walks', '.'])
print t1.most_probable_tags(['The', 'blue', 'bird', 'sings'])

print 'viterbi_tags()'
s1 = "I am waiting to reply".split()
print 'most_probable_tags(s1): ', t1.most_probable_tags(s1)

time = datetime.datetime.now().time()
time1 = time.isoformat()
print 'viterbi_tags(s1): ', t1.viterbi_tags(s1)
time = datetime.datetime.now().time()
print 'Viterbi_tags(s1) start:', time1
print 'Viterbi_tags(s1) end:', time.isoformat()


s2 = "I saw the play".split()
print 'most_probable_tags(s2): ', t1.most_probable_tags(s2)

time = datetime.datetime.now().time()
time1 = time.isoformat()
print 'viterbi_tags(s2): ', t1.viterbi_tags(s2)
time = datetime.datetime.now().time()
print 'Viterbi_tags(s2) start:', time1
print 'Viterbi_tags(s2) end:', time.isoformat()

s3 = [i for k in corpus[1:100] for i,j in k]
s3_answer = [j for k in corpus[1:100] for i,j in k]

time = datetime.datetime.now().time()
time1 = time.isoformat()
print 'viterbi_tags(s3): ', t1.viterbi_tags(s3)
time = datetime.datetime.now().time()
print 'Viterbi_tags(s3) start:', time1
print 'Viterbi_tags(s3) end:', time.isoformat()
print s3_answer
