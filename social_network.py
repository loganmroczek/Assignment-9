class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    def __init__(self, name):
        self.name = name
        self.friends = []


    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    def __init__(self):
        self.people = {}


    def add_person(self, name):
        if name not in self.people:
            self.people[name] = Person(name)


    def add_friendship(self, person1_name, person2_name):
        if person1_name == person2_name:
            print("A person cannot be friends with themselves")
            return

        if person1_name in self.people and person2_name in self.people:
            person1 = self.people[person1_name]
            person2 = self.people[person2_name]

            person1.add_friend(person2)
            person2.add_friend(person1)

        else:
            print(f"One or both of the people don't have accounts")


    def print_network(self):
        for name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]
            
            friends = ", ".join(friend_names)
            print(f"{name}: {friends}")



# Test your code here
alex = Person("Alex")
jordan = Person("Jordan")
print(alex.friends)
alex.add_friend(jordan)
print(alex.friends[0].name)  # Jordan


network = SocialNetwork()

# Add people
network.add_person("Alex")
network.add_person("Jordan") 
network.add_person("Morgan")

# Create friendships
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")  # Error: Taylor doesn't exist

network.print_network()


"""
Design Memo

    Why is a graph the right structure to represent a social network?
    Why wouldn't a list or tree work as well for this?
    What performance or structural trade-offs did you notice when adding friends or printing the network?

A graph is the right structure to represent a social network because it has many nodes that require multiple peer-to-peer, bidirectional relationships to be represented.
Each person has friends, who have their own friends, which expands into a large network of relationships that need to be represented.

A list or tree doesn't work well for this because they can't represent multiple flat relationships for each person. A list only has linear one-to-one connections, and
there is no clear root person or hierarchy to be represented in a tree, which is the other data structure we have learned that has one-to-many relationships. A graph 
maintains a non-linear structure without the requirement for a hierarchy.

I did not notice any immediate performance issues or obvious structural tradeoffs when adding friends or printing the network, but I did not test beyond a couple of 
people. As the list of friends grows, the check for “if friend not in self.friends” is going to grow increasingly large and has O(n) time complexity. It may be more 
efficient to use a set for self.friends, and I actually considered this, but the test conditions in the ReadMe had print(alex.friends[0].name), which is not possible in 
a set because it is not indexed. I left it as a list because of this. Also, the print_network function loops through one list for every person, then another for every 
friend of that person, so that process can also get very costly, very quickly, with a large social network. However, I'm not certain how else to accomplish printing the 
network besides this double loop. 
"""