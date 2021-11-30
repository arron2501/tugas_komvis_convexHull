import sys, numpy as num, matplotlib.pyplot as plot

# Function to know if we have a CCW turn
def CCW(p1, p2, p3):
	if (p3[1]-p1[1])*(p2[0]-p1[0]) >= (p2[1]-p1[1])*(p3[0]-p1[0]):
		return True
	return False

# Main function:
def jarvis_march(S):
	n = len(S)
	P = [None] * n
	l = num.where(S[:,0] == num.min(S[:,0]))
	pointOnHull = S[l[0][0]]
	i = 0
	while True:
		P[i] = pointOnHull
		endpoint = S[0]
		for j in range(1,n):
			if (endpoint[0] == pointOnHull[0] and endpoint[1] == pointOnHull[1]) or not CCW(S[j],P[i],endpoint):
				endpoint = S[j]
		i = i + 1
		pointOnHull = endpoint
		if endpoint[0] == P[0][0] and endpoint[1] == P[0][1]:
			break
	for i in range(n):
		if P[-1] is None:
			del P[-1]
	return num.array(P)

# Plot the computed Convex Hull:
def scatter_plot(convex_hull, koordinat_rantai):
    plot.figure()
    plot.plot(convex_hull[:,0],convex_hull[:,1], 'b-', picker=5)
    plot.plot([convex_hull[-1,0],convex_hull[0,0]],[convex_hull[-1,1],convex_hull[0,1]], 'b-', picker=5)
    plot.plot(koordinat_rantai[:,0],koordinat_rantai[:,1],".r")
    plot.axis('off')
    plot.show()