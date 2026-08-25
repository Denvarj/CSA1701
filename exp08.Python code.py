"""Cryptarithmetic Problem: SEND + MORE = MONEY"""

def solve_send_more_money():
    letters = set("SENDMORY")
    for s in range(10):
        for e in range(10):
            for n in range(10):
                for d in range(10):
                    for m in range(1, 10):
                        for o in range(10):
                            for r in range(10):
                                for y in range(10):
                                    digits = {ch: 0 for ch in letters}
                                    vals = [s, e, n, d, m, o, r, y]
                                    if len(set(vals)) < len(vals):
                                        continue
                                    digits["S"], digits["E"], digits["N"], digits["D"] = s, e, n, d
                                    digits["M"], digits["O"], digits["R"], digits["Y"] = m, o, r, y
                                    if digits["S"] == 0 or digits["M"] == 0:
                                        continue
                                    send = digits["S"] * 1000 + digits["E"] * 100 + digits["N"] * 10 + digits["D"]
                                    more = digits["M"] * 1000 + digits["O"] * 100 + digits["R"] * 10 + digits["E"]
                                    money = digits["M"] * 10000 + digits["O"] * 1000 + digits["N"] * 100 + digits["E"] * 10 + digits["Y"]
                                    if send + more == money:
                                        return digits
    return None

if __name__ == "__main__":
    print("Solution:", solve_send_more_money())
