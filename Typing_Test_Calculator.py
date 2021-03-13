import time

print("Please enter to start typing and once you finished the typing press enter:")
start=input("")
if start=="":
    count=0
    letters=0
    correct=0
    time_seconds=int(time.strftime("%S"))
    time_minutes=int(time.strftime("%M"))
    print("write the following paragraph")
    print("***************************************************************************************")
    paragraph="The topic that I have selected for my research is Influence of media violation on violent nature of society, the reason for selecting this topic is because the topic is much related to the society from where I am, and media has directly impact on us. Yes, I am talking about Pakistan and the role of media can’t be ignored. As all of you knows, there are clashes between Pakistan and India regarding Kashmir issue. Now, the interesting thing is Pakistani media represent it in a different way and Indian media represent it in different way. According to Pakistani media the people of Kashmir wants to join Pakistan and the Indian army had force fully occupied the Kashmir. Also, it claims how the Indian army are treating Kashmiri People (punishing, harassing, raping women, killing many people) (Khan, 2019). Pakistani media represents the violence that the Indian Army creates in Kashmir while on the other hand, when we look at the Indian Media, it shows us how Kashmiri people are happy with their lives and being part of India.  I want to know how both medias (Pakistani and Indian) impact the people of Kashmir. And how both medias impact the mindsets of Paksitani and Indian people. According to Meenakshi Ganguly , “India and Pakistan blame each other for human rights violations in Kashimir while ignoring their own responsibility for abuses.” (Ganguly, 2019)"
    print(paragraph)
    print("\n\n\n")
    typing=input("")
    end_seconds=int(time.strftime("%S"))
    end_minutes=int(time.strftime("%M"))
    total_time=(end_minutes+end_seconds/60)-(time_minutes+time_seconds/60)
    time_in_seconds=(end_minutes*60+end_seconds)-(time_minutes*60+time_seconds)
    for i in typing:
        if i==" ":
            count+=1
    average=count/total_time
    print(f"your speed is {average} words per minute")
    for i in typing:
        letters+=1
    for i in range(0, letters):
        if typing[i]==paragraph[i]:
            correct+=1
    average_seconds=letters/time_in_seconds
    print(f"you typing speed is {average_seconds} alphabet per second")
    print(f"number of correct alphabets were {correct}")
    incorrect=letters-correct
    print(f"number of incorrect alphabets were {incorrect}")
    accuracy=(correct/letters)*100
    print(f"your accuracy was {accuracy} ")































