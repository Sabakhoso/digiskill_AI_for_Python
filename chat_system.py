class User:
    def __init__(self, username):
        self.username = username
    def __str__(self):
        return self.username

class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
    
    def format_message(self):
        return f"{self.sender}:{self.content}"
    
class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []
        self.history = []

    def join_room(self, user):
        if user not in self.users:
            self.users.append(user)
            print(f"---{user.username} joined {self.room_name}")
    
    def leave_room(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"---{user.username} left the room---")
    
    def send_message(self, user, text):
        if user in self.users:
            new_msg = Message(user.username, text)
            self.history.append(new_msg)
        else:
            print("error: user_must_join_first")
    def show_history(self):
        print(f"\n---{self.room_name} chat history---")
        for msg in self.history:
            print("-----------------------\n")

# testing the system
room = ChatRoom("vlog_sqaud")

user1 = User("alex")
user2 = User("sam")

room.join_room(user1)
room.join_room(user2)

room.send_message(user1, "Hey everyone!")
room.send_message(user2, "Yo! ready for the trip?")

room.show_history()
room.leave_room(user2)
