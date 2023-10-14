def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    power = []
    for i in range(len(mat)):
        mat[i] = sum(mat[i])
        power.append(mat[i])
    
    power.sort()
    
    ranking = []
    for i in range(len(power)):
        ranking.append(mat.index(power[i]))
        mat[mat.index(power[i])] = None

    return ranking[0:k]