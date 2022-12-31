import pygame
import sys
from tkinter import *
import time

def pygame_calculator():
    pygame.init()

    window = pygame.display.set_mode((465,500))
    pygame.display.set_caption("yair's calculator")

    white = (255, 255, 255)
    color_dark = (100, 100, 100)

    width = window.get_width()
    """width is the width of the screen"""

    height = window.get_height()
    """height is the height of the screen"""

    smallfont = pygame.font.SysFont('Corbel', 35)
    """small_font is the font of the text that on the button"""
    text = smallfont.render("quit", True, white)
    sero_text = smallfont.render("0", True, white)
    one_text = smallfont.render("1", True, white)
    two_text = smallfont.render("2", True, white)
    three_text = smallfont.render("3", True, white)
    four_text = smallfont.render("4", True, white)
    five_text = smallfont.render("5", True, white)
    six_text = smallfont.render("6", True, white)
    seven_text = smallfont.render("7", True, white)
    eight_text = smallfont.render("8", True, white)
    nine_text = smallfont.render("9", True, white)
    point_text = smallfont.render(".", True, white)
    multiply_text = smallfont.render("*", True, white)
    devision_text = smallfont.render(":", True, white)
    less_text = smallfont.render("-", True, white)
    plues_text = smallfont.render("+", True, white)
    same_text = smallfont.render("=", True, white)
    action_text = smallfont.render("del", True, white)
    """action_text is the action fact() for example if you do fact(5) it will do 5*4*3*2*1"""
    closing_down1_text = smallfont.render(")", True, white)
    closing_down2_text = smallfont.render("(", True, white)

    window.fill(white)

    font_style = pygame.font.SysFont("bahnschrift", 35)
    global exercise
    exercise = ""
    global real_exercise
    real_exercise = ""
    def get_calculator_result(number, number_color):
        global real_exercise
        global exercise
        if exercise == "if you want to do a(b+c) so do a*(b+c)":
            exercise = ""
        if real_exercise == "if you want to do a(b+c) so do a*(b+c)":
            real_exercise = ""
        window.fill(white)
        exercise += str(number)
        if number == ":":
            real_exercise += "/"
        else:
            real_exercise += number
        mesg = font_style.render(exercise, True, number_color)
        window.blit(mesg, [10, 5])
    font_style2 = pygame.font.SysFont("bahnschrift", 20)
    def get_calculator_result2(number,number_color):
        global exercise
        global real_exercise
        window.fill(white)
        exercise += str(number)
        mesg = font_style2.render(exercise, True, number_color)
        window.blit(mesg, [10, 5])

    calculator_on = True
    while True:
        if calculator_on == True:
            mesg = font_style.render("0", True, (0,0,250))
            window.blit(mesg, [10, 5])
            calculator_on = False
        if len(exercise) == 0:
            window.fill(white)
            mesg = font_style.render("0", True, (0,0,250))
            window.blit(mesg, [10, 5])
            calculator_on = False
        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                pygame.quit()

            if ev.type == pygame.MOUSEBUTTONDOWN:
                """this if check if the mouse clicked"""

                if 0 <= mouse[0] <= 0 + 140 and 459 <= mouse[1] <= 459 + 40:
                    """if the mouse clicked on the quit button this start"""
                    pygame.quit()
                if 141 <= mouse[0] <= 141 + 115 and 459 <= mouse[1] <= 459 + 40:
                    """sero button"""
                    get_calculator_result("0",(0,0,250))
                if 374 <= mouse[0] <= 374 + 90 and 459 <= mouse[1] <= 459 + 40:
                    """same button"""
                    try:
                        real_exercise = str(eval(real_exercise))
                        check_exercise = real_exercise.split(".")
                        if check_exercise[-1] == "0":
                            get_calculator_result(" = " + check_exercise[0], (0, 0, 250))
                        else:
                            get_calculator_result(" = " + real_exercise, (0, 0, 250))
                        real_exercise = ""
                    except TypeError:
                        exercise = ""
                        real_exercise = ""
                        get_calculator_result2("if you want to do a(b+c) so do a*(b+c)",(0,0,250))

                if 257 <= mouse[0] <= 230 + 140 and 459 <= mouse[1] <= 459 + 40:
                    """point button"""
                    get_calculator_result(".",(0,0,250))
                if 373 <= mouse[0] <= 373 + 91 and 418 <= mouse[1] <= 418 + 40:
                    """plus button"""
                    get_calculator_result("+",(0,0,250))
                if 367 <= mouse[0] <= 367 + 116 and 367 <= mouse[1] <= 367 + 50:
                    """less button"""
                    get_calculator_result("-",(0,0,250))
                if 373 <= mouse[0] <= 373 + 91 and 316 <= mouse[1] <= 316 + 50:
                    """multiply button"""
                    get_calculator_result("*", (0,0,250))
                if 140 <= mouse[0] <= 140 + 116 and 418 <= mouse[1] <= 418 + 40:
                    """two button"""
                    get_calculator_result("2",(0,0,250))
                if 0 <= mouse[0] <= 0 + 139 and 418 <= mouse[1] <= 418 + 40:
                    """one button"""
                    get_calculator_result("1",(0,0,250))
                if 258 <= mouse[0] <= 258 + 113 and 418 <= mouse[1] <= 418 + 40:
                    """three button"""
                    get_calculator_result("3",(0,0,250))
                if 0 <= mouse[0] <= 0 + 139 and 367 <= mouse[1] <= 367 + 50:
                    """four button"""
                    get_calculator_result("4", (0,0,250))
                if 141 <= mouse[0] <= 141 + 115 and 367 <= mouse[1] <= 367 + 50:
                    """five button"""
                    get_calculator_result("5",(0,0,250))
                if 257 <= mouse[0] <= 257 + 115 and 367 <= mouse[1] <= 367 + 50:
                    """six button"""
                    get_calculator_result("6",(0,0,250))
                if 0 <= mouse[0] <= 0 + 139 and 316 <= mouse[1] <= 316 + 50:
                    """seven button"""
                    get_calculator_result("7",(0,0,250))
                if 140 <= mouse[0] <= 140 + 116 and 316 <= mouse[1] <= 316 + 50:
                    """eight button"""
                    get_calculator_result("8",(0,0,250))
                if 257 <= mouse[0] <= 257 + 116 and 316 <= mouse[1] <= 316 + 50:
                    """nine button"""
                    get_calculator_result("9",(0,0,250))
                if 373 <= mouse[0] <= 373 + 91 and 265 <= mouse[1] <= 265 + 50:
                    """devision button"""
                    get_calculator_result(":",(0,0,250))
                if 256 <= mouse[0] <= 256 + 116 and 256 <= mouse[1] <= 256 + 50:
                    """delete button"""
                    exercise = ""
                if 140 <= mouse[0] <= 140 + 115 and 265 <= mouse[1] <= 265 + 50:
                    """closing down1 button"""
                    get_calculator_result(")",(0,0,250))
                if 0 <= mouse[0] <= 0 + 138 and 265 <= mouse[1] <= 265 + 50:
                    """closing down2 button"""
                    get_calculator_result("(",(0,0,250))
                pygame.display.update()



        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()

        """in this ifs you check if the mouse is on a button if yes the button change color if not it stays in his color"""
        """in this if the first check is the width and thew other is the height"""
        if 0 <= mouse[0] <=  0 + 140 and 459 <= mouse[1] <= 459 + 40:
            """quit button"""
            pygame.draw.rect(window, (170,170,170), [0 , 459, 140, 40]) # in the three argoment the first 2 is where the button place when the mouse is on him the 3 argoment is the width of the button when the mouse on him and the 4 argoment is the height of the button when the mouse is on him(try to change them to understand better)
        else:
            pygame.draw.rect(window, (127,127,127), [0, 459, 140, 40])
        if 141 <= mouse[0] <= 141 + 115 and 459 <= mouse[1] <= 459 + 40:
            """sero button"""
            pygame.draw.rect(window, (170, 170, 170), [141, 459, 115, 40])
        else:
            pygame.draw.rect(window, (127, 127, 127), [141, 459, 115, 40])
        if 374 <= mouse[0] <= 374 + 90 and 459 <= mouse[1] <= 459 + 40:
            """same button"""
            pygame.draw.rect(window, (170, 170, 170), [374, 459, 90, 40])
        else:
            pygame.draw.rect(window, (127, 127, 127), [374, 459, 90, 40])
        if 257 <= mouse[0] <= 230 + 140 and 459 <= mouse[1] <= 459 + 40:
            """point button"""
            pygame.draw.rect(window, (170, 170, 170), [257, 459, 116, 40])
        else:
            pygame.draw.rect(window, (127, 127, 127), [257, 459, 116, 40])
        if 373 <= mouse[0] <= 373 + 91 and 418 <= mouse[1] <= 418 + 40:
            """plus button"""
            pygame.draw.rect(window, (170, 170, 170), [373, 418, 91, 40])
        else:
            pygame.draw.rect(window, (127, 127, 127), [373, 418, 91, 40])
        if 367 <= mouse[0] <= 367 + 116 and 367 <= mouse[1] <= 367 + 50:
            """less button"""
            pygame.draw.rect(window, (170, 170, 170), [373, 367, 116, 50])
        else:
            pygame.draw.rect(window, (127, 127, 127), [373, 367, 91, 50])
        if 373 <= mouse[0] <= 373 + 91 and 316 <= mouse[1] <= 316 + 50:
            """multiply button"""
            pygame.draw.rect(window, (170, 170, 170), [373, 316, 91, 50])
        else:
            pygame.draw.rect(window, (127, 127, 127), [373, 316, 91, 50])
        if 140 <= mouse[0] <= 140 + 116 and 418 <= mouse[1] <= 418 + 40:
            """two button"""
            pygame.draw.rect(window, (170, 170, 170), [140, 418, 116, 40])
        else:
            pygame.draw.rect(window, (127, 127, 127), [140, 418, 116, 40])
        if 0 <= mouse[0] <= 0 + 139 and 418 <= mouse[1] <= 418 + 40:
            """one button"""
            pygame.draw.rect(window, (170, 170, 170), [0, 418, 139, 40])
        else:
            pygame.draw.rect(window, (127, 127, 127), [0, 418, 139, 40])
        if 258 <= mouse[0] <= 258 + 113 and 418 <= mouse[1] <= 418 + 40:
            """three button"""
            pygame.draw.rect(window, (170, 170, 170), [258, 418, 114, 40])
        else:
            pygame.draw.rect(window, (127, 127, 127), [258, 418, 114, 40])
        if 0 <= mouse[0] <= 0 + 139 and 367 <= mouse[1] <= 367 + 50:
            """four button"""
            pygame.draw.rect(window, (170, 170, 170), [0, 367, 139, 50])
        else:
            pygame.draw.rect(window, (127, 127, 127), [0, 367, 139, 50])
        if 141 <= mouse[0] <= 141 + 115 and 367 <= mouse[1] <= 367 + 50:
            """five button"""
            pygame.draw.rect(window, (170, 170, 170), [141, 367, 115, 50])
        else:
            pygame.draw.rect(window, (127, 127, 127), [141, 367, 115, 50])
        if 257 <= mouse[0] <= 257 + 115 and 367 <= mouse[1] <= 367 + 50:
            """six button"""
            pygame.draw.rect(window, (170, 170, 170), [257, 367, 115, 50])
        else:
            pygame.draw.rect(window, (127, 127, 127), [257, 367, 115, 50])
        if 0 <= mouse[0] <= 0 + 139 and 316 <= mouse[1] <= 316 + 50:
            """seven button"""
            pygame.draw.rect(window, (170, 170, 170), [0, 316, 139, 50])
        else:
            pygame.draw.rect(window, (127, 127, 127), [0, 316, 139, 50])
        if 140 <= mouse[0] <= 140 + 116 and 316 <= mouse[1] <= 316 + 50:
            """eight button"""
            pygame.draw.rect(window, (170, 170, 170), [140, 316, 116, 50])
        else:
            pygame.draw.rect(window, (127, 127, 127), [140, 316, 116, 50])
        if 257 <= mouse[0] <= 257 + 116 and 316 <= mouse[1] <= 316 + 50:
            """nine button"""
            pygame.draw.rect(window, (170, 170, 170), [257, 316, 116, 50])
        else:
            pygame.draw.rect(window, (127, 127, 127), [257, 316, 115, 50])
        if 373 <= mouse[0] <= 373 + 91 and 265 <= mouse[1] <= 265 + 50:
            """devision button"""
            pygame.draw.rect(window, (170, 170, 170), [373, 265, 91, 50])
        else:
            pygame.draw.rect(window, (127, 127, 127), [373, 265, 91, 50])
        if 256 <= mouse[0] <= 256 + 116 and 256 <= mouse[1] <= 256 + 50:
            """delete button"""
            pygame.draw.rect(window, (170, 170, 170), [256, 265, 116, 50])
        else:
            pygame.draw.rect(window, (127, 127, 127), [256, 265, 116, 50])
        if 140 <= mouse[0] <= 140 + 115 and 265 <= mouse[1] <= 265 + 50:
            """closing down1 button"""
            pygame.draw.rect(window, (170, 170, 170), [140, 265, 115, 50])
        else:
            pygame.draw.rect(window, (127, 127, 127), [140, 265, 115, 50])
        if 0 <= mouse[0] <= 0 + 138 and 265 <= mouse[1] <= 265 + 50:
            """closing down2 button"""
            pygame.draw.rect(window, (170, 170, 170), [0, 265, 138, 50])
        else:
            pygame.draw.rect(window, (127, 127, 127), [0, 265, 138, 50])

        window.blit(text, (40, 459))
        window.blit(sero_text, (190,459))
        window.blit(point_text, (300,459))
        window.blit(less_text, (410,375))
        window.blit(plues_text, (410,420))
        window.blit(same_text, (410,459))
        window.blit(multiply_text, (410, 325))
        window.blit(two_text, (190, 420))
        window.blit(one_text, (65, 418))
        window.blit(three_text, (300, 415))
        window.blit(four_text, (65, 370))
        window.blit(five_text, (190, 370))
        window.blit(six_text, (300, 375))
        window.blit(seven_text, (65, 318))
        window.blit(eight_text, (190, 325))
        window.blit(nine_text, (300, 318))
        window.blit(devision_text, (415, 270))
        window.blit(action_text, (300, 270))
        window.blit(closing_down1_text, (200, 270))
        window.blit(closing_down2_text, (70, 270))
        pygame.display.update()
pygame_calculator()