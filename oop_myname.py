class MyName:
    total_names = 0  

    def __init__(self, name=None, domain="itcollege.lviv.ua") -> None:
        if name is None:
            name = self.anonymous_user().name

        # перевірка імені
        if not name.isalpha():
            raise ValueError("Ім'я може містити лише літери!")

        self.name = name.capitalize()  #
        self.domain = domain

        MyName.total_names += 1
        self.my_id = MyName.total_names

    @property
    def whoami(self) -> str:
        return f"My name is {self.name}"

    @property
    def my_email(self) -> str:
        return self.create_email()

    @property
    def full_name(self) -> str:
        return f"User #{self.my_id}: {self.name} ({self.my_email})"

    def create_email(self) -> str:
        return f"{self.name}@{self.domain}"

    def name_length(self) -> int:
        return len(self.name)

    def save_to_file(self, filename="users.txt"):
        with open(filename, "a", encoding="utf-8") as f:
            f.write(self.full_name + "\n")

    @classmethod
    def anonymous_user(cls):
        return cls("Anonymous")

    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:
        return f"You say: {message}"


print

names = ("Bohdan", "Marta", "Anastasiia", None)

all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    print(f"""{">*<"*20}
Object: {me}
ID / Name: {me.my_id} / {me.name}
Whoami: {me.whoami}
Email: {me.my_email}
Full info: {me.full_name}
Name length: {me.name_length()}
Greeting: {me.say_hello("Привіт з ООП!")}
{"<*>"*20}""")

print(f"We are done. We create {MyName.total_names} names!")