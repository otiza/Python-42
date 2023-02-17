from vector import Vector

if __name__ == '__main__':
    from vector import Vector

    v1 = Vector([0.0, 13.0, -2.0, 3.0])
    print(v1)
    v5 = v1 * 4
    print(v5)
    print()

    v2 = Vector([[12.0], [24.0], [48.0]])
    print(v2)
    v6 = v2 * 2
    print(v6)
    print()

    v3 = Vector(5)
    print(v3)
    v7 = v3 + Vector([[0.0], [10.0], [20.0], [30.0], [40.0]])
    print(v7)
    print()

    v4 = Vector((10, 15))
    print("heyyyy")
    print(v4)
    v8 = v2 - Vector([[6.0], [12.0], [24.0]])
    print(v8)
    print()

    va = Vector([[1.0], [4.0],[5.0]])
    vb = Vector([[7.0], [9.0], [11.0]])
    vc = va.dot(vb)
    print(vc)
    print()

    va = Vector([1.0, 10.0, 100.0])
    vb = Vector([1.0 ,10.0, 100.0])
    vc = va.dot(vb)
    print(vc)
    print()

    print(v2.T())