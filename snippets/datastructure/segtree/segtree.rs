#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(dead_code)]

// https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_A

fn main() {
    // snip
    struct SegmentTree<T: Clone + Copy>{
        n: usize,
        f: fn(T, T) -> T,
        e: T,
        x: Vec<T>
    }

    impl<T: Clone + Copy> SegmentTree<T> {
        fn new(n: usize, f: fn(T, T) -> T, e: T) -> SegmentTree<T> {
            let m = 1 << format!("{:b}", n).len();
            SegmentTree { n: m, f: f, e: e, x: vec![e; 2 * m - 1] }
        }
        fn update(&mut self, i: usize, y: T) {
            let mut j = i + self.n - 1;
            self.x[j] = y;
            while j > 0 {
                j = (j - 1) / 2;
                self.x[j] = (self.f)(self.x[2 * j + 1], self.x[2 * j + 2]);
            }
        }
        fn find(&self, s: usize, t: usize) -> T { self.q(0, 0, self.n, s, t) }
        fn q(&self, i: usize, l: usize, r: usize, s: usize, t: usize) -> T {
            if l >= t || r <= s { self.e }
            else if s <= l && r <= t { self.x[i] }
            else {
                (self.f)(
                    self.q(2 * i + 1, l, (l + r) / 2, s, t),
                    self.q(2 * i + 2, (l + r) / 2, r, s, t)
                )
            }
        }
    }
    // snip

    let (n, q): (usize, usize) = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        let mut iter = line.split_whitespace();
        (
            iter.next().unwrap().parse().unwrap(),
            iter.next().unwrap().parse().unwrap()
        )
    };
    let (com, x, y): (Vec<usize>, Vec<usize>, Vec<usize>) = {
        let (mut com, mut x, mut y) = (vec![], vec![], vec![]);
        for _ in 0..q {
            let mut line: String = String::new();
            std::io::stdin().read_line(&mut line).unwrap();
            let mut iter = line.split_whitespace();
            com.push(iter.next().unwrap().parse().unwrap());
            x.push(iter.next().unwrap().parse().unwrap());
            y.push(iter.next().unwrap().parse().unwrap());
        }
        (com, x, y)
    };
    const INF: usize = (2 << 30) - 1;
    let mut segt = SegmentTree::new(n, std::cmp::min, INF);

    for i in 0..q {
        if com[i] == 0 { segt.update(x[i], y[i]); }
        else {
            let ans = segt.find(x[i], y[i] + 1);
            println!("{}", ans);
        }
    }
}