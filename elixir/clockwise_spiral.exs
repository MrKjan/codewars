defmodule Clockwise_spiral do
  def create_spiral(n) do
  coord_to_val = fn {x, y} ->
    deep = Enum.min([x, y, n+1-x, n+1-y)
    cond do
      y >= x and x+y <= n+1 -> 
        offset = y + 1 - deep
        {x, y, deep, offset, :top}
      y >= x and x+y > n+1 ->
        {x, y, deep, offset, :right}
      y < x and x+y >= n+1 ->
        {x, y, deep, offset, :bottom}
      true ->
        {x, y, deep, offset, :left}
    end
  end
    for x <- 1..n do
      for y <- 1..n do
        {x, y}
      end
    end
    |> List.flatten
    |> Enum.map(coord_to_val)
    |> Enum.chunk_every(n)
  end
  # defp coord_to_val(x, y, n) when x <= (n+1)/2 and ((x <= x >= y) or ()), do: true
end

IO.puts inspect Clockwise_spiral.create_spiral 4
