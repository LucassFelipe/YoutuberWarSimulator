from random import randint
from time import sleep


# dictionary that all the registered growths will be stored here
growth_dict = { 'youtuber1': [], 'youtuber2': [] }

print("""
--- YOUTUBER 1 ---

This is the youtuber that is about to surpass the second youtuber
This youtuber needs to have less subscribers, but with more subscriber growth
""")

youtuber1_name = input('Name of the first youtuber: ')
youtuber1_subscriber_count = input('Subscriber count of the first youtuber: ')
youtuber1_average_growth = input('Average growth of the first youtuber: ')

print("""
--- YOUTUBER 2 ---

This is the youtuber that is about to get surpassed by the first youtuber
This youtuber needs to have more subscribers, but with less subscriber growth
""")

youtuber2_name = input('Name of the second youtuber: ')
youtuber2_subscriber_count = input('Subscriber count of the second youtuber: ')
youtuber2_average_growth = input('Average growth of the second youtuber: ')

if youtuber1_subscriber_count.isnumeric() and youtuber1_average_growth.isnumeric() and youtuber2_subscriber_count.isnumeric() and youtuber2_average_growth.isnumeric():
    youtuber1_subscriber_count = int(youtuber1_subscriber_count)
    youtuber1_average_growth = int(youtuber1_average_growth)

    youtuber2_subscriber_count = int(youtuber2_subscriber_count)
    youtuber2_average_growth = int(youtuber2_average_growth)

    instantly = input('Type "i" if you want to simulate this instantly: ').lower().strip()

    day = 0
    subgap = youtuber2_subscriber_count - youtuber1_subscriber_count
    base_subgap = 0
    subwar = False

    while True:
        # a youtuber daily growth is not static, am I right? These statements will variate the growth a little
        youtuber1_growth = randint(round(youtuber1_average_growth * 0.8), round(youtuber1_average_growth * 1.2))
        youtuber1_subscriber_count += youtuber1_growth

        youtuber2_growth = randint(round(youtuber2_average_growth * 0.8), round(youtuber2_average_growth * 1.2))
        youtuber2_subscriber_count += youtuber2_growth

        # the community will start a subscriber war when the sub gap is
        # lower than 1% of it's favorite youtuber subscriber count
        if -youtuber2_subscriber_count / 100 < subgap < youtuber2_subscriber_count / 100:
            subwar = True

        # this will be used to perform some calculations on the growth
        if base_subgap == 0:
            base_subgap = subgap

        # all the stuff that will happen with the growth and subcounts when the war is happening
        if subwar:
            youtuber2_additional_growth = round(abs(youtuber2_growth + youtuber2_average_growth * (base_subgap / subgap)))
            youtuber2_subscriber_count += youtuber2_additional_growth
            youtuber2_growth += youtuber2_additional_growth
            youtuber2_average_growth *= 0.99
        
        growth_dict["youtuber1"].append(str(youtuber1_growth))
        growth_dict["youtuber2"].append(str(youtuber2_growth))

        # Adjusting the growth to be smoother
        if len(growth_dict['youtuber1']) > 1:
            if int(growth_dict['youtuber1'][-2]) > int(growth_dict['youtuber1'][-1]):
                youtuber1_subscriber_count -= round((int(growth_dict['youtuber1'][-2]) - int(growth_dict['youtuber1'][-1])) / 2)
                youtuber1_growth -= round((int(growth_dict['youtuber1'][-2]) - int(growth_dict['youtuber1'][-1])) / 2)
            elif int(growth_dict['youtuber1'][-2]) < int(growth_dict['youtuber1'][-1]):
                youtuber1_subscriber_count += round((int(growth_dict['youtuber1'][-1]) - int(growth_dict['youtuber1'][-2])) / 2)
                youtuber1_growth += round((int(growth_dict['youtuber1'][-1]) - int(growth_dict['youtuber1'][-2])) / 2)

            if int(growth_dict['youtuber2'][-2]) > int(growth_dict['youtuber2'][-1]):
                youtuber1_subscriber_count -= round((int(growth_dict['youtuber2'][-2]) - int(growth_dict['youtuber2'][-1])) / 2)
                youtuber1_growth -= round((int(growth_dict['youtuber2'][-2]) - int(growth_dict['youtuber2'][-1])) / 2)
            elif int(growth_dict['youtuber2'][-2]) < int(growth_dict['youtuber2'][-1]):
                youtuber1_subscriber_count += round((int(growth_dict['youtuber2'][-1]) - int(growth_dict['youtuber2'][-2])) / 2)
                youtuber1_growth += round((int(growth_dict['youtuber2'][-1]) - int(growth_dict['youtuber2'][-2])) / 2)

        day += 1
        subgap = youtuber2_subscriber_count - youtuber1_subscriber_count

        print(f"""
{youtuber1_name} has {youtuber1_subscriber_count} subscribers.
{youtuber1_name} gained {youtuber1_growth} subscribers today.

{youtuber2_name} has {youtuber2_subscriber_count} subscribers.
{youtuber2_name} gained {youtuber2_growth} subscribers today.

Sub gap: {subgap}
Day: {day}
""")

        if instantly != 'i':
            sleep(3)

        # the subwar is over, subgap too low
        if subgap < 0 and subgap < -youtuber2_subscriber_count / 100:
            break

    print(f"""
{youtuber1_name}:

{growth_dict['youtuber1']}

{youtuber2_name}:

{growth_dict['youtuber2']}
""")
else:
    print('Enter valid numbers!!!')
