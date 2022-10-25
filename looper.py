import csv 

location_name = input('Enter you locations: ')
locations = location_name.split(' ')
increments = input('Increment by: ')
increments_int = int(increments)
answer = []
for i in range(len(locations)):
    single = locations[i]
    name_split = single.split("-")
    converted_num = int(name_split[3])
    for converted_num in range(increments_int):
        num = converted_num + 1
        double_digit = f'{num:02d}'
        name_split[3] = double_digit
        answer = '-'.join(name_split)
        with open('test.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([answer])
        print(answer)

        

