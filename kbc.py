print(".....................welcome in kbc 🙏....................")
print()
print("......lets start play game..all the best.👍......")
print()
def que_list():
    question_list=[
        "1.how many continents are there?"
        ,"2.what is the capital of india?"
        ,"3.in campus which course we are learning?"
        ,"4.who is the CEO of Navgurukul?"
        ]
    return question_list
que = que_list()

def opt_list():
    options_list=[
    ["1.four","2.nine","3.seven","4.eight"]
    ,["1.mumbai","2.delhi","3.simla","4.bhopal"]
    ,["1.software enjeneering","2.graphic design","3.mbbs","4.tourism"]
    ,["1.Abhishek Gupta","2.Rishabh","3.Anuradha","4.Swati"]
    ]
    return options_list
ope=opt_list()

def answer_list():
    ans_list=[3,2,1,1]
    return ans_list
answer=answer_list()

def lifeline():
    options_list1=[["nine","seven"],["delhi","simla"],["software enjeneering","mbbs"],["Abhishek Gupta","Rishabh"]]
    return options_list1
life=lifeline()

def answer_list1():
    ans_list=[2,1,1,1]
    return ans_list
answer1=answer_list1()
sum=0
i=0
count=1
while i<len(que):
    print(que[i])
    j=0
    while j<len(ope[i]):
        print(ope[i][j])
        j=j+1
    if count<=1:
        lifeline2=input("enter any aswer or use lifeline: ")
        if lifeline2=="yes":
            k=0
            index3=1
            while k<len(life[i]):
                print(index3,life[i][k])
                index3=index3+1
                k=k+1
            num=int(input("enter the answer: "))
            if num==answer1[i]:
                sum=sum+2000
                print("your answer is right:")
                print("you win this: ",sum)
            else:
                print("your answer is wrong:")
                print("game over",sum)
                break
            count=count+1
        else:
            num=int(input("enter your answer: "))
            if num==answer[i]:
                sum=sum+2000
                print("right answer")
                print("you win this",sum)
            else:
                print("your answer is wrong")
                print("game over",sum)
                break
    else:
        num=int(input("enter your answer: "))
        if num==answer[i]:
            sum=sum+2000
            print("right answer:")
            print("you win this: ",sum)
        else:
            print("your answer is wrong:")
            print("game over:",sum)
            break
    i=i+1

