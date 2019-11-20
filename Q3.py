def isCollisionDetected(rec1, rec2):
    rec1_xi = rec1["bottomLeft"][0]
    rec1_xf = rec1["topRight"][0]
    rec1_yi = rec1["bottomLeft"][1]
    rec1_yf = rec1["topRight"][1]

    rec2_xi = rec2["bottomLeft"][0]
    rec2_xf = rec2["topRight"][0]
    rec2_yi = rec2["bottomLeft"][1]
    rec2_yf = rec2["topRight"][1]

    if (rec1_xi < rec2_xf and rec1_xf > rec2_xi and rec1_yi < rec2_yf and rec1_yf > rec2_yi):
        return True
    return False

def main():
    rectangle = {"bottomLeft":"",
             "topRight":""}

    BLx = float(input())
    BLy = float(input())
    TRx = float(input())
    TRy = float(input())

    BL1 = (BLx, BLy)
    TR1 = (TRx, TRy)
    
    rec1 = rectangle.copy()
    rec1["bottomLeft"] = BL1
    rec1["topRight"] = TR1
    
    BLx = float(input())
    BLy = float(input())
    TRx = float(input())
    TRy = float(input())

    BL2 = (BLx, BLy)
    TR2 = (TRx, TRy)

    rec2 = rectangle.copy()
    rec2["bottomLeft"] = BL2
    rec2["topRight"] = TR2

    colidiu = isCollisionDetected(rec1, rec2)

    if colidiu == True:
        print("Colisao detectada")

    else:
        print("Colisao nao detectada")

main()
