import time
from ro_pollard import p_pollard
from brilhart_morrison import canonical_decomposition


numbers = [
    3009182572376191,
    1021514194991569,
    4000852962116741,
    15196946347083,
    499664789704823,
    269322119833303,
    679321846483919,
    96267366284849,
    61333127792637,
    2485021628404193
]

# Time check for ro pollard
for num in numbers:
    start_time = time.time()
    res = p_pollard(num)
    print(f'Число {num} - {time.time() - start_time}')
    print(f"Нетривіальний дільник числа {num} це {res}")


# Time check for brilhart morrison pollard
for num in numbers:
    start_time = time.time()
    res = canonical_decomposition(num, 200)
    print(f'Число {num} - {time.time() - start_time}')
    res = list(res.keys())[0]
    print(f"Нетривіальний дільник числа {num} це {res}")

