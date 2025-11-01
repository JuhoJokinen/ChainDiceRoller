import flet as ft
import random

counter = 1

def main(page: ft.Page):

    def diceRoll(e):

        if len(diceToRoll.value) > 0:
            parseText()

        global counter
        #result = str(counter) + ". " + str(random.randint(1, 6))
        #counter += 1
        #resultCL.controls.append(ft.Text(result))
        #resultCL.update()

    def parseText():

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

        i = 0
        j = 0
        k = 0
        place = 0
        total = 0
        chain = 0

        dString = diceToRoll.value

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
        print(chainType.value)

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
            if all(v == resultList[0] for v in resultList) and len(resultList) > 1 and ( chainType.value == "Match" or chainType.value == "Near" ):
                resultString += "Chain! "
                resultList = []
            #Sequential
            elif len(resultList) > 1 and ( chainType.value == "Sequential" or chainType.value == "Near" ): 
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
            else: 
                place += 1
                resultList = []

            chain = 0
            j = 0

        counter += 1
        resultCL.controls.append(ft.Text(rollInfo))
        resultCL.controls.append(ft.Text(resultString))
        resultCL.controls.append(ft.Text("For a total of: " + str(total)))
        resultCL.controls.append(ft.Text("--------------------------------------------------"))
        resultCL.update()    

        return True

    diceToRoll = ft.TextField(hint_text = "Dice to roll")

    chainType = ft.Dropdown(
                editable = True,
                label = "Chain type",
                options = [
                    ft.dropdown.Option("None"),
                    ft.dropdown.Option("Match"),
                    ft.dropdown.Option("Sequential"),
                    ft.dropdown.Option("Near")
                ],
                value = "Match",
                on_change = page.update()
                )

    choiceCL = ft.Column(
        expand = True,
        height = page.height,
        alignment = ft.MainAxisAlignment.START,
        controls = [
            diceToRoll,
            chainType,
            ft.Container(
                expand = True,
                alignment = ft.alignment.bottom_center,
                content = ft.FilledButton(text = "Roll!",
                                          on_click=diceRoll,
                                          width = 150,
                                          height = 100)                
            )                    
        ]
    )

    resultCL = ft.Column(
        expand = True,
        height = page.height,
        scroll = ft.ScrollMode.ADAPTIVE,
        auto_scroll = True,
        alignment = ft.MainAxisAlignment.START,
        controls = [
            
        ]
        
    )
    
    page.add(
        ft.Column(
            expand = True,
            controls = [
            ft.Row(
                expand = True,
                controls = [
                    choiceCL,
                    resultCL
                ]
            )
            ]        
        )
    )


ft.app(main)
