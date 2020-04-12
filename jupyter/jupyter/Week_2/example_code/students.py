import someCallsToImport


def run():
    someData = someCallsToImport.makeInfo(n=5)

    for name, grades in someData.items():
        print("{} has an average grade of {}".format(name, someCallsToImport.getAverage(grades)))


if __name__ == '__main__':
    run()
