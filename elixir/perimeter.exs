# https://www.codewars.com/kata/559a28007caad2ac4e000083/train/elixir

defmodule Perim do
    def perimeter(n), do: loop({1, 1}, 8, n)
    
    defp loop(_, sum, 1), do: sum
    defp loop({a, b}, sum, n), do: loop({b, a+b}, sum + 4*(a+b), n-1)
end

IO.puts Perim.perimeter 7

# Can be solved with Stream lib
