class Song:
    def __init__(self, song_id, title, artist, duration):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return (f"Song ID: {self.song_id}\n"
                f"Title: {self.title}\n"
                f"Artist: {self.artist}\n"
                f"Duration: {self.duration}")

    def short_str(self):
        return f"[{self.song_id}: {self.title}]"

class Node:
    def __init__(self, song):
        self.song = song
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.count

    def insert_first(self, song):
        new_node = Node(song)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def insert_last(self, song):
        new_node = Node(song)

        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

        self.count += 1

    def insert_at(self, position, song):
        """position is 1-based: 1 = first node, size()+1 = after the last node."""
        if position < 1 or position > self.count + 1:
            return False

        if position == 1:
            self.insert_first(song)
            return True

        if position == self.count + 1:
            self.insert_last(song)
            return True

        new_node = Node(song)
        current = self.head
        for _ in range(position - 2):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.count += 1
        return True

    def search(self, song_id):
        current = self.head
        while current is not None:
            if current.song.song_id == song_id:
                return current.song
            current = current.next
        return None

    def delete(self, song_id):
        current = self.head
        previous = None

        while current is not None:
            if current.song.song_id == song_id:
                if previous is None:          
                    self.head = current.next
                else:
                    previous.next = current.next
                self.count -= 1
                return True
            previous = current
            current = current.next

        return False

    def display(self):
        if self.is_empty():
            print("The playlist is empty.")
            return

        print("-" * 50)
        current = self.head
        position = 1
        while current is not None:
            print(f"Track #{position}")
            print(current.song)
            print("-" * 50)
            current = current.next
            position += 1

        print(f"Total songs: {self.count}")

def read_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def read_position(prompt, max_position):
    while True:
        value = input(prompt).strip()
        if value.isdigit() and 1 <= int(value) <= max_position:
            return int(value)
        print(f"Please enter a valid position between 1 and {max_position}.")


def read_menu_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print("Invalid choice. Please try again.")

def print_menu():
    print("\n================================")
    print("     MUSIC PLAYLIST MANAGER")
    print("================================")
    print("1. Add Song at Beginning")
    print("2. Add Song at End")
    print("3. Insert Song at Position")
    print("4. Display Playlist")
    print("5. Search Song")
    print("6. Remove Song")
    print("7. Display Playlist Size")
    print("8. Exit")


def read_new_song(playlist, song_id):
    title = read_non_empty("Song Title: ")
    artist = read_non_empty("Artist: ")
    duration = read_non_empty("Duration (e.g. 4:23): ")
    return Song(song_id, title, artist, duration)


def add_song_beginning(playlist):
    print("\n-- Add Song at Beginning --")
    song_id = read_non_empty("Song ID: ")
    if playlist.search(song_id) is not None:
        print(f"A song with ID {song_id} already exists.")
        return
    song = read_new_song(playlist, song_id)
    playlist.insert_first(song)
    print("Song added at the beginning.")


def add_song_end(playlist):
    print("\n-- Add Song at End --")
    song_id = read_non_empty("Song ID: ")
    if playlist.search(song_id) is not None:
        print(f"A song with ID {song_id} already exists.")
        return
    song = read_new_song(playlist, song_id)
    playlist.insert_last(song)
    print("Song added at the end.")


def insert_song_at_position(playlist):
    print("\n-- Insert Song at Position --")
    max_position = playlist.size() + 1
    position = read_position(f"Enter position (1-{max_position}): ", max_position)

    song_id = read_non_empty("Song ID: ")
    if playlist.search(song_id) is not None:
        print(f"A song with ID {song_id} already exists.")
        return

    song = read_new_song(playlist, song_id)
    if playlist.insert_at(position, song):
        print(f"Song inserted at position {position}.")
    else:
        print("Could not insert song at that position.")


def display_playlist(playlist):
    print("\n-- Playlist --")
    playlist.display()


def search_song(playlist):
    print("\n-- Search Song --")
    song_id = read_non_empty("Enter Song ID to search: ")
    song = playlist.search(song_id)

    if song is None:
        print(f"No song found with ID {song_id}.")
    else:
        print("Song found:")
        print(song)


def remove_song(playlist):
    print("\n-- Remove Song --")
    song_id = read_non_empty("Enter Song ID to remove: ")

    if playlist.delete(song_id):
        print("Song removed successfully.")
    else:
        print(f"No song found with ID {song_id}.")


def main():
    playlist = LinkedList()

    while True:
        print_menu()
        choice = read_menu_choice(
            "Enter your choice: ", {"1", "2", "3", "4", "5", "6", "7", "8"}
        )

        if choice == "1":
            add_song_beginning(playlist)
        elif choice == "2":
            add_song_end(playlist)
        elif choice == "3":
            insert_song_at_position(playlist)
        elif choice == "4":
            display_playlist(playlist)
        elif choice == "5":
            search_song(playlist)
        elif choice == "6":
            remove_song(playlist)
        elif choice == "7":
            print(f"Total songs in playlist: {playlist.size()}")
        elif choice == "8":
            print("Exiting Music Playlist Manager. Goodbye!")
            break


if __name__ == "__main__":
    main()