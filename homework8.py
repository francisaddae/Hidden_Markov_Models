############################################################
# CIS 391: Homework 8
############################################################

student_name = "Darren Yin"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import copy


############################################################
# Section 1: Hidden Markov Models
############################################################

def load_corpus(path):
		f = open(path)
		ret = []

		for line in f:
			s = []
			t = line.replace("\r\n","")

			split_line = t.split(" ")

			for i in split_line:
				s.append(tuple(i.split("=", 1)))
			ret.append(s)

		return ret


class Tagger(object):

		def __init__(self, sentences):

			init_list = dict()
			tran_list = dict()
			emis_list = dict()
			tag_freq = dict()
			total_sum1 = 0
			total_sum2 = 0
			for s in sentences:
				#probability that a sentence begins with a tag
				t = s[0]
				total_sum1 += 1
				if t[1] not in init_list:
					init_list[t[1]] = 1
				else:
					init_list[t[1]] = init_list[t[1]] + 1

				for i in range(len(s)):
					#probability that tag t_j occurs after t_i
					#if, to prevent out of range error
					if i+1 < len(s):
						total_sum2 = total_sum2 + 1
						if (s[i][1],s[i+1][1]) not in tran_list:
						    tran_list[(s[i][1],s[i+1][1])] = 1
						else:
						    tran_list[(s[i][1],s[i+1][1])] = tran_list[(s[i][1],s[i+1][1])]+1

					#probability that token w_j is generated given tag t_i
					#need to find the total number of words with each tag
					j = s[i]
					if j[1] not in tag_freq:
						tag_freq[j[1]] = 1
						if j[1] not in emis_list:
						    emis_list[j[1]] = dict([(j[0], 1)])
						else:
						    if it[0] not in emis_list[j[1]]:
						        emis_list[j[1]][j[0]] = 1
						    else:
						        emis_list[j[1]][j[0]] = emis_list[j[1]][j[0]]+1
					else:
						tag_freq[j[1]] = tag_freq[j[1]] + 1
						if j[0] not in emis_list[j[1]]:
						    emis_list[j[1]][j[0]] = 1
						else:
						    emis_list[j[1]][j[0]] = emis_list[j[1]][j[0]]+1

			for i in init_list:
				init_list[i] = (float(init_list[i])+0.0001) / (float(total_sum1)+0.0001*(len(init_list)+1))

			self.init_tag_prob = init_list

			for i in tran_list:
				tran_list[i] = (float(tran_list[i])+0.0001) / (float(total_sum2)+0.0001*(len(tran_list)+1))

			self.tran_prob = tran_list

			for j in emis_list:
				for i in emis_list[j]:
					emis_list[j][i] = (float(emis_list[j][i])+0.0001) / (float(tag_freq[j])+0.0001*(len(emis_list[j])+1))

			self.emis_prob = emis_list

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

			ret = []

			#initial state
			t0 = 0
			tag0 = ""
			for i in self.emis_prob:
				if tokens[0] in self.emis_prob[i]:
					temp = self.init_tag_prob[i]*self.emis_prob[i][tokens[0]]
					if temp > t0:
						t0 = temp
						tag0 = i

			ret.append(tag0)

			#rest of the trellis
			for i in range(1, len(tokens)):
				prob_max = 0
				best_tag = ''
				for tag in self.emis_prob:
					if tokens[i] in self.emis_prob[tag]:
						temp = self.tran_prob[(ret[-1],tag)]*self.emis_prob[tag][tokens[i]]
						if temp > prob_max:
							prob_max = temp
							best_tag = tag
				ret.append(best_tag)

			return ret



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
