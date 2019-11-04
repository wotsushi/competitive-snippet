#![allow(non_snake_case)]
#![allow(unused_variables)]

// https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/all/ALDS1_8_D

fn main() {
    let m: usize = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        line.trim().parse().unwrap()
    };
    let cmds: Vec<String> = (0..N).map(|_| {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        line.trim().to_string()
    }).collect();

    // snip
    struct Treap<T: Copy + Ord> {
        root: Option<&Node<T>>
    }
    struct TreapNode<T: Copy + Ord> {
        k: T,
        p: i64,
        l: Option<&TreapNode<T>>,
        r: Option<&TreapNode<T>>
    }

    fn merge<T: Copy + Ord>(x: &mut Option<&TreapNode<T>>, y: &mut Option<&TreapNode<T>>) -> &TreapNode<T> {
        if let mut Some(a) = &x {
            if let mut Some(b) = &y {
                if a.p > b.p {
                    a.r = merge(a.r, y);
                    a
                } else {
                    b.l = merge(x, b.l);
                    b
                }
            } else {
                a
            }
        } else {
            y.unwrap()
        }
    }

    fn split<T: Copy + Ord>(x: &mut Option<&TreapNode<T>>, key: T) -> (&Option<&TreapNode<T>>, &Option<&TreapNode<T>>) {
        if let mut Some(a) = &x {
            if key < a.k {
                let (l, r) = split(a.l, key);
                a.l = r;
                (l, a)
            } else {
                let (l, r) = split(a.r, key);
                a.r = l;
                (a, r)
            }
        } else {
            (None, None)
        }
    }

    impl<T: Copy + Ord> Treap<T> {
        fn new() -> Treap<T> { }
        fn insert(&mut self, x: T) { }
        fn remove(&mut self, x: T) { }
        fn lower_bound(&self, x: T) -> T { }
        fn upper_bound(&self, x: T) -> T { }
    }
    impl<T: Copy + Ord> TreapNode<T> {
        fn new(key: T) -> TreapNode<T> { }
        fn insert(&mut self, node: TreapNode<T>) { }
        fn remove(&mut self, x: T) { }
        fn lower_bound(&self, x: T) -> T { }
        fn upper_bound(&self, x: T) -> T { }
    }
    // snip


    let ans = fact[(n + k - 1) as usize] / (fact[(k - 1) as usize] * fact[n as usize]);

    println!("{}", ans);
}
