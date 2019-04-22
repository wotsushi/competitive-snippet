def code():
    def bis(p, ok, ng):
        mid = (ok + ng) // 2
        return (
            ok if abs(ok - ng) == 1 else
            bis(p, mid, ng) if p(mid) else
            bis(p, ok, mid)
        )
    return bis
