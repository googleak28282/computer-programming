def calc_max_min_avg(grades):
	Max=-1
	Min=100
	total=0
	for i in range(len(grades)):
		if grades[i]>Max:
			Max=grades[i]
		if grades[i]<Min:
			Min=grades[i]
		total+=grades[i]
		avg=total/len(grades)
	return (Max,Min,avg)
grades = [90,95,91,92,94,89,94,70]
(Max,Min,avg)=calc_max_min_avg(grades)
print("Highest:",Max)
print("Lowest:",Min)
print("average:",avg)