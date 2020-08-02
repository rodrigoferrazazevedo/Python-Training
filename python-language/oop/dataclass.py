from dataclasses import dataclass

@dataclass
class Body:
    name: str
    mass: float = 0
    speed: float = 1

    def kinetic_energy(self) -> float:
        return(self.mass * self.speed ** 2) / 2

body = Body('Ball', 19, 3.1415)
print(body.kinetic_energy())
print(body)