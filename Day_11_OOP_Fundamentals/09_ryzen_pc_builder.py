# Day 11: Ryzen PC Builder
# Concept: Object-oriented model for PC components and upgrades.

class Component:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

    def __str__(self):
        return f"{self.brand} {self.name} (${self.price})"

class CPU(Component):
    def __init__(self, name, cores, threads, price):
        super().__init__(name, "AMD Ryzen", price)
        self.cores = cores
        self.threads = threads

class Workstation:
    def __init__(self, owner):
        self.owner = owner
        self.components = {}

    def install_component(self, category, component):
        self.components[category] = component
        print(f"Installed {component} as {category}.")

    def total_cost(self):
        return sum(c.price for c in self.components.values())

# Building a Ryzen Workstation
my_pc = Workstation("Krish")

ryzen_9 = CPU("9 7950X", 16, 32, 550)
gpu = Component("RTX 4080 Super", "NVIDIA", 999)
ram = Component("32GB DDR5 6000MHz", "G.Skill", 120)

my_pc.install_component("CPU", ryzen_9)
my_pc.install_component("GPU", gpu)
my_pc.install_component("RAM", ram)

print(f"\nTotal Build Cost for {my_pc.owner}: ${my_pc.total_cost()}")
