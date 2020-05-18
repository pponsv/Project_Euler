fn main() {
    let max: i64 = 2_000_000;
    // let mut numbers = vec!((0 .. max+1).collect());
    let mut numbers: Vec<i64> = (0 .. max+1).collect();
    for i in 2 .. max+1 {
        let mut n: i64 = 2;
        let mut k: i64 = i*n;
        if numbers[i as usize] != 0 {
            while k <= max {
                (*numbers)[k as usize] = 0i64;
                n += 1;
                k = i*n;
            }
        }
    }
    // let new_numbers = numbers as Vec<f64>;
    let mut sum: i64 = numbers.iter().sum();
    sum = sum - 1;
    println!("{:?}",sum);
}
