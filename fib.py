# (define (fact1 n)
#   (if (= n 1) 1
#       (* n (fact1 (- n 1)))))

# Recursive process
def fact1(n):
    return 1 if 1 == n else n * fact1(n-1)

# (define (fact2 n)
#   (define (loop i result)
#     (if (= i 1)
#         result
#         (loop (- i 1) (* i result))))
#   (loop n 1))

# Iterative process
def fact2(n):
    def loop(i, result):
        return result if 1 == i else loop(i - 1, i*result)
    
    return loop(n, 1)

# (define (fact-cc n cc)
#   (if (= n 0) (cc 1)
#               (fact-cc (- n 1) (lambda (x) (cc (* n x))))))
# (fact-cc 2 (lambda (x) x))
def fact_cc(n):
    def _fact_cc(n, cc):
        return cc(1) if 0 == n else _fact_cc(n-1, lambda x: cc(n*x))
    return _fact_cc(n, lambda x: x)

# (define (fib1 n)
#   (cond ((= n 0) 0)
#         ((= n 1) 1)
#         (else (+ (fib1 (- n 1)) (fib1 (- n 2))))))

# Non-lineary recursive process
def fib1(n):
    if 0 == n:
        return 0
    if 1 == n:
        return 1
    return fib1(n-1) + fib1(n-2)

# (define (fib2 n)
#   (define (loop i fib-n-1 fib-n-2)
#     (if (= i 0) fib-n-2
#                 (loop (- i 1) (+ fib-n-1 fib-n-2) fib-n-1)))
#   (loop n 1 0))

# Lineary iterative process
def fib2(n):
    def loop(i, fib_n_1, fib_n_2):
        return fib_n_2 if 0 == i else loop(i-1, fib_n_1 + fib_n_2, fib_n_1)
    return loop(n, 1, 0)

# (define fib-table (make-table))
# (define (memo-fib n)
#   (cond ((= n 0) 0)
#         ((= n 1) 1)
#         (else (let ((res (lookup fib-table n)))
#           (if res res
#                   (let ((val (+ (memo-fib (- n 1)) (memo-fib (- n 2)))))
#                     (insert! fib-table n val) val))))))

from collections import defaultdict
fib_table = defaultdict(lambda: None)

def memo_fib(n):
    if 0 == n:
        return 0
    if 1 == n:
        return 1
    if res := fib_table[n]:
        return res
    val = memo_fib(n-1) + memo_fib(n-2)
    fib_table[n] = val
    return val

fib_table_2 = defaultdict(lambda: None)

def memo_fib2(n):
    def loop(i, n_1, n_2):
        if res := fib_table_2[i]:
            return res
        return n_2 if 0 == i else loop(i-1, n_1 + n_2, n_1)
    return loop(n, 1, 0)

# print(f"{fib1(30)}, {fib2(30)}, {memo_fib(30)}, {memo_fib2(30)}")

# (define (reverse-simple lst)
#   (if (null? lst) ‘()
#       (append (reverse-simple (cdr lst)) (list (car lst)))))

def reverse_simple(lst):
    if [] == lst:
        return []
    print(lst)
    return reverse_simple(lst[1:]) + [lst[0]]

# (define (reverse-cps lst cc)
#   (if (null? lst) (cc ‘())
#       (reverse-cps (cdr lst) (lambda (x) (cc (append x (list (car lst))))))))
    
def reverse_cps(lst):
    def _reverse_cps(lst, cc):
        def continuation(x):
            return cc(x + [lst[1]])

        if [] == lst:
            return cc([])
        return _reverse_cps(lst[1:], continuation)
    return _reverse_cps(lst, lambda x: x)

# TODO: optimization
# print(reverse_cps(range(1000)))

(define (fibcc n, c)
  (cond ((= 0 n) (cc 0))
        ((= 1 n) (cc 1))
        (else (fibcc
                (- n 1)
                (lambda (r1) (fibcc
                               (- n 2)
                               (lambda (r2) (cc r1 + r2))))))))