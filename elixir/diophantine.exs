# https://www.codewars.com/kata/554f76dca89983cc400000bb/train/elixir
# Get list of divisors from 1 to sqrt(n)
# divisor and its pair are a and b where a > b
# x = (a+b)/2, y = (a-b)/4
# add them to solution if they are integers

defmodule Dioph do
  def sol_equa(n) do
    n
    |> get_div(1, [])
    |> Enum.flat_map(&([{&1, div(n, &1)}, {div(n, &1), &1}]))
    |> Enum.map(fn {a, b} -> [(a+b)/2, (a-b)/4] end)
    |> Enum.filter(&(Enum.fetch!(&1, 0) == Float.ceil(Enum.fetch!(&1, 0))
        and Enum.fetch!(&1, 1) == Float.ceil(Enum.fetch!(&1, 1))
        and Enum.fetch!(&1, 0) > 0 and Enum.fetch!(&1, 1) > 0))
    |> Enum.map(&to_pair/1)
    |> Enum.sort(:desc)
  end
  defp get_div(val, divisor, ret) do
    # IO.puts "#{val}, #{divisor}, #{inspect(ret)}"
    cond do
      divisor > :math.sqrt(val) -> ret
      rem(val, divisor) == 0 -> get_div(val, divisor + 1, [divisor | ret])
      true -> get_div(val, divisor + 1, ret)
    end
  end
  defp to_pair([x, y]) do
    {int_x, _} = Float.ratio x
    {int_y, _} = Float.ratio y
    {int_x, int_y}
  end
end

IO.puts inspect Dioph.sol_equa(20)
IO.puts inspect Dioph.sol_equa(90005)
IO.puts inspect Dioph.sol_equa(90002)
