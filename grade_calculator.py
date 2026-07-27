score = int(input("Type your score here: ")) #we find a score
if score < 0 or score >= 101: #should use 100 like more than maximum
    print("Input error... Invalid score. Please ask teamleader if you want to add A+ ")
elif score >= 0 and score <= 59:
    print("Unfortunaly your score is F")
elif score >= 60 and score <= 69:
    print("Your score is D ")
elif score >= 70 and score <= 79:
    print("Your score is C ")
elif score >= 80 and score <= 89:
    print("Your score is B ")
elif score >= 90 and score <= 100:
    print("Your score is A ")
#else:
#    print("Input error, please type your real score.")