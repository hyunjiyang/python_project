def main():
    while True:
        mid = float(input("Enter grade on midterm : "))
        final = float(input("Enter grade on final exam : "))

        if 0<=mid<=100 and 0<=final<=100:
            grade = float((mid + 2*final)/3)
            break     
        else:
            print("Score range is 0~100.")      
            
    print("Semester Grade: ", semesterGrade(grade))

def semesterGrade(grade):
    grade = ceil(grade)
    if 90<=grade:
        return "A"
    elif 80<=grade:
        return "B"
    elif 70<=grade:
        return "C"
    elif 60<=grade:
        return "D"        
    else:
        return "F"

def ceil(grade):
    if grade-int(grade)>0 : #float-int로 소수점이 나오는 경우 올림해줌.
        grade = int(grade)+1
    return grade #else일경우는 float여도 상관 없으므로 따로 int로 변환하지 않음.

main()