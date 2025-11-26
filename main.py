import flet as ft
import random

counter = 1
menuOpen = False

class DiceButton(ft.ElevatedButton):
    def __init__(self, text, button_clicked):
        super().__init__()
        self.text = text
        self.on_click = button_clicked
        self.data = text

class RollButton(ft.FilledButton):
    def __init__(self, text, button_clicked):
        super().__init__()
        self.text = text
        self.on_click = button_clicked
        self.width = 100
        self.height = 80
        self.data = ""

class ChainDiceRoller(ft.Container):
    def __init__(self):
        super().__init__()

        self.expand = True
 
        self.diceToRoll = ft.TextField(hint_text = "Dice to roll")
        #self.diceMenu = ft.ElevatedButton(text="Dice Menu", on_click = self.opendiceMenu)

        self.chainType = ft.Dropdown(
                editable = True,
                label = "Chain type",
                options = [
                    ft.dropdown.Option("None"),
                    ft.dropdown.Option("Match"),
                    ft.dropdown.Option("Sequential"),
                    ft.dropdown.Option("Near")
                ],
                value = "Match",
                #on_change = self.update()
                )
    
        self.diceButtons = ft.Column(
            visible = False,
            expand = True,
            alignment = ft.alignment.top_left,
                controls=[
                    ft.Row(
                        alignment = ft.alignment.top_left,
                        controls = [
                            DiceButton(text = "1d4", button_clicked = self.button_clicked),
                            DiceButton(text = "2d4", button_clicked = self.button_clicked),
                            DiceButton(text = "3d4", button_clicked = self.button_clicked),
                            DiceButton(text = "4d4", button_clicked = self.button_clicked),
                            DiceButton(text = "5d4", button_clicked = self.button_clicked),
                            DiceButton(text = "6d4", button_clicked = self.button_clicked),
                        ]
                    ),
                    ft.Row(
                        alignment = ft.alignment.top_left,
                        controls = [
                            DiceButton(text = "1d6", button_clicked = self.button_clicked),
                            DiceButton(text = "2d6", button_clicked = self.button_clicked),
                            DiceButton(text = "3d6", button_clicked = self.button_clicked),
                            DiceButton(text = "4d6", button_clicked = self.button_clicked),
                            DiceButton(text = "5d6", button_clicked = self.button_clicked),
                            DiceButton(text = "6d6", button_clicked = self.button_clicked),
                        ]
                    ),
                    ft.Row(
                        alignment = ft.alignment.top_left,
                        controls = [
                            DiceButton(text = "1d8", button_clicked = self.button_clicked),
                            DiceButton(text = "2d8", button_clicked = self.button_clicked),
                            DiceButton(text = "3d8", button_clicked = self.button_clicked),
                            DiceButton(text = "4d8", button_clicked = self.button_clicked),
                            DiceButton(text = "5d8", button_clicked = self.button_clicked),
                            DiceButton(text = "6d8", button_clicked = self.button_clicked),
                        ]
                    ),ft.Row(
                        alignment = ft.alignment.top_left,
                        controls = [
                            DiceButton(text = "1d10", button_clicked = self.button_clicked),
                            DiceButton(text = "2d10", button_clicked = self.button_clicked),
                            DiceButton(text = "3d10", button_clicked = self.button_clicked),
                            DiceButton(text = "4d10", button_clicked = self.button_clicked),
                            DiceButton(text = "5d10", button_clicked = self.button_clicked),
                            DiceButton(text = "6d10", button_clicked = self.button_clicked),
                        ]
                    ),
                    ft.Row(
                        alignment = ft.alignment.top_left,
                        controls = [
                            DiceButton(text = "1d12", button_clicked = self.button_clicked),
                            DiceButton(text = "2d12", button_clicked = self.button_clicked),
                            DiceButton(text = "3d12", button_clicked = self.button_clicked),
                            DiceButton(text = "4d12", button_clicked = self.button_clicked),
                            DiceButton(text = "5d12", button_clicked = self.button_clicked),
                            DiceButton(text = "6d12", button_clicked = self.button_clicked),
                        ]
                    ),ft.Row(
                        alignment = ft.alignment.top_left,
                        controls = [
                            DiceButton(text = "1d20", button_clicked = self.button_clicked),
                            DiceButton(text = "2d20", button_clicked = self.button_clicked),
                            DiceButton(text = "3d20", button_clicked = self.button_clicked),
                            DiceButton(text = "4d20", button_clicked = self.button_clicked),
                            DiceButton(text = "5d20", button_clicked = self.button_clicked),
                            DiceButton(text = "6d20", button_clicked = self.button_clicked),
                        ]
                    ),
                
                ]
        )
    
        self.choiceCL = ft.Column(
            expand = True,
            alignment = ft.alignment.top_left,
            controls = [
                self.diceToRoll,
                self.chainType,
                ft.Container(
                    expand = True,
                    alignment = ft.alignment.bottom_center,
                    content = RollButton(text = "Roll!",
                                        button_clicked = self.button_clicked)                
                )                    
            ]
        )

        self.resultCL = ft.Column(
            expand = True,
            scroll = ft.ScrollMode.ADAPTIVE,
            auto_scroll = True,
            alignment = ft.alignment.top_left,
            controls = [
            
            ]
        
        )

        self.dmCL = ft.Column(
            expand = False,
            alignment = ft.alignment.top_left,
            controls = [
                self.diceButtons
            ]
        
        )


        self.content = ft.Column(
            expand = True,
            controls = [
                ft.Row(
                    expand = True,
                    controls = [
                        self.choiceCL,
                        self.resultCL,
                        self.dmCL
                        
                    ]
                )
            ]
        )
        
        
    def button_clicked(self, e):

        diceList = []
        amountList = []
        resultList = []
        sortedResultList = []

        amount = ""
        dice = ""
        resultString = ""

        global counter
        isA = True
        seqChain = False
        nearChain = False

        i = 0
        j = 0
        k = 0
        place = 0
        total = 0
        chain = 0

        if len(e.control.data) > 0:
            dString = e.control.data
        else:    
            dString = self.diceToRoll.value

        print(dString)

        while i < len(dString):
                try:
                    int(dString[i])
                    if isA:
                        amount = amount + dString[i]
                        i += 1
                    else:
                        dice = dice + dString[i]
                        i += 1
                except:
                    if dString[i].isspace():
                        isA = True
                        diceList.append(int(dice))
                        dice = ""
                        i += 1
                    else:
                        isA = False
                        try:
                            amountList.append(int(amount))
                        except:
                            amountList.append(1)
                        amount = ""
                        i += 1

        diceList.append(int(dice))
            
        print(diceList)
        print(amountList)
        print(self.chainType.value)

        rollInfo = str(counter) + ". Rolling"
        while place < len(amountList):
            rollInfo = rollInfo + " " + str(amountList[place]) + "d" + str(diceList[place])
            place += 1


        place = 0

        while place < len(amountList):
            while j < amountList[place]:
                result = random.randint(1, diceList[place])
                resultString += str(result) + " "
                resultList.append(result)
                total += result
                chain += result
                j += 1

            resultString += "(" + str(chain) + ") "

            #Match
            if all(v == resultList[0] for v in resultList) and len(resultList) > 1 and ( self.chainType.value == "Match" or self.chainType.value == "Near" ):
                resultString += "Chain! "
                resultList = []
            #Sequential
            elif len(resultList) > 1 and ( self.chainType.value == "Sequential" ): 
                sortedResultList = resultList.copy()
                sortedResultList.sort()
                while k + 1 < len(sortedResultList):
                    if sortedResultList[k] + 1 == sortedResultList[k + 1]:
                        seqChain = True
                        k += 1
                    else:
                        seqChain = False
                        k += 1
                        break
                k = 0
                if seqChain:
                    resultString += "Chain! "
                    resultList = []
                else:
                    place += 1
                    resultList = []
            #Near
            elif len(resultList) > 1 and self.chainType.value == "Near":
                sortedResultList = resultList.copy()
                sortedResultList.sort()
                while k + 1 < len(sortedResultList):
                    if sortedResultList[k] + 1 == sortedResultList[k + 1] or sortedResultList[k] == sortedResultList[k + 1]:
                        nearChain = True
                        k += 1
                    else:
                        nearChain = False
                        k += 1
                        break
                k = 0
                if nearChain:
                    resultString += "Chain! "
                    resultList = []
                else:
                    place += 1
                    resultList = []
            else: 
                place += 1
                resultList = []

            chain = 0
            j = 0

        counter += 1
        self.resultCL.controls.append(ft.Text(rollInfo))
        self.resultCL.controls.append(ft.Text(resultString))
        self.resultCL.controls.append(ft.Text("For a total of: " + str(total)))
        self.resultCL.controls.append(ft.Divider(color="grey"))
        self.resultCL.update()    

        return True

    def opendiceMenu(self, e):
        global menuOpen

        if menuOpen == False:
            #self.mainPage.window.width += 400
            menuOpen = True
            self.dmCL.expand = True
            self.diceButtons.visible = True
        elif menuOpen == True:
            #self.mainPage.window.width -= 400
            menuOpen = False
            self.dmCL.expand = False
            self.diceButtons.visible = False

        self.update()
        



def main(page: ft.Page):
    page.title = "ChainDiceRoller"

    def toggleOnTop(e):
        page.window.always_on_top = not page.window.always_on_top
        onTop.checked = not onTop.checked
        page.update()

    def toggleDiceMenu(e):
        roller.diceButtons.visible = not roller.diceButtons.visible
        diceMenu.checked = not diceMenu.checked

        if diceMenu.checked:
            page.window.width += 400
        else:
            page.window.width -= 400
            
        page.update()
    
    page.window.height = 500
    page.window.width = 800
    page.window.min_height = 300
    page.window.min_width = 500

    onTop = ft.PopupMenuItem(
        text = "Always On Top", on_click = toggleOnTop
    )
    
    diceMenu = ft.PopupMenuItem(
        text = "Dice Menu", on_click = toggleDiceMenu
    )

    page.appbar = ft.AppBar(
        actions = [
            ft.PopupMenuButton(
                items = [
                    onTop,
                    diceMenu
                ]
            )
        ]
    )

    roller = ChainDiceRoller()

    page.add(roller)

    page.update()


ft.app(main)
