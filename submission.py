import requests
url='https://lf8q0kx152.execute-api.us-east-2.amazonaws.com/default/computeFitnessScore'
x=requests.post(url,json={"qconfig":"[0 6 4 7 1 3 5 2]","userID":828101,"githubLink":"https://github.com/naeri77/Eight-Queens/blob/master/one%20solution.py"})
print(x.text)
