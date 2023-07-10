import csv
from jinja2 import Template

attributes = ["Name", "MPG", "Cylinders", "Displacement", "Horsepower", "Weight", "Acceleration", "Model", "Origin"]
diclist = []

with open('cars.csv', mode = 'r') as cars:
    carfile = csv.reader(cars, delimiter = ';')
    line_count = 0

    for each in carfile:
        if line_count == 0 or line_count == 1:
            line_count = line_count + 1
        else: 
            dic = {}
            n = 0
            for word in each:
                if n == 0:
                    dic[attributes[n]] = str(word)
                elif n == 1:
                    dic[attributes[n]] = float(word)
                elif n == 2:
                    dic[attributes[n]] = int(word)
                elif n == 3:
                    dic[attributes[n]] = float(word)
                elif n == 4:
                    dic[attributes[n]] = float(word)
                elif n == 5:
                    dic[attributes[n]] = float(word)
                elif n == 6:
                    dic[attributes[n]] = float(word)
                elif n == 7:
                    dic[attributes[n]] = int(word)
                else:
                    dic[attributes[n]] = str(word)
                n = n + 1

            diclist.append(dic)
            
cars.close()
def main():
    tfile = open('carstemplate.html.jinja2', 'r')
    TEMPLATE = tfile.read()
    tfile.close()
    obj1 = Template(TEMPLATE)
    content = obj1.render(diclist = diclist)
    file = open('cars.html', mode = 'w')
    file.write(content)
    file.close()
    

if __name__ == "__main__":
    main()

            
