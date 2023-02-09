import Second_step
import tkinter
import asyncio


async def main():
    screen = tkinter.Tk()

    screen.title("test")
    screen.geometry("600x400")

    Second_step.step_2_test().first_step()

    screen.mainloop()

asyncio.run(main())



