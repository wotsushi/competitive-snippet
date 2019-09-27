#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(dead_code)]

// https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_A

fn main() {
    let (_N, _M): (usize, usize) = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        let mut iter = line.split_whitespace();
        (
            iter.next().unwrap().parse().unwrap(),
            iter.next().unwrap().parse().unwrap()
        )
    };
    let (_A, _B): (Vec<usize>, Vec<usize>) = {
        let (mut _A, mut _B) = (vec![], vec![]);
        for _ in 0.._M {
            let mut line: String = String::new();
            std::io::stdin().read_line(&mut line).unwrap();
            let mut iter = line.split_whitespace();
            _A.push(iter.next().unwrap().parse().unwrap());
            _B.push(iter.next().unwrap().parse().unwrap());
        }
        (_A, _B)
    };
    // snip
    let _G = {
        let mut _G = vec![std::collections::HashSet::new(); _N + 1];
        for i in 0.._M {
            _G[_A[i]].insert(_B[i]);
            _G[_B[i]].insert(_A[i]);
        }
        _G
    };
    // snip

    let (V, E) = (_N, _M);
    let (s, t) = (_A, _B);
    let G = _G;
    fn f(i: usize, depth: usize, G: &Vec<std::collections::HashSet<usize>>,
            order: &mut Vec<usize>, is_articulation: &mut Vec<bool>) -> usize {
        if order[i] < INF { order[i] }
        else {
            order[i] = depth;
            let mut res = depth;
            for &j in &G[i] {
                let d = f(j, depth + 1, G, order, is_articulation);
                if d == depth { is_articulation[i] = true; }
                res = std::cmp::min(res, d);
            }
            res
        }
    }

    const INF: usize = 1_000_000_000;
    let mut order = vec![INF; V];
    let mut is_articulation = vec![false; V];
    f(0, 0, &G, &mut order, &mut is_articulation);
    is_articulation[0] = (0..V).filter(|&i| order[i] == 1).count() >= 2;
    let ans = (0..V)
        .filter(|&i| is_articulation[i])
        .map(|i| i.to_string())
        .collect::<Vec<_>>()
        .join("\n");

    if ans != "" { println!("{}", ans) };
}