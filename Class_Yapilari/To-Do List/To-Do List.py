class Task:
    def __init__(self, name, completed=False):
        self.name = name
        self.completed = completed

    def __str__(self):
        return f"{'[X]' if self.completed else '[ ]'} {self.name}"


class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, name):
        self.tasks.append(Task(name))
        self.save_tasks()

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def list_tasks(self):
        print("Tamamlanmayan Görevler:")
        for i, task in enumerate(self.tasks):
            if not task.completed:
                print(f"{i}. {task}")

        print("\nTamamlanan Görevler:")
        for i, task in enumerate(self.tasks):
            if task.completed:
                print(f"{i}. {task}")

    def save_tasks(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            for task in self.tasks:
                file.write(f"{task.name}|{task.completed}\n")

    def load_tasks(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                for line in file:
                    name, completed = line.strip().split("|")
                    self.tasks.append(Task(name, completed == "True"))
        except FileNotFoundError:
            # Dosya bulunamazsa görev listesi boş kalır.
            self.tasks = []


def main():
    manager = TaskManager()

    while True:
        print("\n1. Görev Ekle")
        print("2. Görevi Tamamla")
        print("3. Görev Sil")
        print("4. Görevleri Listele")
        print("5. Çıkış")

        selection = input("Seçiminizi yapın: ")
        if selection == "1":
            name = input("Görev adı: ")
            manager.add_task(name)
        elif selection == "2":
            manager.list_tasks()
            index = int(input("Tamamlamak istediğiniz görevin numarası: "))
            manager.complete_task(index)
        elif selection == "3":
            manager.list_tasks()
            index = int(input("Silmek istediğiniz görevin numarası: "))
            manager.delete_task(index)
        elif selection == "4":
            manager.list_tasks()
        elif selection == "5":
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçim. Tekrar deneyin.")


if __name__ == "__main__":
    main()
