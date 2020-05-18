fn main() {
    let mut ndiv = 0;
    let mut n_def = 0.;
    let mut n: f64 = 1.;
    while &ndiv < &500 {
        let N: f64 = (n.powi(2) + n)/2.;
        let mut t_ndiv = 0;
        let max = (N.sqrt().trunc() + 1.) as i64;
        for i in 1..max {
            if N % (i as f64) == 0. {
                t_ndiv += 1;
            }
        }
        if approxequal(N, (max -1).pow(2)   as f64) {   
            t_ndiv = 2*t_ndiv - 1;
        }
        else {
            t_ndiv = 2*t_ndiv;
        }
        if t_ndiv > ndiv {
            ndiv = t_ndiv;
            n_def = N;
        }
        n += 1.;
    }
    println!("{0}, {1}",n_def,ndiv);
}

fn approxequal(a: f64, b: f64) -> bool {
    (a/b - 1.).abs() < 1e-6
}

