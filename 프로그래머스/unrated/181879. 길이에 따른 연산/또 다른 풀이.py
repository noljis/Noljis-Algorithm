import functools import reduce

def solution(num_list):
	if len(num_list) >= 11:
		return sum(num_list)
	else:
		return reduce(lambda a,b: a*b, num_list)
  # reduce(lambda [파라미터]: 연산, 배열)
