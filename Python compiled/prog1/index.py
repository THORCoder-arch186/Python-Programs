marks_M = int(input("Enter your marks for Math: "))
marks_E = int(input("Enter your marks for English: "))
marks_S = int(input("Enter your marks for Science: "))

def find_best(M, E, S):
    best = M

    if E>best:
        best = E
    elif S>best:
        best = S
    
    if best==M:
        result="Maths"
    elif best==E:
        result="English"
    elif best==S:
        result= "Science"

    return result
    

pf_M = "passed" if marks_M>=40 else "failed"
pf_E = "passed" if marks_E>=40 else "failed"
pf_S = "passed" if marks_S>=40 else "failed"

total = marks_S + marks_E + marks_M
avg = total/3
bps = find_best(marks_M, marks_E, marks_S)

print(f"Your score in Maths: {marks_M}")
print(f"Your score in Science: {marks_S}")
print(f"Your score in English: {marks_E}")
print(f"Your total score is {total}, and your average marks is {avg}")
print(f"Your best performed subject is {bps}")