############################################################
# CIS 391: Homework 8
############################################################

student_name = "Darren Yin"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import re


############################################################
# Section 1: Hidden Markov Models
############################################################

def load_corpus(path):
		f = open(path)
		ret = []

		for line in f:
			t = line.replace("\r\n","")

			split_line = t.split(" ")

			for i in split_line:
				ret.append(tuple(i.split("=", 1)))

		return ret


class Tagger(object):

		def __init__(self, sentences):
			s = sentences

			#probability that a sentence begins with a tag
			init_list = dict()
			temp = True
			total_sum = 0
			for i in s:
				if i[1] not in init_list and temp:
					init_list[i[1]] = 1
					total_sum = total_sum+1
				if temp:
					init_list[i[1]] = init_list[i[1]] + 1
					total_sum = total_sum + 1
					temp = False
				if i[1] == '.':
					temp = True

			for i in init_list:
				init_list[i] = float(init_list[i]) / float(total_sum)

			self.init_tag_prob = init_list

			#probability that tag t_j occurs after t_i
			tran_list = dict()
			total_sum = 0
			for i in range(len(s)):
				#if, to prevent out of range error
				if i+1 < len(s):
					if (s[i][1],s[i+1][1]) not in tran_list:
						tran_list[(s[i][1],s[i+1][1])] = 1
						total_sum = total_sum + 1
					else:
						tran_list[(s[i][1],s[i+1][1])] = tran_list[(s[i][1],s[i+1][1])]+1
						total_sum = total_sum + 1
			
			for i in tran_list:
				tran_list[i] = float(tran_list[i]) / float(total_sum)

			self.tran_prob = tran_list

			#probability that token w_j is generated given tag t_i
			emis_list = dict()
			tag_freq = dict()

			#need to find the total number of words with each tag
			for i in s:
				if i[1] not in tag_freq:
					tag_freq[i[1]] = 1
					if i[1] not in emis_list:
						emis_list[i[1]] = dict([(i[0], 1)])
					else:
						if i[0] not in emis_list[i[1]]:
							emis_list[i[1]][i[0]] = 1
						else:
							emis_list[i[1]][i[0]] = emis_list[i[1]][i[0]]+1
				else:
					tag_freq[i[1]] = tag_freq[i[1]] + 1
					if i[0] not in emis_list[i[1]]:
						emis_list[i[1]][i[0]] = 1
					else:
						emis_list[i[1]][i[0]] = emis_list[i[1]][i[0]]+1

			for j in emis_list:
				for i in emis_list[j]:
					emis_list[j][i] = float(emis_list[j][i]) / float(tag_freq[j])

			self.emis_prob = emis_list
			print emis_list
			print tag_freq

		def most_probable_tags(self, tokens):
			e = self.emis_prob
			ret = []

			for token in tokens:
				max = 0;
				max_tag = "";
				for i in e:
					if token in e[i]:
						if e[i][token] > max:
							max = e[i][token]
							max_tag = i;
				ret.append(max_tag)

			return ret


		def viterbi_tags(self, tokens):
			#vertices, implied paths from each vertex in each column to the next column
			#this V ignores the fist node in normal trellis
			V = [[] for i in range(len(tokens))]

			ret = []

			#initialize base case (t = 0)
			#max P of tag * emission probability for that word
			t0 = 0
			tag0 = ""
			for i in self.emis_prob:
				if tokens[0] in self.emis_prob[i]:
					temp = self.init_tag_prob[i]*self.emis_prob[i][tokens[0]]
					if temp > t0:
						t0 = temp
						tag0 = i

			V[0].append((tag0,1))

			#build trellis
			for i in range(1, len(tokens)):
				for tag in self.emis_prob:
					if tokens[i] in self.emis_prob[tag]:
						for j in V[i-1]:
							V[i].append((tag, (self.tran_prob[(j[0],tag)]*self.emis_prob[tag][tokens[i]])))
			print V
			#backtrace
			for i in list(reversed(range(len(tokens)))):
				t = 0
				max_t = ""
				for j in range(len(V[i])):
					temp = V[i][j]
					if temp[1] > t:
						t = temp[1]
						max_t = temp[0]
				ret.append(max_t)

			return list(reversed(ret))


############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = """
8 hours
"""

feedback_question_2 = """
The verterbi decoding section, the slides were hard to understand due to notation.
"""

feedback_question_3 = """
Nothing in particular.
"""
