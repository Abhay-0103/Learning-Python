love_type = "Rommantic" # Global Scop

def love_story():
    def marriage():
        global love_type
        love_type = "Rommantic + Drama + Sexual"
    marriage()

love_story()
print(f"Love Type: {love_type}")