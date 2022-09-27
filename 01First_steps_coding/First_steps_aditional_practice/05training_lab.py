w=float(input())
h=float(input())
coridor=1
w_descs=float(w//1.2)
h_descs=float((h-coridor)//0.7)
work_places=int((h_descs * w_descs)-3)
print(work_places)