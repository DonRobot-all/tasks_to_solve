"""
https://www.codewars.com/kata/550f22f4d758534c1100025a
Once upon a time, on a way through the old wild mountainous west,…
… a man was given directions to go from one point to another. The directions
were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are
opposite, "WEST" and "EAST" too.
Going to one direction and coming back the opposite direction right away is a
needless effort. Since this is the wild west, with dreadful weather and not
much water, it's important to save yourself some energy, otherwise you might
die of thirst!
How I crossed a mountainous desert the smart way.
The directions given to the man are, for example, the following (depending on
the language):
- ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
- ['WEST']

- ["NORTH", "WEST", "SOUTH", "EAST"]
- ["NORTH", "WEST", "SOUTH", "EAST"]

# """


def dir_reduc(arr):
    direction = ({
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "WEST": "EAST",
        "EAST": "WEST"
    })
    for i in range(len(arr) - 1):
        if direction[arr[i]] == arr[i + 1]:
            del arr[i]
            del arr[i]
            return dir_reduc(arr)
    return arr


if __name__ == '__main__':
    print(dir_reduc(
        ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
        ))
    print(dir_reduc(["NORTH", "WEST", "SOUTH", "EAST"]))
