
def GetInputToCorrectForm(inputString):
        inputList = inputString.split(",")
        initialPrice = inputList.pop(0)
        
        for index, item in enumerate(inputList):
                if index % 2 == 0:
                        bidderList.append(item)
                else:
                        bidsList.append(item)

        return initialPrice

def GetHighestBidderAndBid(initialPrice):
        highestBidder = bidderList[0]
        highestBid = initialPrice

        for i in range(bidderList):
                if bidsList[i] > highestBid:
                        print("Implement Code")
                

        return highestBidder + "," + str(highestBid)

if __name__ == "__main__":
    try:
        f = open("Input.txt", "r")
        inputString = f.read()
    except:
        print("File was not Found")
    finally:
        f.close()

    bidderList = []; bidsList = []
    initialPrice = GetInputToCorrectForm(inputString)
    
    print(GetHighestBidderAndBid(initialPrice))