import csv
# For the average
from statistics import mean
from collections import OrderedDict
import operator


def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name) as csvfile:
        reader = csv.reader(csvfile)
        data = {}
        with open(output_file_name, 'w', newline='', ) as avgfile:
            for row in reader:
                # print(row)
                name = row[0]
                these_grades = list()

                for grade in row[1:]:  # because the first one is the name
                    these_grades.append(float(grade))
                #data.append(name + ',' + str(mean(these_grades)))
                # print(data)
                avg = mean(these_grades)
                data.update({name: avg})
            writer = csv.writer(avgfile, delimiter=",")
            writer.writerows(data.items())
        avgfile.close()
    csvfile.close()


def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name) as csvfile:
        reader = csv.reader(csvfile)
        data = OrderedDict()
        with open(output_file_name, 'w', newline='', ) as avgfile:
            for row in reader:
                # print(row)
                name = row[0]
                these_grades = list()
                for grade in row[1:]:  # because the first one is the name
                    these_grades.append(float(grade))
                # print(mean(these_grades))
                avg = mean(these_grades)
                data.update({name: avg})
            # print(data)
            #print(list(sorted(data.items(), key=operator.itemgetter(1))))
            #print(sorted(list(sorted(data.items(), key=operator.itemgetter(0))), key=operator.itemgetter(1)))
            writer = csv.writer(avgfile, delimiter=",")
            writer.writerows(sorted(list(sorted(data.items(), key=operator.itemgetter(0))), key=operator.itemgetter(1)))

        avgfile.close()
    csvfile.close()


def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name) as csvfile:
        reader = csv.reader(csvfile)
        data = OrderedDict()
        with open(output_file_name, 'w', newline='', ) as avgfile:
            for row in reader:
                # print(row)
                name = row[0]
                these_grades = list()
                for grade in row[1:]:  # because the first one is the name
                    these_grades.append(float(grade))
                # print(mean(these_grades))
                avg = mean(these_grades)
                data.update({name: avg})
            # print(data)
            #sorted_avg = list(sorted(data.items(), key=operator.itemgetter(1), reverse=True))
            #print(sorted_avg[:3])
            list(sorted(data.items(), key=operator.itemgetter(1)))
            sorted_avg = list(sorted(list(sorted(data.items(), key=operator.itemgetter(0))), key=operator.itemgetter(1) , reverse=True))
            writer = csv.writer(avgfile, delimiter=",")
            writer.writerows(sorted_avg[:3])

        avgfile.close()
    csvfile.close()


def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name) as csvfile:
        reader = csv.reader(csvfile)
        data = OrderedDict()
        with open(output_file_name, 'w', newline='', ) as avgfile:
            for row in reader:
                # print(row)
                name = row[0]
                these_grades = list()
                for grade in row[1:]:  # because the first one is the name
                    these_grades.append(float(grade))
                # print(mean(these_grades))
                avg = mean(these_grades)
                data.update({name: avg})
            # print(data)
            sorted_avg = list(sorted(data.items(), key=operator.itemgetter(1)))
            x = OrderedDict(sorted_avg[:3])
            list(x.values())
            #print(list(x.values()))
            writer = csv.writer(avgfile, delimiter="\n")
            writer.writerow(list(x.values()))

        avgfile.close()
    csvfile.close()


def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name) as csvfile:
        reader = csv.reader(csvfile)
        data = OrderedDict()
        with open(output_file_name, 'w') as avgfile:
            for row in reader:
                # print(row)
                name = row[0]
                these_grades = list()
                for grade in row[1:]:  # because the first one is the name
                    these_grades.append(float(grade))
                # print(mean(these_grades))
                avg = mean(these_grades)
                data.update({name: avg})
                list(data.values())
            #print(mean(list(data.values())))
            avgfile.write(str(mean(list(data.values()))))

        avgfile.close()
    csvfile.close()


in1 = r"E:\pythonexercise\grades.csv"
out1 = r"E:\pythonexercise\average.csv"
out2 = r"E:\pythonexercise\sorted_average.csv"
out3 = r"E:\pythonexercise\sorted_3average.csv"
out4 = r"E:\pythonexercise\sorted_3worstavg.csv"
out5 = r"E:\pythonexercise\avgavg.txt"
calculate_averages(in1, out1)
calculate_sorted_averages(in1, out2)
calculate_three_best(in1, out3)
calculate_three_worst(in1, out4)
calculate_average_of_averages(in1, out5)






