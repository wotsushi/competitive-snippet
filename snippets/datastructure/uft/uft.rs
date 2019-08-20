#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(dead_code)]

// https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/1/DSL_1_A

// snip
struct UnionFindTree {
    parent: Vec<usize>,
    size: Vec<i64>
}

impl UnionFindTree {
    fn new(n: usize) -> UnionFindTree {
        UnionFindTree {
            parent: (0..(n + 1)).collect(),
            size: vec![1; n + 1]
        }
    }
    fn find(&mut self, x: usize) -> usize {
        if self.parent[x] != x {
            let parent_x = self.parent[x];
            self.parent[x] = self.find(parent_x);
        }
        self.parent[x]
    }
    fn same(&mut self, x: usize, y: usize) -> bool {
        self.find(x) == self.find(y)
    }
    fn size(&mut self, x: usize) -> i64 {
        let i = self.find(x);
        self.size[i]
    }
    fn union(&mut self, x: usize, y: usize) {
        let parent_x = self.find(x);
        let parent_y = self.find(y);
        if !self.same(x, y) {
            if self.size[parent_x] < self.size[parent_y] {
                self.size[parent_y] += self.size[parent_x];
                self.parent[parent_x] = parent_y;
            } else {
                self.size[parent_x] += self.size[parent_y];
                self.parent[parent_y] = parent_x;
            }
        }
    }
}
// snip

fn main() {
    let (n, q): (usize, usize) = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        let mut iter = line.split_whitespace();
        (
            iter.next().unwrap().parse().unwrap(),
            iter.next().unwrap().parse().unwrap()
        )
    };
    let (com, x, y): (Vec<i64>, Vec<usize>, Vec<usize>) = {
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

    let mut uft = UnionFindTree::new(n - 1);
    let ans = {
        let mut ans = vec![];
        for i in 0..q {
            if com[i] == 0 {
                uft.union(x[i], y[i]);
            } else {
                if uft.same(x[i], y[i]) {
                    ans.push(1);
                } else {
                    ans.push(0);
                }
            }
        }
        ans.iter().map(std::string::ToString::to_string).collect::<Vec<_>>().join("\n")
    };

    println!("{}", ans);
}
