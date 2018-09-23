def evaluate():
    list_of_persons = data.get("persons");
        tally = {}
        for x in list_of_persons:
            tally[x] = 0
        expenses = data.get("expenses");
        for x in expenses:
            amount = x.get("amount")
            paidBy = x.get("paidBy")
            exclude = x.get("exclude")
            if ifinstance(exclude, list):
                payable = [a for a in list_of_persons if not (a in exclude)]
            else:
                payable = [a for a in list_of_persons if not exclude]
            eachpay = amount/len(payable)
            for x in payable:
                tally[x] += eachpay
            tally[paidBy] -= amount
        print(tally)