def main ():
    answer=input("Describe how you are feeling using an emotican ")
    print(convert(answer))
def convert(feedback):
    return(feedback.replace(':)', '🙂').replace (':(', '🙁'))

main()
