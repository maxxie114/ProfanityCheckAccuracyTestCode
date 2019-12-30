from profanity_check import predict, predict_prob

# This program test an open source AI profanity check API
# https://github.com/vzhou842/profanity-check

def mean(numLst):
  """This function calculate the mean of a list of numbers"""
  total = 0
  length = len(numLst)
  for i in numLst:
    total += i
  return total/length

def calculateAccuracy(real, expected):
  """
  This function calculate the accuracy of the prediction and return a percentage, by comparing the predicted data with 
  the expected data

  real - a list of number of the predicted result, that is either 1 or 0
  expected - a list of number of the expected result

  both input should be the same length
  """
  # print("debug: real:", real)
  # print("debug: expected:", expected)
  result = []
  percentage = 0
  for i in range(len(expected)):
    result.append(real[i] ^ expected[i])
  # print("debug: result:", result)
  return (1 - mean(result))*100

a = [0,1,0,1,0,0,1,1,0,0,0,1]
b = [1,1,1,1,0,0,1,0,1,1,1,1]
#   [0,1,0,1,1,1,1,0,0,0,0,1]

print("test calculateAccuracy(): real:{real}, expected:{expected}".format(real=calculateAccuracy(a,b),expected=50.0))

sentences = [
"go to hell, you scumm",    # 1
"fk u bitch, I hope u die!", # 1
"I will kill u", # 1
"asshole", # 1
"this is not profanity", # 0
"hi, this is Max", # 0
"you are complete shit", # 1
"oh shit, this is bad...", # 0
"fuuuuuuuuuuuuuuuuuuu", # 1
"fukkkkkkkkkkkkkkkkkkk", # 1
"fck off!", # 1
"you are an idiot!" # 1
]

expectedResult = [1,1,1,1,0,0,1,0,1,1,1,1]
# expectedResult = [0,0,0,0,0,0,0,0,0,0,0,0]
print("=============================================================================================")
print("printing all test cases:")
for i in sentences:
  print(i)

# exact prediction
print("Exact prediction, the Algorithm come up with a number of either 1(true) or 0(false)")
print("Exact prediction result:")
exact = predict(sentences)
newexact = []
for i in exact:
  newexact.append(i)
print(newexact)
print("exact prediction accuracy: {0:.2f}".format(calculateAccuracy(newexact, expectedResult)))
print("==============================================================================================")
# probability prediction
# This part of the test expect probability result to be 20
print("Probability prediction: the Algorithm come up with a floating point number between 1 and 0")
print("In this test, any probability below 0.1 is interpreted as no, while anything above 0.1 is interpreted otherwise")
prob= predict_prob(sentences)
print("Probability prediction result in floating point:")
print(prob)
print("Probability prediction result in integer(a > 0.1 => 1, a < 0.1 => 0)")
newprob = []
# result > 0.5 = Yes = 1
# result < 0.5 = No = 0
for i in prob:
  if i >= 0.1:
    newprob.append(1)
  elif i < 0.1:
    newprob.append(0)
print(newprob)
print("probability prediction accuracy: {0:.2f}".format(calculateAccuracy(newprob, expectedResult)))
print("===============================================================================================")
