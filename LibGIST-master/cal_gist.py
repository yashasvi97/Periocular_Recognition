train = open('G_feature_train')
test = open('G_feature_test')
train_list = []
test_list = []
for x in train:
	train_list.append(float(x[:len(x)-1]))
for x in test:
	test_list.append(float(x[:len(x)-1]))
# print(type(train_list))
# print(len(train_list))
pta = [(i - j)**2 for i, j in zip(train_list, test_list)]
sm = sum(pta)
# print(len(pta))
# print(pta)
# for x,y in train,test:
# 	diff = (x-y)**2
# 	sm += diff
print("Gist sum EU: " + str(sm))