defmodule TribonacciSequence do

  @spec tribonacci({number, number, number}, non_neg_integer) :: [number]
  def tribonacci(signature, n) do
    if n < 3 do
      signature
      |> Tuple.to_list
      |> Enum.slice(0, n)
    else
      signature
      |> Tuple.to_list
      |> Enum.reverse
      |> my_trib(n-3)
      |> Enum.reverse
    end
  end
  def my_trib(seq, 0), do: seq
  def my_trib([a, b, c | tail], n), do: my_trib([a+b+c, a, b, c | tail], n-1)
end

IO.puts(inspect(TribonacciSequence.tribonacci({1,1,1}, 2)))
IO.puts(inspect(TribonacciSequence.tribonacci({1,1,1}, 0)))
IO.puts(inspect(TribonacciSequence.tribonacci({1,1,1}, 10)))
