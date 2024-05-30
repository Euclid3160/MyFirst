#User will enter their age in years here
x = int(input("what is your age in years: "))

#This will let the user know what they are old enough for
if x > 15:
    print ("You are old enough to drive!")
    if x > 17:
        print ("You are old enough to vote!")
        if x > 20:
            print ("You can buy alcohol legally!")
            if x > 64:
                print ("You are eligable for a senior discount!")
            else:
                print ("You are not eligable for a senior disount.")
        else:
            print ("You can not buy alcohol legally.\nYou are not eligable for a senior discount.")
    else:
        print ("You can not vote legally.\nYou can not buy alcohol legally.\nYou are not eligable for a senior discount.")
else:
    print ("You are not old enough for a drivers license.\nYou can not vote legally.\nYou can not buy alcohol legally. \nYou are not eligable for a senior discount.")