class Underscore:
    def map(self, iterable, callback):
        new_list = []
        for i in iterable:
            # print(f"callback(i): {callback(i)}")
            new_list.append(callback(i))
        return new_list

    def find(self, iterable, callback):
        for i in range(len(iterable)):
            # print(f"i: {i}\niterable[i]: {iterable[i]}\ncallback(i): {callback(i)}\ncallback(iterable[i]): {callback(iterable[i])}")
            if callback(iterable[i]):
                return iterable[i]
        return "Object not included in set"

    def filter(self, iterable, callback):
        new_list = []
        for i in iterable:
            # print(f"callback(i): {callback(i)}\ni: {i}")
            if callback(i):
                new_list.append(i)
        return new_list


    def reject(self, iterable, callback):
        new_list = []
        for i in iterable:
            if not callback(i):
                new_list.append(i)
        return new_list


_ = Underscore() # let's create an instance of our class, we are setting our instance to a variable that is an underscore

print("---_.map()---")
x = _.map([1,2,3], lambda x: x*2)
print(x)

print("\n\n---_.find()---")
y =  _.find([1,2,3,4,5,6], lambda x: x>4)
print(y)
y =  _.find([9, 1, 3], lambda x: x>4)
print(y)

print("\n\n---_.filter()---")
z = _.filter([1,2,3,4,5,6], lambda x: x%2==0)
print(z)

print("\n\n---_.reject()---")
r =  _.reject([1,2,3,4,5,6], lambda x: x%2==0)
print(r)


# _.map([1,2,3], lambda x: x*2) # should return [2,4,6]
# _.find([1,2,3,4,5,6], lambda x: x>4) # should return the first value that is greater than 4
# _.filter([1,2,3,4,5,6], lambda x: x%2==0) # should return [2,4,6]
# _.reject([1,2,3,4,5,6], lambda x: x%2==0) # should return [1,3,5]