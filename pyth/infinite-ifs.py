retar=lambda minr, maxr, init_enum: {
    'msg': 'sup', 
    'cnd': ''.join(
        f'if {j} else {i} ' 
        for (i, j)
        in enumerate(range(minr, maxr), init_enum)
    )
}
bruh=retar(1, 100, 1)
exec(f"print('{bruh['msg']}' {bruh['cnd']})")
print(f"\nthe script,\nprint('{bruh['msg']}' {bruh['cnd'][:-1]})\nwas ran above")





"""
print('sup' if 1 else 1 if 2 else 2 if 3 else 3 if 4 else 4 if 5 else 5 if 6 else 6 if 7 else 7 
if 8 else 8 if 9 else 9 if 10 else 10 if 11 else 11 if 12 else 12 if 13 else 13 if 14 else 14 if 15 else 15 if 16 else 16 if 17 else 17 if 18 else 18 if 19 else 19 if 20 else 20 if 21 else 21 
if 22 else 22 if 23 else 23 if 24 else 24 if 25 else 25 if 26 else 26 if 27 else 27 if 28 else 28 if 29 else 29 if 30 else 30 if 31 else 31 if 32 else 32 if 33 else 33 if 34 else 34 if 35 else 35 if 36 else 36 if 37 else 37 if 38 else 38 if 39 else 39 if 40 else 40 if 41 else 41 if 42 else 42 if 43 else 43 if 44 else 44 if 45 else 45 if 46 else 46 if 47 else 47 if 48 else 48 if 49 
else 49 if 50 else 50 if 51 else 51 if 52 else 52 if 53 else 53 if 54 else 54 if 55 else 55 if 56 else 56 if 57 else 57 if 58 else 58 if 59 else 59 if 60 else 60 if 61 else 61 if 62 else 62 if 63 else 63 if 64 else 64 if 65 else 65 if 66 else 66 if 67 else 67 if 68 else 68 if 69 else 69 
if 70 else 70 if 71 else 71 if 72 else 72 if 73 else 73 if 74 else 74 if 75 else 75 if 76 else 76 if 77 else 77 if 78 else 78 if 79 else 79 if 80 else 80 if 81 else 81 if 82 else 82 if 83 else 83 if 84 else 84 if 85 else 85 if 86 else 86 if 87 else 87 if 88 else 88 if 89 else 89 if 90 else 90 if 91 else 91 if 92 else 92 if 93 else 93 if 94 else 94 if 95 else 95 if 96 else 96 if 97 
else 97 if 98 else 98 if 99 else 99)
"""
