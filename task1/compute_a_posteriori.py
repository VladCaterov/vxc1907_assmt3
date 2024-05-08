import sys

def observationLength(observations):
    return len(observations)

def verifyObservations(observations):
    valid = ['C', 'L']
    for ch in observations:
        if ch not in valid:
            print("Invalid Observations")
            exit()

def update_posterior_probabilities(observation, posteriorProbabilities):
    '''
    P_t(hi) = P(hi |  Q1, ..., Qt)
    = P(Qt | hi) * P_t-1(h_1) / P_t(Q_t+1)
    '''
    # observationsArray = observations.split() 
    # observationCount = len(observationsArray)
    # if observationCount == 0:
    #     return priori[hypothesis]  

    # currObservedGivenHypothesis = 1
    # observationsArray.pop()
    # previousPosteriorHypothesisProb = calculatePosteriorHypothesisProb(observations, priori, hypothesis)
    # posteriorHypothesisProb = (currObservedGivenHypothesis * previousPosteriorHypothesisProb) / calculatePosteriorObservationProb(observations,priori)
    ratioIndex = 1 if observation =='C' else 2

    for hypothesis in posteriorProbabilities.values():
        probObservationGivenHypothesis = hypothesis[ratioIndex]
        previousProbilityOfHypothesis = hypothesis[0]
        observationProbability = calculate_posterior_observation_prob(observation, posteriorProbabilities)
        hypothesis[0] = (probObservationGivenHypothesis * previousProbilityOfHypothesis) /  observationProbability
    
    return posteriorProbabilities


def calculate_posterior_observation_prob(observation, posteriorProbabilities):
    ratioIndex = 1 if observation =='C' else 2
    prob = 0
    for hypothesis in posteriorProbabilities.values(): #SUMMATION
        prob += hypothesis[ratioIndex] * hypothesis[0]
    return prob

def compute_a_posteriori(observations):
    priori = { 
        "h1":[0.10000, 1, 0], # This type of bag contains 100% cherry candies.
        "h2":[0.20000, 0.75, 0.25], # This type of bag contains 75% cherry candies and 25% lime candies.
        "h3":[0.40000, 0.5, 0.5], # This type of bag contains 50% cherry candies and 50% lime candies.
        "h4":[0.20000, 0.25, 0.75], # This type of bag contains 25% cherry candies and 75% lime candies.
        "h5":[0.10000, 0, 1]# This type of bag contains 100% lime candies.
    }
    posteriorProbabilities = priori.copy()
    verifyObservations(observations)
    length = observationLength(observations)
    file = open("result.txt", 'w')

    file.write("Observation sequence Q: " + observations + '\n')
    file.write("Length of Q: " + str(length) + "\n\n")
    for i in range(length):
        observation = observations[i]

        file.write("After Observation " + str(i+1) + " = " + observation + ":\n\n")      
        posteriorProbabilities = update_posterior_probabilities(observation , posteriorProbabilities)
        for hypothesis in posteriorProbabilities:
            posteriorHypothesisProb = posteriorProbabilities[hypothesis][0]
            file.write("P(" + hypothesis + " | Q) = " + str(posteriorHypothesisProb) + "\n")
        probNextCherry = calculate_posterior_observation_prob('C', posteriorProbabilities)
        probNextLime = calculate_posterior_observation_prob('L', posteriorProbabilities)
        file.write("\nProbability that the next candy we pick will be C, given Q: " + str(probNextCherry) + '\n')  
        file.write("Probability that the next candy we pick will be L, given Q: " + str(probNextLime) + "\n\n")  
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
