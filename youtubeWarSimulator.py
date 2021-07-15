from time import sleep
from random import randint, uniform

print("---  YOUTUBER 1  ---\n\n THIS YOUTUBER NEEDS TO BE THE LEAST SUBSCRIBED AND WITH THE HIGHEST SUBSCRIBER GROWTH, LIKE T-SERIES.\n")

youtuber1_name = input("Name of the first youtuber: ")
youtuber1_subscriber_count = int(input("Subscribers of the first youtuber: "))
youtuber1_average_growth = int(input("Average growth of the first youtuber: "))

print("--- YOUTUBER 2 ---\n\n THIS YOUTUBER NEEDS TO BE THE MORE SUBSCRIBED AND WITH THE SMALLEST SUBSCRIBER GROWTH, LIKE PEWDIEPIE.\n")

youtuber2_name = input("Name of the second youtuber: ")
youtuber2_subscriber_count = int(input("Subscribers of the second youtuber: "))
youtuber2_average_growth = int(input("Average growth of the second youtuber: "))

war = False
day = 0
difference = 0

while difference > -200000:
    youtuber1_growth = randint(round(youtuber1_average_growth * 0.7), round(youtuber1_average_growth * 1.4))

    youtuber1_subscriber_count += youtuber1_growth

    youtuber2_growth = randint(round(youtuber2_average_growth * 0.7), round(youtuber2_average_growth * 1.4))

    youtuber2_subscriber_count += youtuber2_growth

    difference = youtuber2_subscriber_count - youtuber1_subscriber_count

    low_critical_difference = True if difference < 500000 else False
    critical_difference = True if difference < 100000 else False
    high_critical_difference = True if difference < 50000 else False
    video_today = True if randint(1, 2) == 1 else False
    influencer_help = True if randint(1, 20) == 1 else False

    if high_critical_difference:
        youtuber2_additional_growth = round(youtuber2_growth / uniform(0.1, 0.6))
        youtuber2_subscriber_count += youtuber2_additional_growth
        youtuber2_growth += youtuber2_additional_growth
        youtuber2_average_growth -= round(youtuber2_average_growth / 100)
    elif critical_difference:
        youtuber2_additional_growth = round(youtuber2_growth / uniform(0.1, 1.0))
        youtuber2_subscriber_count += youtuber2_additional_growth
        youtuber2_growth += youtuber2_additional_growth
        youtuber2_average_growth -= round(youtuber2_average_growth / 100) 
    elif low_critical_difference:
        war = True
        youtuber2_additional_growth = round(youtuber2_growth / uniform(0.1, 2.2))
        youtuber2_subscriber_count += youtuber2_additional_growth
        youtuber2_growth += youtuber2_additional_growth
        youtuber2_average_growth -= round(youtuber2_average_growth / 100)

    if video_today:
        youtuber2_additional_growth = round(youtuber2_growth / uniform(0.5, 5))
        youtuber2_subscriber_count += youtuber2_additional_growth
        youtuber2_growth += youtuber2_additional_growth
    
    if influencer_help:
        youtuber2_additional_growth = round(youtuber2_growth / uniform(0.2, 1.5))
        youtuber2_subscriber_count += youtuber2_additional_growth
        youtuber2_growth += youtuber2_additional_growth
        
    if war:
        if youtuber2_growth > youtuber1_growth * 3:
            youtuber2_growth = round(youtuber2_growth / 2)
            youtuber2_subscriber_count -= youtuber2_growth
        elif youtuber2_growth < youtuber1_growth / 2:
            youtuber2_subscriber_count += round(youtuber2_growth / 2)
            youtuber2_growth += round(youtuber2_growth / 2)

    difference = youtuber2_subscriber_count - youtuber1_subscriber_count

    print(f"{youtuber1_name} has {youtuber1_subscriber_count} subscribers.\nAnd gained {youtuber1_growth} subscribers today.\n\n")
    print(f"{youtuber2_name} has {youtuber2_subscriber_count} subscribers.\nAnd gained {youtuber2_growth} subscribers today.\n\n")

    print(f"Difference = {difference}")

    day += 1 

    print(f"Day = {day}\n")

    sleep(4)
