import random
class Environment(object):
    def _init_(self):
        self.locationCondition = {'A': '0', 'B': '0'}
        self.locationCondition['A'] = random.randint(0, 1)
        self.locationCondition['B'] = random.randint(0, 1)
class SimpleReflexVacuumAgent(Environment):
    def _init_(self, Environment):
        print (Environment.locationCondition)
        Score = 0
        vacuumLocation = random.randint(0, 1)
        if vacuumLocation == 0:
            print ("Vacuum is randomly placed at Location A")
            if Environment.locationCondition['A'] == 1:
                print ("Location A is Dirty. ")
                Environment.locationCondition['A'] = 0;
                Score += 1
                print ("Location A has been Cleaned. :D")
                if Environment.locationCondition['B'] == 1:
                    print ("Location B is Dirty.")
                    print ("Moving to Location B...")
                    Score -= 1
                    Environment.locationCondition['B'] = 0;
                    Score += 1
                    print ("Location B has been Cleaned :D.")
            else:
                if Environment.locationCondition['B'] == 1:
                    print ("Location B is Dirty.")
                    Score -= 1
                    print ("Moving to Location B...")
                    Environment.locationCondition['B'] = 0;
                    Score += 1
                    print ("Location B has been Cleaned. :D")
        elif vacuumLocation == 1:
            print ("Vacuum is randomly placed at Location B. ")
            if Environment.locationCondition['B'] == 1:
                print ("Location B is Dirty")
                Environment.locationCondition['B'] = 0;
                Score += 1
                print ("Location B has been Cleaned")
                if Environment.locationCondition['A'] == 1:
                    print ("Location A is Dirty")
                    Score -= 1
                    print ("Moving to Location A")
                    Environment.locationCondition['A'] = 0;
                    Score += 1
                    print ("Location A has been Cleaned")
            else:
                if Environment.locationCondition['A'] == 1:
                    print ("Location A is Dirty")
                    print ("Moving to Location A")
                    Score -= 1
                    Environment.locationCondition['A'] = 0;
                    Score += 1
                    print ("Location A has been Cleaned")
        print (Environment.locationCondition)
        print ("Performance Measurement: " + str(Score))
theEnvironment = Environment()
theVacuum = SimpleReflexVacuumAgent(theEnvironment)