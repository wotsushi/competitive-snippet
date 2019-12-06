#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(dead_code)]

fn main() {
    let (V, E): (usize, usize) = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        let mut iter = line.split_whitespace();
        (
            iter.next().unwrap().parse().unwrap(),
            iter.next().unwrap().parse().unwrap(),
        )
    };
    let (u, v, c): (Vec<usize>, Vec<usize>, Vec<i64>) = {
        let (mut u, mut v, mut c) = (vec![], vec![], vec![]);
        for _ in 0..E {
            let mut line: String = String::new();
            std::io::stdin().read_line(&mut line).unwrap();
            let mut iter = line.split_whitespace();
            u.push(iter.next().unwrap().parse().unwrap());
            v.push(iter.next().unwrap().parse().unwrap());
            c.push(iter.next().unwrap().parse().unwrap());
        }
        (u, v, c)
    };

    let _N = V;
    let _M = E;
    let _A = u;
    let _B = v;
    let _C = c;
    static INF: i64 = 1e15 as i64;

    // snip
    fn dfs(
        i: usize,
        t: usize,
        f: i64,
        G: &mut Vec<Vec<(usize, i64, usize)>>,
        next_edge: &mut Vec<usize>,
        level: &Vec<usize>,
    ) -> Option<i64> {
        if i == t {
            Some(f)
        } else {
            for k in next_edge[i]..G[i].len() {
                let (j, c, l) = G[i][k];
                if c > 0 && level[i] < level[j] {
                    if let Some(d) = dfs(j, t, std::cmp::min(f, c), G, next_edge, level) {
                        G[i][k] = (j, c - d, l);
                        let (_, w, _) = G[j][l];
                        G[j][l] = (i, w + d, k);
                        next_edge[i] = k;
                        return Some(d);
                    }
                }
            }
            next_edge[i] = G[i].len();
            None
        }
    }

    let flow = |s, t| {
        let mut G = vec![vec![]; _N + 1];
        for i in 0.._M {
            let k = G[_B[i]].len();
            let l = G[_A[i]].len();
            G[_A[i]].push((_B[i], _C[i], k));
            G[_B[i]].push((_A[i], 0, l));
        }
        let mut res = 0;
        loop {
            let mut level = vec![0; _N + 1];
            let mut q = std::collections::VecDeque::new();
            level[s] = 1;
            q.push_back(s);
            while let Some(i) = q.pop_front() {
                for &(j, c, _) in &G[i] {
                    if c > 0 && level[j] == 0 {
                        level[j] = level[i] + 1;
                        q.push_back(j);
                    }
                }
            }
            if level[t] == 0 {
                break;
            }
            let mut next_edge = vec![0; _N + 1];
            while let Some(f) = dfs(s, t, INF, &mut G, &mut next_edge, &level) {
                res += f;
            }
        }
        res
    };
    // snip

    let ans = flow(0, V - 1);

    println!("{}", ans);
}
