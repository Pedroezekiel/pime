from dataclasses import dataclass


@dataclass(frozen=True)
class Player:
    name: str
    sign: str

# class Player:
#     def __init__(self, name: str, sign: str) -> None:
#         self.name = name
#         self.sign = sign
if  __name__ == "__main__":
    player1 = Player("segun","x")
    print(player1.name)