import sys

def observationLength(observations):
    return len(observations)

def verifyObservations(observations):
    valid = ['C', 'L']
    for ch in observations:
        if ch not in valid:
            print("Invalid Observations")
            exit()

def calculatePosteriorHypothesisProb(observations, priori, hypothesis):
    '''
    P_t(hi) = P(hi |  Q1, ..., Qt)
    = P(Qt | hi) * P_t-1(h_1) / P_t(Q_t+1)
    '''
    
    
    observationCount = len(observations)
    if observationCount == 0:
        return priori[hypothesis]  
    if observations[observationCount - 1] == 'C':

    previousPosteriorHypothesisProb = calculatePosteriorHypothesisProb(observations[0:observationCount - 1], priori, hypothesis)
    posteriorHypothesisProb = (currObservedGivenHypothesis * previousPosteriorHypothesisProb) / calculatePosteriorObservationProb(observations[0:observationCount - 1],priori, observations[observationCount - 1])

    
        
   
    return posteriorHypothesisProb
def calculatePosteriorObservationProb(observations, priori, nextCandyType):    
    sum = 1
    # for hypothesis in priori:
    #     for observation in observations:
    #         if nextCandyType == 'C':
    #             if hypothesis == "h1":
    #                 sum += 1 * calculatePosteriorHypothesisProb(observations, priori, hypothesis)
    #             elif hypothesis == "h2":
    #                 sum += priori[hypothesis] * calculatePosteriorHypothesisProb(observations, priori, hypothesis)
    #             elif hypothesis == "h3":
    #                         sum += priori[hypothesis] * calculatePosteriorHypothesisProb(observations, priori, hypothesis)
    #             elif hypothesis == "h4":
    #                         sum += priori[hypothesis] * calculatePosteriorHypothesisProb(observations, priori, hypothesis)
    #             elif hypothesis == "h5":
    #                         sum += 0
        
    #         else: # nextCandyType == 'L'
    #             if hypothesis == "h1":
    #                 sum += 0 * calculatePosteriorHypothesisProb(observations, priori, hypothesis)
    #             elif hypothesis == "h2":
    #                 sum += priori[hypothesis] * calculatePosteriorHypothesisProb(observations, priori, hypothesis)
    #             elif hypothesis == "h3":
    #                         sum += priori[hypothesis] * calculatePosteriorHypothesisProb(observations, priori, hypothesis)
    #             elif hypothesis == "h4":
    #                         sum += priori[hypothesis] * calculatePosteriorHypothesisProb(observations, priori, hypothesis)
    #             elif hypothesis == "h5":
    #                         sum += 1 * calculatePosteriorHypothesisProb(observations, priori, hypothesis)
    return sum

def compute_a_posteriori(observations):
    priori = {
        "h1":0.10000, # This type of bag contains 100% cherry candies.
        "h2":0.20000, # This type of bag contains 75% cherry candies and 25% lime candies.
        "h3":0.40000, # This type of bag contains 50% cherry candies and 50% lime candies.
        "h4":0.20000, # This type of bag contains 25% cherry candies and 75% lime candies.
        "h5":0.10000 # This type of bag contains 100% lime candies.
    }
    verifyObservations(observations)
    length = observationLength(observations)
    file = open("result.txt", 'w')

    file.write("Observation sequence Q: " + observations + '\n')
    file.write("Length of Q: " + str(length) + "\n\n")
    for i in range (1,length+1):
        currObservation = observations[i - 1] 
        file.write("After Observation " + str(i) + " = " + currObservation + ":\n\n")
        for hyp in priori:
            posteriorHypothesisProb = calculatePosteriorHypothesisProb(observations, priori, hyp)
            file.write("P(" + hyp + " | Q) = " + str(posteriorHypothesisProb) + "\n")

        condProb1 = calculatePosteriorObservationProb(observations, priori)
        condProb2 = 1 - condProb2
        file.write("\nProbability that the next candy we pick will be C, given Q: " + str(condProb1) + '\n')  
        file.write("Probability that the next candy we pick will be L, given Q: " + str(condProb2) + "\n\n")  
    file.close()

if  __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Insufficient Arguments")
        exit()
    else:
        program = argv[0]
        observations = argv[1]
        compute_a_posteriori(observations)
