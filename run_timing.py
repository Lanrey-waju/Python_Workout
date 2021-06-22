def run_timing():
    """
    Asks the userrepeatedly for their run time of 5km
    """

    number_of_runs = 0
    time_taken = 0
    while True:
        one_run = input("Enter your 5km run time in minutes: ").strip()


        if not one_run:
            break

        number_of_runs += 1
        time_taken += float(one_run)
    average_time = time_taken/number_of_runs
    print(f'Your average run time is {average_time:.2f} minutes, over {number_of_runs} runs.')


run_timing()
