import flet as ft # type: ignore
import random
import socket
import os

counter = 1

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
        self.width = 60
        self.height = 40
        self.data = ""

class Macro(ft.Row):
    def __init__(self,macro_name, macro_dice, deleteMacro, button_clicked, editMacro):
        super().__init__()
        self.macro_dice = macro_dice
        self.deleteMacro = deleteMacro
        self.on_click = button_clicked
        self.macro_name = macro_name
        self.editMacros = editMacro

        self.nameField = ft.TextField(hint_text = "name", value = macro_name, width = 150, on_blur = self.renameMacro)

        self.controls = [
            self.nameField,
            DiceButton(text = self.macro_dice, button_clicked = button_clicked),
            ft.Container (
                expand = True,
                alignment = ft.alignment.top_right,
                content = (
                    ft.IconButton(
                        ft.Icons.DELETE_OUTLINE,
                        tooltip = "Delete macro",
                        on_click = self.deleteClick,
                    )
                )
            )
        ]

    def deleteClick(self, e):
        self.deleteMacro(self)
    
    def renameMacro(self, e):
        self.macro_name = self.nameField.value
        self.editMacros()


class ChainDiceRoller(ft.Container):
    def __init__(self):
        super().__init__()

        self.expand = True

        self.app_data_path = os.getenv("FLET_APP_STORAGE_DATA")
        self.macroPath = os.path.join(self.app_data_path, "saved_macros")

 
        self.diceToRoll = ft.TextField(hint_text = "Dice to roll", width = 200, on_submit = self.button_clicked)

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
                )
        
        self.luckyCheck = ft.Checkbox(label = "Lucky", value = False, on_change = self.luckySwitch)

        self.unluckyCheck = ft.Checkbox(label = "Unlucky", value = False, on_change = self.unluckySwitch)
        
        self.macros = ft.Column(
            expand = True,
            scroll = ft.ScrollMode.ADAPTIVE,
            controls = [
            ]            
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
                    ),ft.Row(
                        alignment = ft.alignment.top_left,
                        controls = [
                            DiceButton(text = "1d2", button_clicked = self.button_clicked),
                            DiceButton(text = "1d3", button_clicked = self.button_clicked),
                            DiceButton(text = "1d100", button_clicked = self.button_clicked)
                        ]
                    )
                ]
        )
    
        self.choiceCL = ft.Column(
            expand = True,
            alignment = ft.alignment.top_left,
            controls = [  
                ft.Row(
                    controls = [
                        self.diceToRoll,
                        RollButton(text = "Roll!", button_clicked = self.button_clicked),
                        ft.ElevatedButton(text = "Add as macro", on_click = self.addMacro) 
                    ]
                ), 
                ft.Row(
                    controls = [
                        self.chainType,
                        self.luckyCheck,
                        self.unluckyCheck,                       
                    ]
                ),
                self.macros            
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
        totalRolls = 1

        try:
            if len(e.control.data) > 0:
                dString = e.control.data
            else:    
                dString = self.diceToRoll.value
        except:
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

        if self.luckyCheck.value:
            rollInfo += " lucky"
            totalRolls = 2
        elif self.unluckyCheck.value:
            rollInfo += " unlucky"
            totalRolls = 2
        
        while place < len(amountList):
            rollInfo = rollInfo + " " + str(amountList[place]) + "d" + str(diceList[place])
            place += 1

        self.resultCL.controls.append(ft.Text(rollInfo))        

        while totalRolls > 0:

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

            self.resultCL.controls.append(ft.Text(resultString))
            self.resultCL.controls.append(ft.Text("For a total of: " + str(total)))

            totalRolls -= 1
            if totalRolls == 1:
                firstTotal = total
            if totalRolls == 0:
                secondTotal = total
            resultString = ""
            total = 0

        if self.luckyCheck.value:
            self.resultCL.controls.append(ft.Text("better roll is " + str(max(firstTotal, secondTotal))))
        elif self.unluckyCheck.value:
            self.resultCL.controls.append(ft.Text("worse roll is " + str(min(firstTotal, secondTotal))))


        self.resultCL.controls.append(ft.Divider(color = "grey"))
        self.resultCL.update()    

        counter += 1

        return total
    
    def luckySwitch(self, e):

        if self.luckyCheck.value:
            self.unluckyCheck.value = False

        self.update()

    def unluckySwitch(self, e):

        if self.unluckyCheck.value:
            self.luckyCheck.value = False

        self.update()


    def addMacro(self, e):

        macro = Macro("", self.diceToRoll.value, self.deleteMacro, self.button_clicked, self.editMacros)

        self.macros.controls.append(macro)

        with open(self.macroPath, "a") as file:
            file.write("," + self.diceToRoll.value + "\n")
        
        self.macros.update()

    def deleteMacro(self, macro):
        self.macros.controls.remove(macro)

        i = 0

        with open(self.macroPath, "w") as file:
            while i < len(self.macros.controls):
                file.write(self.macros.controls[i].macro_name + "," + self.macros.controls[i].macro_dice + "\n")
                i += 1

        self.macros.update()

    def editMacros(self):
        i = 0

        with open(self.macroPath, "w") as file:
            while i < len(self.macros.controls):
                file.write(self.macros.controls[i].macro_name + "," + self.macros.controls[i].macro_dice + "\n")
                i += 1

    def readMacros(self):
        namedice = []

        with open(self.macroPath) as file:
            l = file.readlines()
            for line in l:
                namedice = line.strip().split(",")

                macro = Macro(namedice[0], namedice[1], self.deleteMacro, self.button_clicked, self.editMacros)

                self.macros.controls.append(macro)

def main(page: ft.Page):
    page.title = "ChainDiceRoller"

    def toggleOnTop(e):
        page.window.always_on_top = not page.window.always_on_top
        page.update()

    def toggleDiceMenu(e):
        roller.diceButtons.visible = not roller.diceButtons.visible

        if diceMenu.value:
            page.window.width += 400
        else:
            page.window.width -= 400
            
        page.update()
    
    page.window.height = 500
    page.window.width = 800
    page.window.min_height = 400
    page.window.min_width = 600
    
    diceMenu = ft.Checkbox(
        label = "Dice Menu", on_change = toggleDiceMenu
    )

    onTop = ft.Checkbox(
        label = "Always on top", on_change = toggleOnTop
    )

    page.appbar = ft.AppBar(
        toolbar_height = 30,
        leading_width = 250,
        leading = ft.Row(
            controls = [
                diceMenu,
                onTop
            ]
        )
    )   

    try:
        s = socket.socket()

        port = 12345

        s.connect(("127.0.0.1", port))

        print(s.recv(1024).decode)
    except:
        print("server not online")
        
    roller = ChainDiceRoller()

    try:
        roller.readMacros()
    except:
        print("no saved macros")
        
    page.add(roller)

    page.update()


ft.app(main)
