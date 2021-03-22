from random import randint, uniform
from math import trunc
from time import sleep

growth_dictionary = { "youtuber1": [], "youtuber2": [] }

while True:
    print("---  YOUTUBER 1  ---\n\n THIS YOUTUBER NEEDS TO BE THE LESS SUBSCRIBED\n")

    youtuber1_name = input("Name of the first youtuber: ")
    youtuber1_subscriber_count = int(input("Subscribers of the first youtuber: "))
    youtuber1_average_growth = int(input("Average growth of the first youtuber: "))

    print("--- YOUTUBER 2 ---\n\n THIS YOUTUBER NEEDS TO BE THE MORE SUBSCRIBED\n")

    youtuber2_name = input("Name of the second youtuber: ")
    youtuber2_subscriber_count = int(input("Subscribers of the second youtuber: "))
    youtuber2_average_growth = int(input("Average growth of the second youtuber: "))

    day = 0
    difference = 0
    
    while difference > -1000000:
        youtuber1_growth = randint(trunc(youtuber1_average_growth * 0.7), trunc(youtuber1_average_growth * 1.4))

        youtuber1_subscriber_count += youtuber1_growth

        youtuber2_growth = randint(trunc(youtuber2_average_growth * 0.7), trunc(youtuber2_average_growth * 1.4))

        youtuber2_subscriber_count += youtuber2_growth

        low_critical_difference = True if difference < 1000000 else False
        critical_difference = True if difference < 300000 else False
        high_critical_difference = True if difference < 100000 else False
        video_today = True if randint(1, 2) == 1 else False
        influencer_help = 0

        if high_critical_difference:
            youtuber2_additional_growth = trunc(youtuber2_growth / uniform(0.1, 0.6))
            youtuber2_subscriber_count += youtuber2_additional_growth
            youtuber2_growth += youtuber2_additional_growth
            youtuber2_average_growth -= trunc(youtuber2_average_growth / 125)
            
            if difference > 0:
                if difference < 20000:
                    influencer_help = True if randint(1, 3) == 1 else False
                else:
                    influencer_help = True if randint(1, 6) == 1 else False
        elif critical_difference:
            youtuber2_additional_growth = trunc(youtuber2_growth / uniform(0.1, 1.0))
            youtuber2_subscriber_count += youtuber2_additional_growth
            youtuber2_growth += youtuber2_additional_growth
            youtuber2_average_growth -= trunc(youtuber2_average_growth / 125)
            
            influencer_help = True if randint(1, 20) == 1 else False
        elif low_critical_difference:
            youtuber2_additional_growth = trunc(youtuber2_growth / uniform(0.1, 2.2))
            youtuber2_subscriber_count += youtuber2_additional_growth
            youtuber2_growth += youtuber2_additional_growth
            youtuber2_average_growth -= trunc(youtuber2_average_growth / 125)

        if video_today:
            youtuber2_additional_growth = trunc(youtuber2_growth / uniform(0.5, 5))
            youtuber2_subscriber_count += youtuber2_additional_growth
            youtuber2_growth += youtuber2_additional_growth
        
        if influencer_help:
            youtuber2_additional_growth = trunc(youtuber2_growth / uniform(0.2, 1.5))
            youtuber2_subscriber_count += youtuber2_additional_growth
            youtuber2_growth += youtuber2_additional_growth
        
        if -100000 < difference < 1000000:
            war = True
        else:
            war = False

        if war:
            if youtuber2_growth > youtuber1_growth * 3:
                youtuber2_subscriber_count -= trunc(youtuber2_growth / 1.5)
                youtuber2_growth -= trunc(youtuber2_growth / 1.5)
            elif youtuber2_growth < youtuber1_growth / 2:
                youtuber2_subscriber_count += trunc(youtuber2_growth / 1.4)
                youtuber2_growth += trunc(youtuber2_growth / 1.4)

        difference = youtuber2_subscriber_count - youtuber1_subscriber_count

        if len(growth_dictionary["youtuber1"]) > 1 and int(growth_dictionary["youtuber1"][-2]) > int(growth_dictionary["youtuber1"][-1]):
            youtuber1_additional_growth = trunc(youtuber1_growth / 10)
            youtuber1_subscriber_count -= youtuber1_additional_growth
            youtuber1_growth -= youtuber1_additional_growth
        elif len(growth_dictionary["youtuber1"]) > 1 and int(growth_dictionary["youtuber1"][-2]) < int(growth_dictionary["youtuber1"][-1]):
            youtuber1_additional_growth = trunc(youtuber1_growth / 6)
            youtuber1_subscriber_count += youtuber1_additional_growth
            youtuber1_growth += youtuber1_additional_growth

        if len(growth_dictionary["youtuber2"]) > 1 and int(growth_dictionary["youtuber2"][-2]) > int(growth_dictionary["youtuber2"][-1]):
            youtuber2_additional_growth = trunc(youtuber2_growth / 10)
            youtuber2_subscriber_count -= youtuber2_additional_growth
            youtuber2_growth -= youtuber2_additional_growth
        elif len(growth_dictionary["youtuber2"]) > 1 and int(growth_dictionary["youtuber2"][-2]) < int(growth_dictionary["youtuber2"][-1]):
            youtuber2_additional_growth = trunc(youtuber2_growth / 6)
            youtuber2_subscriber_count += youtuber2_additional_growth
            youtuber2_growth += youtuber2_additional_growth

        if youtuber1_growth > difference and difference > -50000:
            youtuber2_additional_growth = randint(trunc(youtuber1_growth / 3), trunc(youtuber1_growth / 1.5))
            youtuber2_subscriber_count += youtuber2_additional_growth
            youtuber2_growth += youtuber2_additional_growth

        growth_dictionary["youtuber1"].append(str(youtuber1_growth))
        growth_dictionary["youtuber2"].append(str(youtuber2_growth))

        print(f"{youtuber1_name} has {youtuber1_subscriber_count} subscribers.\n{youtuber1_name} gained {youtuber1_growth} subscribers today.\n\n")
        print(f"{youtuber2_name} has {youtuber2_subscriber_count} subscribers.\n{youtuber2_name} gained {youtuber2_growth} subscribers today.\n\n")

        difference = youtuber2_subscriber_count - youtuber1_subscriber_count
        
        print(f"Difference = {difference}")

        day += 1 

        print(f"Day = {day}\n")

        if video_today:
            print("Video today!")
        
        if influencer_help:
            print("A influencer helped!")

        temp = youtuber1_subscriber_count
        temp2 = youtuber2_subscriber_count

        if youtuber1_growth > youtuber2_growth and difference > 0:
            for i in range(0, 1002):
                temp += youtuber1_growth
                temp2 += youtuber2_growth

                if temp > temp2:
                    print(f"It is expected that {youtuber1_name} will surpass {youtuber2_name} in {i} days.")
                    break
                elif i > 1000:
                    print(f"It is expected that {youtuber1_name} will surpass {youtuber2_name} in more than 1000 days.")

        sleep(4)

    print(f"{youtuber1_name}:\n\n{growth_dictionary['youtuber1']}\n\n{youtuber2_name}:\n\n{growth_dictionary['youtuber2']}")
