#![allow(non_snake_case)]
#![allow(unused_variables)]
#![allow(dead_code)]

// https://onlinejudge.u-aizu.ac.jp/courses/library/7/DPL/all/DPL_5_D

fn main() {

    let (n, k): (usize, usize) = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        let mut iter = line.split_whitespace();
        (
            iter.next().unwrap().parse().unwrap(),
            iter.next().unwrap().parse().unwrap()
        )
    };

    const _MOD: i64 = 1_000_000_007;
    fn modinv(x: i64) -> i64 {
        let mut a = x;
        let mut b = _MOD;
        let mut u = 1;
        let mut v = 0;
        while b != 0 {
            let t = a / b;
            a -= t * b;
            std::mem::swap(&mut a, &mut b);
            u -= t * v;
            std::mem::swap(&mut u, &mut v);
        }
        u %= _MOD;
        if u >= 0 { u } else { u + _MOD }
    }
    #[derive(Copy, Clone)]
    struct ModInt {
        x: i64
    }
    impl ModInt {
        fn new(x: i64) -> ModInt {
            let y = if x >= 0 {
                x % _MOD
            } else {
                (x + (1 - x / _MOD) * _MOD) % _MOD
            };
            ModInt {x: y}
        }
    }
    impl std::ops::Add<ModInt> for ModInt {
        type Output = ModInt;
        fn add(self, other: ModInt) -> ModInt {
            ModInt::new(self.x + other.x)
        }
    }
    impl std::ops::Add<i64> for ModInt {
        type Output = ModInt;
        fn add(self, other: i64) -> ModInt {
            ModInt::new(self.x + other)
        }
    }
    impl std::ops::Add<usize> for ModInt {
        type Output = ModInt;
        fn add(self, other: usize) -> ModInt {
            ModInt::new(self.x + (other as i64))
        }
    }
    impl std::ops::Sub<ModInt> for ModInt {
        type Output = ModInt;
        fn sub(self, other: ModInt) -> ModInt {
            ModInt::new(self.x - other.x)
        }
    }
    impl std::ops::Sub<i64> for ModInt {
        type Output = ModInt;
        fn sub(self, other: i64) -> ModInt {
            ModInt::new(self.x - other)
        }
    }
    impl std::ops::Sub<usize> for ModInt {
        type Output = ModInt;
        fn sub(self, other: usize) -> ModInt {
            ModInt::new(self.x - (other as i64))
        }
    }
    impl std::ops::Mul<ModInt> for ModInt {
        type Output = ModInt;
        fn mul(self, other: ModInt) -> ModInt {
            ModInt::new(self.x * other.x)
        }
    }
    impl std::ops::Mul<i64> for ModInt {
        type Output = ModInt;
        fn mul(self, other: i64) -> ModInt {
            ModInt::new(self.x * other)
        }
    }
    impl std::ops::Mul<usize> for ModInt {
        type Output = ModInt;
        fn mul(self, other: usize) -> ModInt {
            ModInt::new(self.x * (other as i64))
        }
    }
    impl std::ops::Div<ModInt> for ModInt {
        type Output = ModInt;
        fn div(self, other: ModInt) -> ModInt {
            ModInt::new(self.x * modinv(other.x as i64))
        }
    }
    impl std::ops::Div<i64> for ModInt {
        type Output = ModInt;
        fn div(self, other: i64) -> ModInt {
            ModInt::new(self.x * modinv(other))
        }
    }
    impl std::ops::Div<usize> for ModInt {
        type Output = ModInt;
        fn div(self, other: usize) -> ModInt {
            ModInt::new(self.x * modinv(other as i64))
        }
    }
    impl std::fmt::Display for ModInt {
        fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
            write!(f, "{}", self.x)
        }
    }

    let _N = n + k;
    // snip
    let fact: Vec<_> = (0..(_N + 1))
        .scan(ModInt::new(1),
            |f, i| {*f = if i == 0 { ModInt::new(1) } else { *f * i }; Some(*f)})
        .collect();
    fn comb(n: usize, r: usize, fact: &Vec<ModInt>) -> ModInt { fact[n] / (fact[r] * fact[n - r]) }
    // snip

    let ans = comb(n + k - 1, k - 1, &fact);

    println!("{}", ans);
}