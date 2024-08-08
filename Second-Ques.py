from collections import deque, defaultdict

class SocialNetwork:
    def __init__(self):
        self.network = defaultdict(set)
    
    def add_friendship(self, person1, person2):
        self.network[person1].add(person2)
        self.network[person2].add(person1)
    
    def get_friends(self, person):
        return self.network.get(person, set())
    
    def common_friends(self, person1, person2):
        return self.get_friends(person1).intersection(self.get_friends(person2))
    
    def nth_connection(self, person1, person2):
        if person1 == person2:
            return 0
        
        queue = deque([(person1, 0)])
        visited = set([person1])
        
        while queue:
            current_person, level = queue.popleft()
            for friend in self.network[current_person]:
                if friend == person2:
                    return level + 1
                if friend not in visited:
                    visited.add(friend)
                    queue.append((friend, level + 1))
        
        return -1

def main():
    network = SocialNetwork()
    while True:
        print("Add a friendship (or type 'done' to finish):")
        person1 = input("Enter the first person's name: ").strip()
        if person1.lower() == 'done':
            break
        person2 = input("Enter the second person's name: ").strip()
        if person2.lower() == 'done':
            break
        network.add_friendship(person1, person2)
    
    person = input("\nEnter the name of the person to find their friends: ").strip()
    friends = network.get_friends(person)
    print(f"{person}'s friends: {friends}")
    
    person1 = input("\nEnter the first person's name to find common friends: ").strip()
    person2 = input("Enter the second person's name to find common friends: ").strip()
    common = network.common_friends(person1, person2)
    print(f"Common friends of {person1} and {person2}: {common}")
    
    person1 = input("\nEnter the first person's name to find the nth connection: ").strip()
    person2 = input("Enter the second person's name to find the nth connection: ").strip()
    connection_level = network.nth_connection(person1, person2)
    print(f"{person1} and {person2} connection level: {connection_level}")

if __name__ == "__main__":
    main()
