from Node import Node

def findSubSeq(node: Node, mat):
	""" Returns the Subsequence from the matrix for the given Node """
	final_str = ''
	while(node is not None):
		final_str = (node.getChar() or '') + final_str
		node = node.from_node
	return final_str
	
def longestSubsequences(str1: str, str2: str):
	""" Returns the longest common subsequences between two strings """
	mat  = [ [ Node(0) for j in range(len(str1)+1) ] for i in range(len(str2)+1) ]
	for i in range(1, len(str2)+1):
		for j in range(1, len(str1)+1):
			if(str2[i-1] == str1[j-1]):
				mat[i][j] = Node(mat[i-1][j-1].val + 1, mat[i-1][j-1], str2[i-1])
			else:
				mat[i][j] = Node(mat[i][j-1].val, mat[i][j-1]) if mat[i-1][j] < mat[i][j-1] else Node(mat[i-1][j].val, mat[i-1][j])

	max_len = max(mat[len(str2)]).val
	return [ findSubSeq(node, mat) for node in mat[len(str2)] if node.val == max_len ]

# Calling the function
#str1 = input("Enter first string: ")
#str2 = input("Enter second string: ")

#print(longestSubsequences(str1, str2))