from PIL import Image

class User:
    def __init__(self, username, password, image_paths):
        self.username = username
        self.password = password
        self.image_paths = image_paths

class UserDatabase:
    def __init__(self):
        self.users = []

    def register_user(self, username, password, image_paths):
        # Check if username is already taken
        for user in self.users:
            if user.username == username:
                print("Username already taken. Please choose a different username.")
                return False

        # Load image files
        images = []
        for image_path in image_paths:
            try:
                image = Image.open(image_path)
                images.append(image)
            except IOError:
                print(f"Failed to load image file {image_path}.")
                return False

        # Create new user and add to database
        new_user = User(username, password, image_paths)
        self.users.append(new_user)
        print("Registration successful.")
        return True
