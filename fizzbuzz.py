#!/usr/bin/env python3

def fizzbuzz(start,end,multiples,answers):
    #Usual programming task, used as based for testing for jenkins automation

    counters = [start % i if start % i != 0 else i for i in multiples]

    #I keep track of multiples with counters instead of doing the modulus 
    #operation because the modulus operation is slow, it is not the focus
    #of this code

    result = []
    
    for current_number in range(start,end+1):
        iteration_result = []
        for i in range(len(multiples)):
            #Because the multiples are being kept track with a list I must loop
            #the list
            if counters[i] == multiples[i]:
                #If counter matches its multiple it gets reseted to 0 and answer 
                #stored in the iteration_result list
                iteration_result.append(answers[i])
                counters[i] = 0

        if len(iteration_result) == 0:
            #If this number had no multiplicity with any number, record the
            #number in the result
            iteration_result.append(current_number)

        result.append(iteration_result)
        counters = [i+1 for i in counters]

    return result


if __name__ == "__main__":
    print("Test1")
    res = fizzbuzz(1,100,[3,5],["fizz","buzz"])
    [print(i) for i in res]
    print()
    print("Test2")
    res = fizzbuzz(1,100,[1],["PseudoTest"])
    [print(i) for i in res]
