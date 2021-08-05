defmodule TribonacciSequence do
  @spec tribonacci({number, number, number}, non_neg_integer) :: [number]
  def tribonacci(signature, n) do
    signature
    |> Stream.unfold(fn {a, b, c} -> {a, {b, c, a+b+c}} end)
    |> Enum.take(n)
  end
end
