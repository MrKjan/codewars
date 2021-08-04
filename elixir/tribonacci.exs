defmodule TribonacciSequence do

  @spec tribonacci({number, number, number}, non_neg_integer) :: [number]
  def tribonacci(signature, n) do
    ret =
      signature
      |> Tuple.to_list
      |> Enum.reverse
    my_trib(signature, ret, n-3)
    |> Enum.reverse
  end

  def my_trib(_, ret, 0) do ret end

  def my_trib(sig, ret, n) when

  def my_trib(sig, seq, n) do
    {first, second, third} = sig
    new = first + second + third
    my_trib({second, third, new}, [new | seq], n-1)
  end
end

IO.puts(inspect(TribonacciSequence.tribonacci({0.5, 0.5, 0.5}, 4)))
