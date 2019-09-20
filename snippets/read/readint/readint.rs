fn main() {
    // snip
    let _N: _i64 = {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        line.trim().parse().unwrap()
    };
    // snip
}