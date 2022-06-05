import csv

def test(username, password):
    with open('test.csv', 'r') as test:
        for row in csv.DictReader(test):
            if row["Username"] == username:
                if row["Password"] == password:
                    return 'Logged In Successfully!'
                    

def add_acc(username, password):
    format = "\n{username},{password},0".format(username=username, password=password)
    with open('test.csv', 'a') as test:
        test.write(format)


